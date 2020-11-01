from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from flask_restful import Api
from resources.produto import Produtos, Produto
from resources.fornecedor import Fornecedores, Fornecedor
from resources.vendedor import Vendedores, Vendedor, VendedorRegistro
from resources.vendedor import VendedorLogin, VendedorLogout
from blacklist import blacklist

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reicangaco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENEBLED'] = True
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    db.create_all()


@jwt.token_in_blacklist_loader
def verificar_blacklist(token):
    return token['jti'] in blacklist


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'mensagem': 'Você foi deslogado.'}), 401


api.add_resource(Produtos, '/produtos')
api.add_resource(Produto, '/produtos/<int:id_produto>')
api.add_resource(Fornecedores, '/fornecedores')
api.add_resource(Fornecedor, '/fornecedores/<int:cod_fornecedor>')
api.add_resource(Vendedores, '/usuarios')
api.add_resource(Vendedor, '/usuarios/<int:cod_vendedor>')
api.add_resource(VendedorRegistro, '/cadastro')
api.add_resource(VendedorLogin, '/login')
api.add_resource(VendedorLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
