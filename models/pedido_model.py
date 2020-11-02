from sql_alchemy import db


class PedidoModel(db.Model):
    cod_pedido = db.Column(db.Integer, primary_key=True)
    valor_pedido = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, valor_pedido, data_pedido, status):
        self.valor_pedido = valor_pedido
        self.data_pedido = data_pedido
        self.status = status

    def json(self):
        return {
            'cod_pedido': self.cod_pedido,
            'valor_pedido': self.valor_pedido,
            'data_pedido': self.data_pedido,
            'status': self.status
        }

    @classmethod
    def find_pedido(cls, cod_pedido):
        pedido = cls.query.filter_by(
            cod_pedido=cod_pedido).first()
        if pedido:
            return pedido
        return None

    def save_pedido(self):
        db.session.add(self)
        db.session.commit()

    def update_pedido(self, valor_pedido, data_pedido, status):
        self.valor_pedido = valor_pedido
        self.data_pedido = data_pedido
        self.status = status

    def delete_pedido(self):
        db.session.delete(self)
        db.session.commit()
