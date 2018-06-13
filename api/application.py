

from flask import Flask
from flask_restful import Resource, Api

from tables import *
from resources import *

class HelloWorld(Resource):
    def get(self):
        return "Hello!"

def setup_resources(api):
    api.add_resource(HelloWorld, '/', '/hello')
    api.add_resource(ProductList, '/products')
    api.add_resource(Product, '/products/<id>', endpoint='product')
    api.add_resource(EventList, '/events')
    api.add_resource(Event, '/events/<id>', endpoint='event')

def create_app(app_name='SYNDICATOR_API'):
    app = Flask(app_name)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../syndicator_repo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)
    db.create_all(app=app)

    api = Api(app)
    setup_resources(api)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()