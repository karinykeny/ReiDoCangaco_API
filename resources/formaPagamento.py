from flask_restful import Resource, reqparse
from models.forma_pagemento_model import FormaPagamentoModel
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
        return {'msg': 'Forma de pagamento não encontrado.'}, 404

    @jwt_required
    def put(self, cod_formaPgameno):
        dados = argumentos.parse_args()

        fp_encontrada = FormaPagamentoModel.find_formaPagamento(
            cod_formaPgameno)
        if fp_encontrada:
            fp_encontrada.update_formaPagamento(**dados)
            fp_encontrada.save_formaPagamento()
            return fp_encontrada.json(), 200

        if FormaPagamentoModel.find_formaPagamento(dados['cod_formaPgameno']):
            return {'msg': 'Forma de pagamento com código "{}" já existe.'
                    .format(dados['cod_formaPgameno'])}, 400

        fp = FormaPagamentoModel(cod_formaPgameno, **dados)
        try:
            fp.save_formaPagamento()
        except ValueError:
            return {'msg': 'Erro ao salvar a forma de pagamento.'}, 500
        return fp.json(), 201

    @jwt_required
    def delete(self, cod_formaPgameno):
        fp = FormaPagamentoModel.find_formaPagamento(cod_formaPgameno)
        if fp:
            try:
                fp.delete_formaPagamento()
            except ValueError:
                return {'msg': 'Erro ao excluir a forma de pagamento.'}, 500
            return {'msg': 'Forma de pagamento excluída.'}
        return {'msg': 'Forma de pagamento não encontrado.'}, 404


class FormaPagamentoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if FormaPagamentoModel.find_formaPagamento_tipo(
                dados['tipo_formaPagamento']):
            return {'msg': 'Forma de pagamento "{}" já existe.'
                    .format(dados['tipo_formaPagamento'])}, 400

        fp = FormaPagamentoModel(**dados)

        try:
            fp.save_formaPagamento()
        except ValueError:
            return {'msg': 'Erro ao salvar a forma de pagamento.'}, 500
        return fp.json(), 200
