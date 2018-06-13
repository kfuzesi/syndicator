

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import threading

from tables import *
from resources import *
from threads import check_db

INTERVAL = 10

class HelloWorld(Resource):
    def get(self):
        return "Hello!"

def setup_resources(api):
    api.add_resource(HelloWorld, '/', '/hello')
    api.add_resource(ProductList, '/products')
    api.add_resource(Product, '/products/<id>', endpoint='product')
    api.add_resource(EventList, '/events')
    api.add_resource(Event, '/events/<id>', endpoint='event')
    api.add_resource(RecentEventList, '/recentEvents')
    api.add_resource(RecentEvent, '/recentEvents/<id>', endpoint='recent_event')

def create_app():
    application = Flask(__name__)
    CORS(application)

    application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../syndicator_repo.db'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(application)
    db.create_all(app=application)

    api = Api(application)
    setup_resources(api)

    return application

def create_daemon():
    f = threading.Timer(INTERVAL, check_db, [INTERVAL])
    f.daemon = True
    f.start()

if __name__ == "__main__":
    application = create_app()
    application.debug = True
    create_daemon()
    application.run()