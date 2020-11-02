from flask_restful import Resource, reqparse
from models.contato_model import ContatoModel
from models.fornecedor_model import FornecedorModel
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('logradouro', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('numero',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('bairro',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('cidade', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('estado', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('cep', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('complemento', type=str)
argumentos.add_argument('telefone_fixo', type=str)
argumentos.add_argument('celular', type=str)
argumentos.add_argument('email', type=str)
argumentos.add_argument('cod_fornecedor', type=int,
                        required=True, help="Campo obrigatório.")


class Contato(Resource):

    def get(self, cod_contato):
        contato = ContatoModel.find_contato(cod_contato)
        if contato:
            return contato.json()
        return {'mensagem': 'Contato não encontrado.'}, 404

    @jwt_required
    def put(self, cod_contato):
        dados = argumentos.parse_args()

        contato_encontrado = ContatoModel.find_contato(cod_contato)
        if contato_encontrado:
            contato_encontrado.update_contato(**dados)
            contato_encontrado.save_contato()
            return contato_encontrado.json(), 200

        if ContatoModel.find_contato(dados['cod_contato']):
            return {'mensagem': 'Contato com código "{}" já existe.'
                    .format(dados['cod_contato'])}, 400

        contato = ContatoModel(cod_contato, **dados)
        try:
            contato.save_contato()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o fornecedor.'}, 500
        return contato.json(), 201

    @jwt_required
    def delete(self, cod_contato):
        contato = ContatoModel.find_contato(cod_contato)
        if contato:
            try:
                contato.save_contato()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o contato.'}, 500
            return {'mensagem': 'Contato excluído.'}
        return {'mensagem': 'Contato não encontrado.'}, 404


class ContatoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if not FornecedorModel.find_fornecedor(dados['cod_fornecedor']):
            return {'mensagem': 'Fornecedor com código "{}" não existe.'
                    .format(dados['cod_fornecedor'])}, 400

        contato = ContatoModel(**dados)

        try:
            contato.save_contato()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o contato.'}, 500
        return contato.json(), 200
