from sql_alchemy import db


class FornecedorModel(db.Model):
    __tablename__ = 'fornecedor'

    cod_fornecedor = db.Column(db.Integer, primary_key=True)
    cnpj_cpf = db.Column(db.String(18), unique=True, nullable=False)
    nome_fantasia = db.Column(db.String(150), nullable=False)
    razao_social = db.Column(db.String(150), nullable=False)
    ativo = db.Column(db.String(3), nullable=False)
    contato = db.relationship("ContatoModel")

    def __init__(self, cnpj_cpf, nome_fantasia, razao_social, ativo):
        self.cnpj_cpf = cnpj_cpf
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.ativo = ativo

    def json(self):
        return {
            'cod_fornecedor': self.cod_fornecedor,
            'cnpj_cpf': self.cnpj_cpf,
            'nome_fantasia': self.nome_fantasia,
            'razao_social': self.razao_social,
            'ativo': self.ativo,
            'contatos': [contato.json() for contato in self.contato]
        }

    @classmethod
    def find_fornecedor(cls, cod_fornecedor):
        fornecedor = cls.query.filter_by(cod_fornecedor=cod_fornecedor).first()
        if fornecedor:
            return fornecedor
        return None

    @classmethod
    def find_fornecedor_cnpj_cpf(cls, cnpj_cpf):
        fornecedor = cls.query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if fornecedor:
            return fornecedor
        return None

    def save_fornecedor(self):
        db.session.add(self)
        db.session.commit()

    def update_fornecedor(self, cod_fornecedor, cnpj_cpf, nome_fantasia,
                          razao_social, ativo):
        self.cod_fornecedor = cod_fornecedor
        self.cnpj_cpf = cnpj_cpf
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.ativo = ativo

    def delete_fornecedor(self):
        [contato.delete_contato() for contato in self.contato]
        db.session.delete(self)
        db.session.commit()
