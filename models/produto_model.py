from sql_alchemy import db


class ProdutoModel(db.Model):
    __tablename__ = 'produto'

    id_produto = db.Column(db.Integer, primary_key=True)
    cod_produto = db.Column(db.String(50), nullable=False)
    nome_produto = db.Column(db.String(150), nullable=False)
    valor_produto = db.Column(db.Float(precision=2), nullable=False)
    ativo = db.Column(db.String(3), nullable=False)
    cod_categoria = db.Column(db.Integer, db.ForeignKey(
        'categoria_model.cod_categoria'))
    cod_fornecedor = db.Column(db.Integer, db.ForeignKey(
        'fornecedor_model.cod_fornecedor'))

    def __init__(self, id_produto, cod_produto, nome_produto,
                 valor_produto, ativo, cod_categoria, cod_fornecedor):
        self.id_produto = id_produto
        self.cod_produto = cod_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.ativo = ativo
        self.cod_categoria = cod_categoria
        self.cod_fornecedor = cod_fornecedor

    def json(self):
        return {
            'id_produto': self.id_produto,
            'cod_produto': self.cod_produto,
            'nome_produto':  self.nome_produto,
            'valor_produto': self.valor_produto,
            'ativo': self.ativo,
            'cod_categoria': self.cod_categoria,
            'cod_fornecedor': self.cod_fornecedor
        }

    @classmethod
    def find_produto_by_cod(cls, cod_produto):
        produto = cls.query.filter_by(cod_produto=cod_produto).first()
        if produto:
            return produto
        return None

    @classmethod
    def find_produto(cls, id_produto):
        produto = cls.query.filter_by(id_produto=id_produto).first()
        if produto:
            return produto
        return None

    def save_produto(self):
        db.session.add(self)
        db.session.commit()

    def update_produto(self, cod_produto, nome_produto, valor_produto, ativo):
        self.cod_produto = cod_produto
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.ativo = ativo

    def delete_produto(self):
        db.session.delete(self)
        db.session.commit()
