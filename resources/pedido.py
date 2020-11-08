from flask_restful import Resource, reqparse
from models.pedido_model import PedidoModel
from models.vendedor_model import VendedorModel
from models.produto_pedido_model import ProdutoPedidoModel
from models.forma_pagemento_model import FormaPagamentoModel
from resources.mensagem import pedidoEmUso, pedidoNaoEncontrado
from resources.mensagem import vendedorNaoEncontrado, FPNaoEncontrada
from resources.mensagem import erroSalvarPedido, erroExcluirPedido
from resources.mensagem import pedidoExcluido
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('valor_pedido', type=float,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('data_pedido',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('status',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('cod_vendedor',  type=int,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('cod_formaPgameno',  type=int,
                        required=True, help="Campo obrigatório.")


class Pedidos(Resource):

    def get(self):
        order = [pedido.json()
                 for pedido in PedidoModel.query.all()]
        return {'pedidos': order}


class Pedido(Resource):

    def get(self, cod_pedido):
        pedido = PedidoModel.find_pedido(cod_pedido)
        if pedido:
            return pedido.json()
        return pedidoNaoEncontrado

    @jwt_required
    def put(self, cod_pedido):
        dados = argumentos.parse_args()

        if not VendedorModel.find_vendedor(dados['cod_vendedor']):
            return vendedorNaoEncontrado

        if not FormaPagamentoModel.find_formaPagamento(
                dados['cod_formaPgameno']):
            return FPNaoEncontrada

        pedido_encontrado = PedidoModel.find_pedido(cod_pedido)
        if pedido_encontrado:
            pedido_encontrado.update_pedido(**dados)
            try:
                pedido_encontrado.save_pedido()
            except ValueError:
                return erroSalvarPedido
            return pedido_encontrado.json(), 200
        return pedidoNaoEncontrado

    @jwt_required
    def delete(self, cod_pedido):
        if ProdutoPedidoModel.find_pedido(cod_pedido):
            return pedidoEmUso(cod_pedido)

        pedido = PedidoModel.find_pedido(cod_pedido)
        if pedido:
            try:
                pedido.delete_pedido()
            except ValueError:
                return erroExcluirPedido
            return pedidoExcluido
        return pedidoNaoEncontrado


class PedidoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if not VendedorModel.find_vendedor(dados['cod_vendedor']):
            return vendedorNaoEncontrado

        if not FormaPagamentoModel.find_formaPagamento(
                dados['cod_formaPgameno']):
            return FPNaoEncontrada

        pedido = PedidoModel(**dados)

        try:
            pedido.save_pedido()
        except ValueError:
            return erroSalvarPedido
        return pedido.json(), 200
