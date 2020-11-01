from sql_alchemy import db


class FornecedorModel(db.Model):
    __tablename__ = 'fornecedor'

    cod_fornecedor = db.Column(db.Integer, primary_key=True)
    cnpj_cpf = db.Column(db.String(18), nullable=False)
    nome_fantasia = db.Column(db.String(150), nullable=False)
    ativo = db.Column(db.String(3), nullable=False)
    produtos = db.relationship('ProdutoModel')

    def __init__(self, cod_fornecedor, cnpj_cpf, nome_fantasia, ativo):
        self.cod_fornecedor = cod_fornecedor
        self.cnpj_cpf = cnpj_cpf
        self.nome_fantasia = nome_fantasia
        self.ativo = ativo

    def json(self):
        return {
            'cod_fornecedor': self.cod_fornecedor,
            'cnpj_cpf': self.cnpj_cpf,
            'nome_fantasia': self.nome_fantasia,
            'ativo': self.ativo,
            'produtos': [produto.json() for produto in self.produtos]
        }

    @classmethod
    def find_fornecedor(cls, cod_fornecedor):
        fornecedor = cls.query.filter_by(cod_fornecedor=cod_fornecedor).first()
        if fornecedor:
            return fornecedor
        return None

    def save_fornecedor(self):
        db.session.add(self)
        db.session.commit()

    def update_fornecedor(self, cnpj_cpf, nome_fantasia, ativo):
        self.cnpj_cpf = cnpj_cpf
        self.nome_fantasia = nome_fantasia
        self.ativo = ativo

    def delete_fornecedor(self):
        db.session.delete(self)
        db.session.commit()
