from sql_alchemy import db


class VendedorModel(db.Model):
    __tablename__ = 'vendedor'

    cod_vendedor = db.Column(db.Integer, primary_key=True)
    nome_vendedor = db.Column(db.String(150))
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def __init__(self, nome_vendedor, login, senha, ativo):
        self.nome_vendedor = nome_vendedor
        self.login = login
        self.senha = senha
        self.ativo = ativo

    def json(self):
        return {
            'cod_vendedor': self.cod_vendedor,
            'nome_vendedor': self.nome_vendedor,
            'login':  self.login,
            'ativo': self.ativo
        }

    def jsonPut(self):
        return {
            'cod_vendedor': self.cod_vendedor,
            'nome_vendedor': self.nome_vendedor,
            'login':  self.login,
            'senha': self.senha,
            'ativo': self.ativo
        }

    @classmethod
    def find_vendedor(cls, cod_vendedor):
        vendedor = cls.query.filter_by(cod_vendedor=cod_vendedor).first()
        if vendedor:
            return vendedor
        return None

    @classmethod
    def find_by_login(cls, login):
        vendedor = cls.query.filter_by(login=login).first()
        if vendedor:
            return vendedor
        return None

    def save_vendedor(self):
        db.session.add(self)
        db.session.commit()

    def update_vendedor(self, cod_vendedor, nome_vendedor, login,
                        senha, ativo):
        self.cod_vendedor = cod_vendedor
        self.nome_vendedor = nome_vendedor
        self.login = login
        self.senha = senha
        self.ativo = ativo

    def delete_vendedor(self):
        db.session.delete(self)
        db.session.commit()
