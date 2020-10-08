from flask_restful import Resource, reqparse
from models.vendedor_model import VendedorModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import blacklist

atributos = reqparse.RequestParser()
atributos.add_argument('nome_vendedor')
atributos.add_argument('senha', type=str,
                       required=True, help="Campo obrigatório.")
atributos.add_argument('login', type=str,
                       required=True, help="Campo obrigatório.")
atributos.add_argument('ativo')


class Vendedores(Resource):
    def get(self):
        order = [vendedor.json() for vendedor in VendedorModel.query.all()]
        return {'vendedor': order}


class Vendedor(Resource):

    def get(self, cod_vendedor):
        vendedor = VendedorModel.find_vendedor(cod_vendedor)
        if vendedor:
            return vendedor.json()
        return {'mensagem': 'Vendedor não encontrado.'}, 404

    @jwt_required
    def delete(self, cod_vendedor):
        vendedor = VendedorModel.find_vendedor(cod_vendedor)
        if vendedor:
            try:
                vendedor.delete_vendedor()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o vendedor.'}, 500
            return {'mensagem': 'Vendedor excluído.'}
        return {'mensagem': 'Vendedor não encontrado.'}, 404


class VendedorRegistro(Resource):

    def post(self):
        dados = atributos.parse_args()
        if VendedorModel.find_by_login(dados['login']):
            return {'mensagem': 'Login "{}" já existe.'
                    .format(dados['login'])}, 400

        vendedor = VendedorModel(**dados)
        vendedor.save_vendedor()
        return {'mensagem': 'Vendedor criado com sucesso!'}, 201


class VendedorLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        vendedor = VendedorModel.find_by_login(dados['login'])

        if vendedor and safe_str_cmp(vendedor.senha, dados['senha']):
            token_de_acesso = create_access_token(
                identity=vendedor.cod_vendedor)
            return {'access_token': token_de_acesso}, 200
        return {'mensagem': 'login ou senha inválidos!'}, 401


class VendedorLogout(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return {'mensagem': 'Logout com sucesso!'}, 200
