from flask_restful import Resource, reqparse
from models.produto_model import ProdutoModel
from models.fornecedor_model import FornecedorModel
from models.categoria_model import CategoriaModel
from models.produto_pedido_model import ProdutoPedidoModel
from resources.mensagem import produtoJaExiste, produtoNaoEncontrado
from resources.mensagem import erroSalvarProduto, erroExcluirProduto
from resources.mensagem import produtoExcluido, categoriaNaoEncontrada
from resources.mensagem import fornecedorNaoEncontrado
from flask_jwt_extended import jwt_required
from resources.mensagem import produtoEmUso


class Produtos(Resource):

    def get(self):
        order = [produto.json()
                 for produto in ProdutoModel.query.all()]
        return {'produtos': order}


class Produto(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cod_produto', type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('nome_produto',  type=str,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('valor_produto', type=float,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('cod_categoria', type=int,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('cod_fornecedor', type=int,
                            required=True, help="Campo obrigatório.")
    argumentos.add_argument('ativo', type=str, required=True)

    def get(self, id_produto):
        produto = Produto.find_produto(id_produto)
        if produto:
            return produto.json()
        return produtoNaoEncontrado

    @jwt_required
    def put(self, id_produto):
        dados = Produto.argumentos.parse_args()

        if not CategoriaModel.find_categoria(dados['cod_categoria']):
            return categoriaNaoEncontrada

        if not FornecedorModel.find_fornecedor(dados['cod_fornecedor']):
            return fornecedorNaoEncontrado

        produto_encontrado = ProdutoModel.find_produto(id_produto)
        if produto_encontrado:
            if produto_encontrado.getCodProduto() != dados['cod_produto']:
                if ProdutoModel.find_produto_by_cod(dados['cod_produto']):
                    return produtoJaExiste(dados['cod_produto'])
            produto_encontrado.update_produto(id_produto, **dados)
            try:
                produto_encontrado.save_produto()
            except ValueError:
                return erroSalvarProduto
            return produto_encontrado.json(), 200
        return produtoNaoEncontrado

    @jwt_required
    def delete(self, id_produto):
        if ProdutoPedidoModel.find_produto(id_produto):
            return produtoEmUso(id_produto)

        produto = ProdutoModel.find_produto(id_produto)
        if produto:
            try:
                produto.delete_produto()
            except ValueError:
                return erroExcluirProduto
            return produtoExcluido
        return produtoNaoEncontrado


class ProdutoCadastro(Resource):

    @jwt_required
    def post(self):
        dados = Produto.argumentos.parse_args()

        if ProdutoModel.find_produto_by_cod(dados['cod_produto']):
            return produtoJaExiste(dados['cod_produto'])

        if not CategoriaModel.find_categoria(dados['cod_categoria']):
            return categoriaNaoEncontrada

        if not FornecedorModel.find_fornecedor(dados['cod_fornecedor']):
            return fornecedorNaoEncontrado

        produto = ProdutoModel(**dados)

        try:
            produto.save_produto()
        except ValueError:
            return erroSalvarProduto
        return produto.json(), 200
