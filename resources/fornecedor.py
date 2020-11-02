from flask_restful import Resource, reqparse
from models.fornecedor_model import FornecedorModel
from flask_jwt_extended import jwt_required


class Fornecedores(Resource):

    def get(self):
        order = [fornecedor.json()
                 for fornecedor in FornecedorModel.query.all()]
        return {'fornecedores': order}


class Fornecedor(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cnpj_cpf', type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('nome_fantasia',  type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('razao_social',  type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('ativo', type=str, required=True)

    def get(self, cod_fornecedor):
        fornecedor = FornecedorModel.find_produto(cod_fornecedor)
        if fornecedor:
            return fornecedor.json()
        return {'mensagem': 'Produto não encontrado.'}, 404

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
                fornecedor.delete_fornecedor()
            except ValueError:
                return {'mensagem': 'Erro ao excluir o fornecedor.'}, 500
            return {'mensagem': 'Fornecedor excluído.'}
        return {'mensagem': 'Fornecedor não encontrado.'}, 404


class FornecedorCadastro(Resource):
    @jwt_required
    def post(self):
        dados = Fornecedor.argumentos.parse_args()

        if FornecedorModel.find_fornecedor_cnpj_cpf(dados['cnpj_cpf']):
            return {'mensagem': 'CNPJ/CPF "{}" já existe.'
                    .format(dados['cnpj_cpf'])}, 400

        fornecedor = FornecedorModel(**dados)

        try:
            fornecedor.save_fornecedor()
        except ValueError:
            return {'mensagem': 'Erro ao salvar o fornecedor.'}, 500
        return fornecedor.json(), 200
