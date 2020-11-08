from flask_restful import Resource, reqparse
from models.produto_pedido_model import ProdutoPedidoModel
from models.pedido_model import PedidoModel
from models.produto_model import ProdutoModel
from resources.mensagem import produtoNaoEncontrado, pedidoNaoEncontrado
from resources.mensagem import pPNaoEncontrado, erroSalavarPP
from resources.mensagem import erroExcluirPP, pPExcluido
from flask_jwt_extended import jwt_required


argumentos = reqparse.RequestParser()
argumentos.add_argument('qtd_produto', type=int,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('valor_parcial',  type=float,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('cod_pedido',  type=int,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('id_produto',  type=int,
                        required=True, help="Campo obrigatório.")


class ProdutoPedido(Resource):

    def get(self, cod_nota):
        pp = ProdutoPedidoModel.find_produtoPedido(cod_nota)
        if pp:
            return pp.json()
        return pPNaoEncontrado

    @jwt_required
    def put(self, cod_nota):
        dados = argumentos.parse_args()

        pp_encontrado = ProdutoPedidoModel.find_produtoPedido(cod_nota)
        if pp_encontrado:
            if not PedidoModel.find_pedido(dados['cod_pedido']):
                return pedidoNaoEncontrado

            if not ProdutoModel.find_produto(dados['id_produto']):
                return produtoNaoEncontrado

            pp_encontrado.update_produtoPedido(**dados)
            try:
                pp_encontrado.save_produtoPedido()
            except ValueError:
                return erroSalavarPP
            return pp_encontrado.json(), 200
        return pPNaoEncontrado

    @jwt_required
    def delete(self, cod_nota):
        pp = ProdutoPedidoModel.find_produtoPedido(cod_nota)
        if pp:
            try:
                pp.delete_produtoPedido()
            except ValueError:
                return erroExcluirPP
            return pPExcluido
        return pPNaoEncontrado


class ProdutoPedidoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if not PedidoModel.find_pedido(dados['cod_pedido']):
            return pedidoNaoEncontrado

        if not ProdutoModel.find_produto(dados['id_produto']):
            return produtoNaoEncontrado

        pp = ProdutoPedidoModel(**dados)

        try:
            pp.save_produtoPedido()
        except ValueError:
            return erroSalavarPP
        return pp.json(), 200
