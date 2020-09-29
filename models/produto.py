from sql_alchemy import db


class ProdutoModel(db.Model):
    __tablename__ = 'produto'

    id_produto = db.Column(db.Integer, primary_key=True)
    cod_produto = db.Column(db.String(50), unique=True, nullable=False)
    nome_produto = db.Column(db.String(150), nullable=False)
    valor_produto = db.Column(db.Float, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

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

    @classmethod
    def find_produto(cls, cod_produto):
        produto = cls.query.filter_by(cod_produto=cod_produto).first()
        if produto:
            return produto
        return None

    def save_produto(self):
        db.session.add(self)
        db.session.commit()
