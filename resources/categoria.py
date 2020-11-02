from flask_restful import Resource, reqparse
from models.categoria_model import CategoriaModel
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_categoria', type=str,
                        required=True, help="Campo obrigatório.")


class Categorias(Resource):
    def get(self):
        order = [categoria.json() for categoria in CategoriaModel.query.all()]
        return {'categorias': order}


class Categoria(Resource):

    def get(self, cod_categoria):
        categoria = CategoriaModel.find_categoria(cod_categoria)
        if categoria:
            return categoria.json()
        return {'mensagem': 'Categoria não encontrado.'}, 404

    @jwt_required
    def put(self, cod_categoria):
        dados = argumentos.parse_args()

        categoria_encontrada = CategoriaModel.find_categoria(cod_categoria)
        if categoria_encontrada:
            categoria_encontrada.update_categoria(**dados)
            categoria_encontrada.save_categoria()
            return categoria_encontrada.json(), 200

        if CategoriaModel.find_categoria(dados['cod_categoria']):
            return {'mensagem': 'Categoria com código "{}" já existe.'
                    .format(dados['cod_categoria'])}, 400

        categoria = CategoriaModel(cod_categoria, **dados)
        try:
            categoria.save_categoria()
        except ValueError:
            return {'mensagem': 'Erro ao salvar a categora.'}, 500
        return categoria.json(), 201

    @jwt_required
    def delete(self, cod_categoria):
        categoria = CategoriaModel.find_categoria(cod_categoria)
        if categoria:
            try:
                categoria.delete_categoria()
            except ValueError:
                return {'mensagem': 'Erro ao excluir a categoria.'}, 500
            return {'mensagem': 'Categoria excluída.'}
        return {'mensagem': 'Categoria não encontrada.'}, 404


class CategoriaCadastro(Resource):

    @jwt_required
    def post(self):
        dados = argumentos.parse_args()
        if CategoriaModel.find_categoria_nome(dados['nome_categoria']):
            return {'mensagem': 'Categoria "{}" já existe.'
                    .format(dados['nome_categoria'])}, 400

        categoria = CategoriaModel(**dados)

        try:
            categoria.save_categoria()
        except ValueError:
            return {'mensagem': 'Erro ao salvar a categoria.'}, 500
        return categoria.json(), 200
