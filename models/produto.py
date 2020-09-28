class ProdutoModel:
    def __init__(self, id_produto, cod_produto, nome_produto,
                 valor_produto, ativo):
        self.id_produto = id_produto
        self.cod_produto = cod_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.ativo = ativo

    def json(self):
        return {
            'id_produto': self.id_produto,
            'cod_produto': self.cod_produto,
            'nome_produto':  self.nome_produto,
            'valor_produto': self.valor_produto,
            'ativo': self.ativo
        }
