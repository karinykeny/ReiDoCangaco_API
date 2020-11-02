from sql_alchemy import db


class ProdutoPedidoModel(db.Model):
    cod_nota = db.Column(db.Integer, primary_key=True)
    qtd_produto = db.Column(db.Integer, nullable=False)
    valor_parcial = db.Column(db.Float, nullable=False)

    def __init__(self, qtd_produto, valor_parcial):
        self.qtd_produto = qtd_produto
        self.valor_parcial = valor_parcial

    def json(self):
        return {
            'cod_nota': self.cod_nota,
            'qtd_produto': self.qtd_produto,
            'valor_parcial': self.valor_parcial
        }

    @classmethod
    def find_produtoPedido(cls, cod_nota):
        pp = cls.query.filter_by(
            cod_nota=cod_nota).first()
        if pp:
            return pp
        return None

    def save_produtoPedido(self):
        db.session.add(self)
        db.session.commit()

    def update_produtoPedido(self, qtd_produto, valor_parcial):
        self.qtd_produto = qtd_produto
        self.valor_parcial = valor_parcial

    def delete_produtoPedido(self):
        db.session.delete(self)
        db.session.commit()
