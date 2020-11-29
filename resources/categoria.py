from flask_restful import Resource, reqparse
from models.categoria_model import CategoriaModel
from models.produto_model import ProdutoModel
from resources.mensagem import categoriaEmUso, categoriaNaoEncontrada
from resources.mensagem import categoriaJaExiste, erroSalvarCategoria
from resources.mensagem import erroExcluirCategoria, categoriaExcluida
from flask_jwt_extended import jwt_required
import mysql.connector

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_categoria', type=str,
                        required=True, help="Campo obrigatório.")


class Categorias(Resource):
    def get(self):
        connection = mysql.connector.connect(user='root', password='',
                                             host='localhost', port='3307',
                                             database='reicangaco')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categoria")

        resultado = cursor.fetchall()
        categorias = []
        if resultado:
            for linha in resultado:
                categorias.append({
                    'cod_categoria': linha[0],
                    'nome_categoria': linha[1]
                })
        return {"categorias": categorias}


class Categoria(Resource):

    def get(self, cod_categoria):
        categoria = CategoriaModel.find_categoria(cod_categoria)
        if categoria:
            return categoria.json()
        return categoriaNaoEncontrada

    @jwt_required
    def put(self, cod_categoria):
        dados = argumentos.parse_args()

        if CategoriaModel.find_categoria_nome(dados['nome_categoria']):
            return categoriaJaExiste(dados['nome_categoria'])

        categoria_encontrada = CategoriaModel.find_categoria(cod_categoria)
        if categoria_encontrada:
            categoria_encontrada.update_categoria(cod_categoria, **dados)
            try:
                categoria_encontrada.save_categoria()
            except ValueError:
                return erroSalvarCategoria
            return categoria_encontrada.json(), 200
        return categoriaNaoEncontrada

    @jwt_required
    def delete(self, cod_categoria):
        categoria = CategoriaModel.find_categoria(cod_categoria)

        if ProdutoModel.find_produto_categoria(cod_categoria):
            return categoriaEmUso(cod_categoria)

        if categoria:
            try:
                categoria.delete_categoria()
            except ValueError:
                return erroExcluirCategoria
            return categoriaExcluida
        return categoriaNaoEncontrada


class CategoriaCadastro(Resource):

    @jwt_required
    def post(self):
        dados = argumentos.parse_args()
        if CategoriaModel.find_categoria_nome(dados['nome_categoria']):
            return categoriaJaExiste(dados['nome_categoria'])

        categoria = CategoriaModel(**dados)

        try:
            categoria.save_categoria()
        except ValueError:
            return erroSalvarCategoria
        return categoria.json(), 200
