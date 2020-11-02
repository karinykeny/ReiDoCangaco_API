from flask_restful import Resource, reqparse
from models.pedido_model import PedidoModel
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('valor_pedido', type=float,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('data_pedido',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('status',  type=str,
                        required=True, help="Campo obrigatório.")


class Pedidos(Resource):

    def get(self):
        order = [pedido.json()
                 for pedido in PedidoModel.query.all()]
        return {'fornecedores': order}


class Pedido(Resource):

    def get(self, cod_pedido):
        pedido = PedidoModel.find_pedido(cod_pedido)
        if pedido:
            return pedido.json()
        return {'mensagem': 'Pedido não encontrado.'}, 404

    @jwt_required
    def put(self, cod_pedido):
        dados = argumentos.parse_args()

        pedido_encontrado = PedidoModel.find_pedido(cod_pedido)
        if pedido_encontrado:
            pedido_encontrado.update_pedido(**dados)
            pedido_encontrado.save_pedido()
            return pedido_encontrado.json(), 200

        if PedidoModel.find_pedido(dados['cod_pedido']):
            return {'mensagem': 'Pedido com código "{}" já existe.'
                    .format(dados['cod_pedido'])}, 400

        pedido = PedidoModel(cod_pedido, **dados)
        try:
            pedido.save_pedido()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o pedido.'}, 500
        return pedido.json(), 201

    @jwt_required
    def delete(self, cod_pedido):
        pedido = PedidoModel.find_pedido(cod_pedido)
        if pedido:
            try:
                pedido.delete_pedido()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o pedido.'}, 500
            return {'mensagem': 'Pedido excluído.'}
        return {'mensagem': 'Fornecedor não encontrado.'}, 404


class PedidoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        pedido = PedidoModel(**dados)

        try:
            pedido.save_pedido()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o pedido.'}, 500
        return pedido.json(), 200
