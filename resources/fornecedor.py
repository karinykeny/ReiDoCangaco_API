from flask_restful import Resource, reqparse
from models.fornecedor_model import FornecedorModel
from models.produto_model import ProdutoModel
from resources.mensagem import fornecedorEmUso, erroSalvarFornecedor
from resources.mensagem import fornecedorNaoEncontrado
from resources.mensagem import erroExcluirFornecedor, fornecedorExcluido
from resources.mensagem import cnpjCpfJaExiste
from flask_jwt_extended import jwt_required

argumentos = reqparse.RequestParser()
argumentos.add_argument('cnpj_cpf', type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('nome_fantasia',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('razao_social',  type=str,
                        required=True, help="Campo obrigatório.")
argumentos.add_argument('ativo', type=str, required=True)


class Fornecedores(Resource):

    def get(self):
        order = [fornecedor.json()
                 for fornecedor in FornecedorModel.query.all()]
        return {'fornecedores': order}


class Fornecedor(Resource):

    def get(self, cod_fornecedor):
        fornecedor = FornecedorModel.find_fornecedor(cod_fornecedor)
        if fornecedor:
            return fornecedor.json()
        return fornecedorNaoEncontrado

    @jwt_required
    def put(self, cod_fornecedor):
        dados = argumentos.parse_args()
        fornecedor_encontrado = FornecedorModel.find_fornecedor(cod_fornecedor)

        if fornecedor_encontrado:
            fornecedor_encontrado.update_fornecedor(
                cod_fornecedor, **dados)
            try:
                fornecedor_encontrado.save_fornecedor()
            except ValueError:
                return erroSalvarFornecedor
            return fornecedor_encontrado.json(), 200
        return fornecedorNaoEncontrado

    @jwt_required
    def delete(self, cod_fornecedor):
        fornecedor = FornecedorModel.find_fornecedor(cod_fornecedor)

        if ProdutoModel.find_produto_fornecedor(cod_fornecedor):
            return fornecedorEmUso(cod_fornecedor)

        if fornecedor:
            try:
                fornecedor.delete_fornecedor()
            except ValueError:
                return erroExcluirFornecedor
            return fornecedorExcluido
        return fornecedorNaoEncontrado


class FornecedorCadastro(Resource):
    @jwt_required
    def post(self):
        dados = argumentos.parse_args()

        if FornecedorModel.find_fornecedor_cnpj_cpf(dados['cnpj_cpf']):
            return cnpjCpfJaExiste(dados['cnpj_cpf'])

        fornecedor = FornecedorModel(**dados)

        try:
            fornecedor.save_fornecedor()
        except ValueError:
            return erroSalvarFornecedor
        return fornecedor.json(), 200
