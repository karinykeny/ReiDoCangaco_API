from flask_restful import Resource, reqparse
from models.forma_pagemento_model import FormaPagamentoModel
from models.pedido_model import PedidoModel
from resources.mensagem import formaPagamentoEmUso, FPNaoEncontrada
from resources.mensagem import fPJaExiste, erroSalvarFP
from resources.mensagem import erroExcluirFP, FPExcluida
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('tipo_formaPagamento', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('descricao_formaPagamento',  type=str,
                        required=True, help="Campo obrigatório.")


class FormasPagamento(Resource):
    def get(self):
        order = [fp.json()
                 for fp in FormaPagamentoModel.query.all()]
        return {'formasPagamento': order}


class FormaPagamento(Resource):

    def get(self, cod_formaPgameno):
        contato = FormaPagamentoModel.find_formaPagamento(cod_formaPgameno)
        if contato:
            return contato.json()
        return FPNaoEncontrada

    @jwt_required
    def put(self, cod_formaPgameno):
        dados = argumentos.parse_args()

        fp_encontrada = FormaPagamentoModel.find_formaPagamento(
            cod_formaPgameno)
        if fp_encontrada:
            if fp_encontrada.getTipoFormaPagamento() != dados['tipo_formaPagamento']:
                if FormaPagamentoModel.find_formaPagamento_tipo(
                        dados['tipo_formaPagamento']):
                    return fPJaExiste(dados['tipo_formaPagamento'])
            fp_encontrada.update_formaPagamento(cod_formaPgameno, **dados)
            try:
                fp_encontrada.save_formaPagamento()
            except ValueError:
                return erroSalvarFP
            return fp_encontrada.json(), 200
        return FPNaoEncontrada

    @jwt_required
    def delete(self, cod_formaPgameno):
        if PedidoModel.find_pedido_formaPgameno(cod_formaPgameno):
            return formaPagamentoEmUso(cod_formaPgameno)

        fp = FormaPagamentoModel.find_formaPagamento(cod_formaPgameno)
        if fp:
            try:
                fp.delete_formaPagamento()
            except ValueError:
                return erroExcluirFP
            return FPExcluida
        return FPNaoEncontrada


class FormaPagamentoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if FormaPagamentoModel.find_formaPagamento_tipo(
                dados['tipo_formaPagamento']):
            return fPJaExiste(dados['tipo_formaPagamento'])

        fp = FormaPagamentoModel(**dados)

        try:
            fp.save_formaPagamento()
        except ValueError:
            return erroSalvarFP
        return fp.json(), 200
