from sql_alchemy import db


class FormaPagamentoModel(db.Model):
    __tablename__ = 'forma_pagamento'

    cod_formaPgameno = db.Column(db.Integer, primary_key=True)
    tipo_formaPagamento = db.Column(db.String(50), nullable=False)
    descricao_formaPagamento = db.Column(db.String(50), nullable=False)

    def __init__(self, tipo_formaPagamento,
                 descricao_formaPagamento):
        self.tipo_formaPagamento = tipo_formaPagamento
        self.descricao_formaPagamento = descricao_formaPagamento

    def getTipoFormaPagamento(self):
        return self.tipo_formaPagamento

    def json(self):
        return {
            'cod_formaPgameno': self.cod_formaPgameno,
            'tipo_formaPagamento': self.tipo_formaPagamento,
            'descricao_formaPagamento': self.descricao_formaPagamento
        }

    @classmethod
    def find_formaPagamento(cls, cod_formaPgameno):
        formaPgameno = cls.query.filter_by(
            cod_formaPgameno=cod_formaPgameno).first()
        if formaPgameno:
            return formaPgameno
        return None

    @classmethod
    def find_formaPagamento_tipo(cls, tipo_formaPagamento):
        formaPgameno = cls.query.filter_by(
            tipo_formaPagamento=tipo_formaPagamento).first()
        if formaPgameno:
            return tipo_formaPagamento
        return None

    def save_formaPagamento(self):
        db.session.add(self)
        db.session.commit()

    def update_formaPagamento(self, cod_formaPgameno, tipo_formaPagamento,
                              descricao_formaPagamento):
        self.tipo_formaPagamento = tipo_formaPagamento
        self.descricao_formaPagamento = descricao_formaPagamento

    def delete_formaPagamento(self):
        db.session.delete(self)
        db.session.commit()
