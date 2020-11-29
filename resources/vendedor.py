from flask_restful import Resource, reqparse
from models.vendedor_model import VendedorModel
from models.pedido_model import PedidoModel
from resources.mensagem import vendedorEmUso, vendedorNaoEncontrado
from resources.mensagem import erroExcluirVendedor, vendedorExcluido
from resources.mensagem import loginExiste, vendedorCriado, loginInvalido
from resources.mensagem import logout, erroSalvarVendedor
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import blacklist


argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_vendedor')
argumentos.add_argument('senha', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('login', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('ativo', type=bool)


class Vendedores(Resource):
    def get(self):
        order = [vendedor.json() for vendedor in VendedorModel.query.all()]
        return {'vendedores': order}


class Vendedor(Resource):

    def get(self, cod_vendedor):
        vendedor = VendedorModel.find_vendedor(cod_vendedor)
        if vendedor:
            return vendedor.json()
        return vendedorNaoEncontrado

    def put(self, cod_vendedor):
        dados = argumentos.parse_args()
        vendedor_encontrado = VendedorModel.find_vendedor(cod_vendedor)

        if vendedor_encontrado:
            vendedor_encontrado.update_vendedor(
                cod_vendedor, **dados)
            try:
                vendedor_encontrado.save_vendedor()
            except ValueError:
                return erroSalvarVendedor
            return vendedor_encontrado.jsonPut(), 200
        return vendedorNaoEncontrado

    @jwt_required
    def delete(self, cod_vendedor):
        if PedidoModel.find_pedido_vendedor(cod_vendedor):
            return vendedorEmUso(cod_vendedor)

        vendedor = VendedorModel.find_vendedor(cod_vendedor)
        if vendedor:
            try:
                vendedor.delete_vendedor()
            except ValueError:
                return erroExcluirVendedor
            return vendedorExcluido
        return vendedorNaoEncontrado


class VendedorRegistro(Resource):

    def post(self):
        dados = argumentos.parse_args()
        if VendedorModel.find_by_login(dados['login']):
            return loginExiste(dados['login'])

        vendedor = VendedorModel(**dados)
        vendedor.ativo = True
        vendedor.save_vendedor()
        return vendedor.json()


class VendedorLogin(Resource):

    @classmethod
    def post(cls):
        dados = argumentos.parse_args()
        vendedor = VendedorModel.find_by_login(dados['login'])

        if vendedor and safe_str_cmp(vendedor.senha, dados['senha']):
            if vendedor.ativo:
                token_de_acesso = create_access_token(
                    identity=vendedor.cod_vendedor)
                return {
                    'access_token': token_de_acesso,
                    'vendedor': vendedor.nome_vendedor,
                    'cod_vendedor': vendedor.cod_vendedor}, 200
            return {'message': 'Usuário não confirmado.'}, 400
        return loginInvalido


class VendedorLogout(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return logout
