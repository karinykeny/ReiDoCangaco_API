from flask_restful import Resource, reqparse
from models.produto_model import ProdutoModel
from resources.filtros import normalize_path_params_produto
from resources.filtros import consulta_sem_nome_produto
from resources.filtros import consulta_com_nome_produto
from flask_jwt_extended import jwt_required
import sqlite3

path_params = reqparse.RequestParser()
path_params.add_argument('nome_produto', type=str)
path_params.add_argument('valor_max', type=float)
path_params.add_argument('valor_min', type=float)
path_params.add_argument('ativo', type=str)


class Produtos(Resource):

    def get(self):
        connection = sqlite3.connect('reicangaco.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {chave: dados[chave]
                         for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params_produto(**dados_validos)

        if not parametros.get('nome_produto'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_nome_produto, tupla)

        else:
            params = [parametros[chave] for chave in parametros]
            resultado = cursor.execute(consulta_com_nome_produto, (
                '%' + params[0] + '%', params[1], params[2], params[3]))

        produtos = []
        for linha in resultado:
            produtos.append({
                'id_produto': linha[0],
                'cod_produto': linha[1],
                'nome_produto':  linha[2],
                'valor_produto': linha[3],
                'ativo': linha[4]
            })

        return {'produtos': produtos}


class Produto(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cod_produto', type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('nome_produto',  type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('valor_produto', type=float,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('ativo', type=str, required=True)

    def get(self, id_produto):
        produto = ProdutoModel.find_produto(id_produto)
        if produto:
            return produto.json()
        return {'mensagem': 'Produto não encontrado.'}, 404

    @jwt_required
    def post(self, id_produto):
        dados = Produto.argumentos.parse_args()

        if ProdutoModel.find_produto_by_cod(dados['cod_produto']):
            return {'mensagem': 'Produto com código "{}" já existe.'
                    .format(dados['cod_produto'])}, 400

        produto = ProdutoModel(id_produto, **dados)

        try:
            produto.save_produto()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o produto.'}, 500
        return produto.json(), 200

    @jwt_required
    def put(self, id_produto):
        dados = Produto.argumentos.parse_args()

        produto_encontrado = ProdutoModel.find_produto(id_produto)
        if produto_encontrado:
            produto_encontrado.update_produto(**dados)
            produto_encontrado.save_produto()
            return produto_encontrado.json(), 200

        if ProdutoModel.find_produto_by_cod(dados['cod_produto']):
            return {'mensagem': 'Produto com código "{}" já existe.'
                    .format(dados['cod_produto'])}, 400

        produto = ProdutoModel(id_produto, **dados)
        try:
            produto.save_produto()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o produto.'}, 500
        return produto.json(), 201

    @jwt_required
    def delete(self, id_produto):
        produto = ProdutoModel.find_produto(id_produto)
        if produto:
            try:
                produto.delete_produto()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o produto.'}, 500
            return {'mensagem': 'Produto excluído.'}
        return {'mensagem': 'Produto não encontrado.'}, 404
