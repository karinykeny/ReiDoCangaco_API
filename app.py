from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Produtos(Resource):
    def get(self):
        return {'produtos': 'meus produtos'}


api.add_resource(Produtos, '/produtos')
# http://127.0.0.1:5000/produtos

if __name__ == '__main__':
    app.run(debug=True)
