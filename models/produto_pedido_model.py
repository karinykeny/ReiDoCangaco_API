from sql_alchemy import db


class ProdutoPedidoModel(db.Model):
    __tablename__ = 'produto_pedido'

    cod_nota = db.Column(db.Integer, primary_key=True)
    qtd_produto = db.Column(db.Integer, nullable=False)
    valor_parcial = db.Column(db.Float, nullable=False)
    cod_pedido = db.Column(
        db.Integer, db.ForeignKey('pedido.cod_pedido'))
    id_produto = db.Column(
        db.Integer, db.ForeignKey('produto.id_produto'))

    def __init__(self, qtd_produto, valor_parcial,
                 cod_pedido, id_produto):
        self.qtd_produto = qtd_produto
        self.valor_parcial = valor_parcial
        self.cod_pedido = cod_pedido
        self.id_produto = id_produto

    def json(self):
        return {
            'cod_nota': self.cod_nota,
            'qtd_produto': self.qtd_produto,
            'valor_parcial': self.valor_parcial,
            'cod_pedido': self.cod_pedido,
            'id_produto': self.id_produto
        }

    @classmethod
    def find_produtoPedido(cls, cod_nota):
        pp = cls.query.filter_by(
            cod_nota=cod_nota).first()
        if pp:
            return pp
        return None

    @classmethod
    def find_produto(cls, id_produto):
        pp = cls.query.filter_by(
            id_produto=id_produto).first()
        if pp:
            return pp
        return None

    @classmethod
    def find_pedido(cls, cod_pedido):
        pp = cls.query.filter_by(
            cod_pedido=cod_pedido).first()
        if pp:
            return pp
        return None

    def save_produtoPedido(self):
        db.session.add(self)
        db.session.commit()

    def update_produtoPedido(self, qtd_produto, valor_parcial,
                             cod_pedido, id_produto):
        self.qtd_produto = qtd_produto
        self.valor_parcial = valor_parcial
        self.cod_pedido = cod_pedido
        self.id_produto = id_produto

    def delete_produtoPedido(self):
        db.session.delete(self)
        db.session.commit()
