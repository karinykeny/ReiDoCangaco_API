from sql_alchemy import db


class PedidoModel(db.Model):
    __tablename__ = 'pedido'

    cod_pedido = db.Column(db.Integer, primary_key=True)
    valor_pedido = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    cod_vendedor = db.Column(
        db.Integer, db.ForeignKey('vendedor.cod_vendedor'))
    cod_formaPgameno = db.Column(
        db.Integer, db.ForeignKey('forma_pagamento.cod_formaPgameno'))

    def __init__(self, valor_pedido, data_pedido, status,
                 cod_vendedor, cod_formaPgameno):
        self.valor_pedido = valor_pedido
        self.data_pedido = data_pedido
        self.status = status
        self.cod_vendedor = cod_vendedor
        self.cod_formaPgameno = cod_formaPgameno

    def json(self):
        return {
            'cod_pedido': self.cod_pedido,
            'valor_pedido': self.valor_pedido,
            'data_pedido': self.data_pedido,
            'status': self.status,
            'cod_vendedor': self.cod_vendedor,
            'cod_formaPgameno': self.cod_formaPgameno
        }

    @classmethod
    def find_pedido(cls, cod_pedido):
        pedido = cls.query.filter_by(
            cod_pedido=cod_pedido).first()
        if pedido:
            return pedido
        return None

    @classmethod
    def find_pedido_vendedor(cls, cod_vendedor):
        pedido = cls.query.filter_by(
            cod_vendedor=cod_vendedor).first()
        if pedido:
            return pedido
        return None

    @classmethod
    def find_pedido_formaPgameno(cls, cod_formaPgameno):
        pedido = cls.query.filter_by(
            cod_formaPgameno=cod_formaPgameno).first()
        if pedido:
            return pedido
        return None

    def save_pedido(self):
        db.session.add(self)
        db.session.commit()

    def update_pedido(self, valor_pedido, data_pedido, status,
                      cod_vendedor, cod_formaPgameno):
        self.valor_pedido = valor_pedido
        self.data_pedido = data_pedido
        self.status = status
        self.cod_vendedor = cod_vendedor
        self.cod_formaPgameno = cod_formaPgameno

    def delete_pedido(self):
        db.session.delete(self)
        db.session.commit()
