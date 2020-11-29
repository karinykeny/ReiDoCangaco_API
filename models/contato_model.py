from sql_alchemy import db


class ContatoModel(db.Model):
    __tablename__ = 'contato'

    cod_contato = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    logradouro = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    complemento = db.Column(db.String(150))
    telefone_fixo = db.Column(db.String(10))
    celular = db.Column(db.String(11))
    email = db.Column(db.String(150))
    cod_fornecedor = db.Column(
        db.Integer, db.ForeignKey('fornecedor.cod_fornecedor'))

    def __init__(self, nome, logradouro, numero, bairro, cidade,
                 estado, cep, complemento, telefone_fixo, celular, email,
                 cod_fornecedor):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento
        self.telefone_fixo = telefone_fixo
        self.celular = celular
        self.email = email
        self.cod_fornecedor = cod_fornecedor

    def json(self):
        return {
            'cod_contato': self.cod_contato,
            'nome': self.nome,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
            'cep': self.cep,
            'complemento': self.complemento,
            'telefone_fixo': self.telefone_fixo,
            'celular': self.celular,
            'email': self.email,
            'cod_fornecedor': self.cod_fornecedor
        }

    @classmethod
    def find_contato(cls, cod_contato):
        fornecedor = cls.query.filter_by(cod_contato=cod_contato).first()
        if fornecedor:
            return fornecedor
        return None

    def save_contato(self):
        db.session.add(self)
        db.session.commit()

    def update_contato(self, nome, logradouro, numero, bairro, cidade, estado,
                       cep, complemento, telefone_fixo, celular, email,
                       cod_fornecedor):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento
        self.telefone_fixo = telefone_fixo
        self.celular = celular
        self.email = email
        self.cod_fornecedor = cod_fornecedor

    def delete_contato(self):
        db.session.delete(self)
        db.session.commit()
