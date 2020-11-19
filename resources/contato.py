from flask_restful import Resource, reqparse
from models.contato_model import ContatoModel
from models.fornecedor_model import FornecedorModel
from resources.mensagem import contatoNaoEncontrado, contatoJaExiste
from resources.mensagem import erroSalvarContato, erroExcluirContato
from resources.mensagem import contatoExcluido, fornecedorNaoEncontrado
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type=str,
                        required=True, help="Campo obrigatório.")
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


class Contatos(Resource):
    def get(self):
        order = [contato.json() for contato in ContatoModel.query.all()]
        return {'contatos': order}


class Contato(Resource):

    def get(self, cod_contato):
        contato = ContatoModel.find_contato(cod_contato)
        if contato:
            return contato.json()
        return contatoNaoEncontrado

    @jwt_required
    def put(self, cod_contato):
        dados = argumentos.parse_args()

        contato_encontrado = ContatoModel.find_contato(cod_contato)
        if contato_encontrado:
            contato_encontrado.update_contato(**dados)
            contato_encontrado.save_contato()
            return contato_encontrado.json(), 200

        if ContatoModel.find_contato(dados['cod_contato']):
            return contatoJaExiste(dados['cod_contato'])

        contato = ContatoModel(cod_contato, **dados)
        try:
            contato.save_contato()
        except ValueError:
            return erroSalvarContato
        return contato.json(), 201

    @jwt_required
    def delete(self, cod_contato):
        contato = ContatoModel.find_contato(cod_contato)
        if contato:
            try:
                contato.save_contato()
            except ValueError:
                return erroExcluirContato
            return contatoExcluido
        return contatoNaoEncontrado


class ContatoCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if not FornecedorModel.find_fornecedor(dados['cod_fornecedor']):
            return fornecedorNaoEncontrado

        contato = ContatoModel(**dados)

        try:
            contato.save_contato()
        except ValueError:
            return erroSalvarContato
        return contato.json(), 200
