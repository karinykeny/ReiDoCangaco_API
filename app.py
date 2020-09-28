from flask import Flask
from flask_restful import Api
from resources.produto import Produtos, Produto

app = Flask(__name__)
api = Api(app)

api.add_resource(Produtos, '/produtos')
api.add_resource(Produto, '/produtos/<int:id_produto>')

if __name__ == '__main__':
    app.run(debug=True)
