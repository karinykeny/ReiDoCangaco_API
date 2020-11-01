from flask_restful import Resource, reqparse
from models.fornecedor_model import FornecedorModel
from resources.filtros import normalize_path_params_fornecedor
from resources.filtros import consulta_fornecedor
from flask_jwt_extended import jwt_required
import sqlite3

path_params = reqparse.RequestParser()
path_params.add_argument('cnpj_cpf', type=str)
path_params.add_argument('nome_fantasia', type=float)
path_params.add_argument('ativo', type=str)


class Fornecedores(Resource):

    def get(self):
        connection = sqlite3.connect('reicangaco.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {chave: dados[chave]
                         for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params_fornecedor(**dados_validos)
        tupla = tuple([parametros[chave] for chave in parametros])
        consulta = consulta_fornecedor

        if parametros.get('cnpj_cpf'):
            consulta = consulta + "AND cnpj_cpf = ?"
        if parametros.get('nome_produto'):
            consulta = consulta + "AND nome_produto = ?"

        resultado = cursor.execute(consulta, tupla)
        fornecedores = []
        for linha in resultado:
            fornecedores.append({
                'cod_fornecedor': linha[0],
                'cnpj_cpf': linha[1],
                'nome_fantasia': linha[2],
                'ativo': linha[3]
            })

        return {'fornecedores': fornecedores}


class Fornecedor(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cnpj_cpf', type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('nome_fantasia',  type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('ativo', type=str, required=True)

    def get(self, cod_fornecedor):
        fornecedor = FornecedorModel.find_produto(cod_fornecedor)
        if fornecedor:
            return fornecedor.json()
        return {'mensagem': 'Produto não encontrado.'}, 404

    @jwt_required
    def post(self, cod_fornecedor):
        dados = Fornecedor.argumentos.parse_args()

        if FornecedorModel.find_fornecedor(dados['cod_fornecedor']):
            return {'mensagem': 'Fornecedor com código "{}" já existe.'
                    .format(dados['cod_produto'])}, 400

        fornecedor = FornecedorModel(cod_fornecedor, **dados)

        try:
            fornecedor.save_fornecedor()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o fornecedor.'}, 500
        return fornecedor.json(), 200

    @jwt_required
    def put(self, cod_fornecedor):
        dados = Fornecedor.argumentos.parse_args()

        fornecedor_encontrado = FornecedorModel.find_fornecedor(cod_fornecedor)
        if fornecedor_encontrado:
            fornecedor_encontrado.update_fornecedor(**dados)
            fornecedor_encontrado.save_fornecedor()
            return fornecedor_encontrado.json(), 200

        if FornecedorModel.find_fornecedor(dados['cod_fornecedor']):
            return {'mensagem': 'Fornecedor com código "{}" já existe.'
                    .format(dados['cod_fornecedor'])}, 400

        fornecedor = FornecedorModel(cod_fornecedor, **dados)
        try:
            fornecedor.save_fornecedor()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o fornecedor.'}, 500
        return fornecedor.json(), 201

    @jwt_required
    def delete(self, cod_fornecedor):
        fornecedor = FornecedorModel.find_fornecedor(cod_fornecedor)
        if fornecedor:
            try:
                fornecedor.save_fornecedor()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o fornecedor.'}, 500
            return {'mensagem': 'Fornecedor excluído.'}
        return {'mensagem': 'Fornecedor não encontrado.'}, 404
