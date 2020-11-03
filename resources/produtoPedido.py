from flask_restful import Resource, reqparse
from models.produto_pedido_model import ProdutoPedidoModel
from models.pedido_model import PedidoModel
from models.produto_model import ProdutoModel
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
        return {'mensagem': 'Produto/Pedido não encontrado.'}, 404

    @jwt_required
    def put(self, cod_nota):
        dados = argumentos.parse_args()

        pp_encontrado = ProdutoPedidoModel.find_produtoPedido(cod_nota)
        if pp_encontrado:
            pp_encontrado.update_produtoPedido(**dados)
            pp_encontrado.save_produtoPedido()
            return pp_encontrado.json(), 200

        if ProdutoPedidoModel.find_produtoPedido(dados['cod_nota']):
            return {'mensagem': 'Produto/Pedido com código "{}" já existe.'
                    .format(dados['cod_nota'])}, 400

        pp = ProdutoPedidoModel(cod_nota, **dados)
        try:
            pp.save_produtoPedido()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o Produto/Pedido.'}, 500
        return pp.json(), 201

    @jwt_required
    def delete(self, cod_nota):
        pp = ProdutoPedidoModel.find_produtoPedido(cod_nota)
        if pp:
            try:
                pp.delete_produtoPedido()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o Produto/Pedido.'}, 500
            return {'mensagem': 'Produto/Pedido excluído.'}
        return {'mensagem': 'Produto/Pedido não encontrado.'}, 404


class ProdutoPedidoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if not PedidoModel.find_pedido(dados['cod_pedido']):
            return {'mensagem': 'Pedido com código "{}" não existe.'
                    .format(dados['cod_pedido'])}, 400

        if not ProdutoModel.find_produto(dados['id_produto']):
            return {'mensagem': 'Produto com id "{}" não existe.'
                    .format(dados['id_produto'])}, 400

        pp = ProdutoPedidoModel(**dados)

        try:
            pp.save_produtoPedido()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o fornecedor.'}, 500
        return pp.json(), 200
