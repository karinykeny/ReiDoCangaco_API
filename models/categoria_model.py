from sql_alchemy import db


class CategoriaModel(db.Model):
    __tablename__ = 'categoria'

    cod_categoria = db.Column(db.Integer, primary_key=True)
    nome_categoria = db.Column(db.String(50), nullable=False)

    def __init__(self, nome_categoria):
        self.nome_categoria = nome_categoria

    def json(self):
        return {
            'cod_categoria': self.cod_categoria,
            'nome_categoria': self.nome_categoria
        }

    @classmethod
    def find_categoria(cls, cod_categoria):
        categoria = cls.query.filter_by(cod_categoria=cod_categoria).first()
        if categoria:
            return categoria
        return None

    @classmethod
    def find_categoria_nome(cls, nome_categoria):
        categoria = cls.query.filter_by(nome_categoria=nome_categoria).first()
        if categoria:
            return categoria
        return None

    def save_categoria(self):
        db.session.add(self)
        db.session.commit()

    def update_categoria(self, cod_categoria, nome_categoria):
        self.cod_categoria = cod_categoria
        self.nome_categoria = nome_categoria

    def delete_categoria(self):
        db.session.delete(self)
        db.session.commit()
