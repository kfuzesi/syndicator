

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

def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../syndicator_repo.db'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(application)
    db.create_all(app=application)

    api = Api(application)
    setup_resources(api)

    return application

if __name__ == "__main__":
    application = create_app()
    application.debug = True
    application.run()