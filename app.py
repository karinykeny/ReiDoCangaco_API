from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from resources.produto import Produtos, Produto, ProdutoCadastro
from resources.fornecedor import Fornecedores, Fornecedor, FornecedorCadastro
from resources.categoria import Categorias, Categoria, CategoriaCadastro
from resources.vendedor import Vendedores, Vendedor, VendedorRegistro
from resources.contato import Contato, ContatoCadastro, Contatos
from resources.vendedor import VendedorLogin, VendedorLogout
from resources.formaPagamento import FormasPagamento, FormaPagamento
from resources.formaPagamento import FormaPagamentoCadastro
from resources.pedido import Pedido, Pedidos, PedidoCadastro
from resources.produtoPedido import ProdutoPedido, ProdutoPedidoCadastro
from blacklist import blacklist

mysql = 'mysql+pymysql://root:@localhost:3307/reicangaco'

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = mysql
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


# Produto
api.add_resource(Produtos, '/produtos')
api.add_resource(ProdutoCadastro, '/produtos/cadastro')
api.add_resource(Produto, '/produtos/<int:id_produto>')

# Forma de Pagamento
api.add_resource(FormasPagamento, '/formas-de-pagamento')
api.add_resource(FormaPagamento, '/forma-de-pagamento/<int:cod_formaPgameno>')
api.add_resource(FormaPagamentoCadastro, '/forma-de-pagamento/cadastro')

# Fornecedor
api.add_resource(Fornecedores, '/fornecedores')
api.add_resource(FornecedorCadastro, '/fornecedores/cadastro')
api.add_resource(Fornecedor, '/fornecedores/<int:cod_fornecedor>')

# Categorias
api.add_resource(Categorias, '/categorias')
api.add_resource(CategoriaCadastro, '/categorias/cadastro')
api.add_resource(Categoria, '/categorias/<int:cod_categoria>')

# Contato
api.add_resource(Contatos, '/contatos')
api.add_resource(ContatoCadastro, '/contato/cadastro')
api.add_resource(Contato, '/contato/<int:cod_contato>')

# Vendedor
api.add_resource(Vendedores, '/usuarios')
api.add_resource(Vendedor, '/usuarios/<int:cod_vendedor>')
api.add_resource(VendedorRegistro, '/cadastro')
api.add_resource(VendedorLogin, '/login')
api.add_resource(VendedorLogout, '/logout')

# Pedido
api.add_resource(Pedidos, '/pedidos')
api.add_resource(PedidoCadastro, '/pedidos/cadastro')
api.add_resource(Pedido, '/pedidos/<int:cod_pedido>')

# Produto/Pedido
api.add_resource(ProdutoPedidoCadastro, '/produto-pedido/cadastro')
api.add_resource(ProdutoPedido, '/produto-pedido/<int:cod_nota>')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)

app.run()
