from flask_restful import Resource, reqparse
from models.produto import ProdutoModel

produtos = [
    {
        'id_produto': 1,
        'cod_produto': '0001',
        'nome_produto': 'produto1',
        'valor_produo': 10.5,
        'ativo': True
    },
    {
        'id_produto': 2,
        'cod_produto': '0002',
        'nome_produto': 'produto2',
        'valor_produo': 11.5,
        'ativo': True
    },
    {
        'id_produto': 3,
        'cod_produto': '0003',
        'nome_produto': 'produto3',
        'valor_produto': 11.5,
        'ativo': True
    }
]


class Produtos(Resource):
    def get(self):
        return {'produtos': produtos}


class Produto(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cod_produto')
    argumentos.add_argument('nome_produto')
    argumentos.add_argument('valor_produto')
    argumentos.add_argument('ativo')

    def find_produto(id_produto):
        for produto in produtos:
            if produto['id_produto'] == id_produto:
                return produto
        return None

    def get(self, id_produto):
        produto = Produto.find_produto(id_produto)
        if produto:
            return produto
        return {'mensagem': 'Produto não encontrado.'}, 404

    def post(self, id_produto):
        dados = Produto.argumentos.parse_args()
        produto_obj = ProdutoModel(id_produto, **dados)
        novo_produto = produto_obj.json()

        produtos.append(novo_produto)
        return novo_produto, 200

    def put(self, id_produto):
        dados = Produto.argumentos.parse_args()
        produto_obj = ProdutoModel(id_produto, **dados)
        novo_produto = produto_obj.json()

        produto = Produto.find_produto(id_produto)
        if produto:
            produto.update(dados)
            return novo_produto, 200

        produtos.append(novo_produto)
        return novo_produto, 201

    def delete(self, id_produto):
        global produtos
        produtos = [p for p in produtos if p['id_produto'] != id_produto]
        return {'mensagem': 'Produto deletado.'}
