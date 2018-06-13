import uuid

from flask import jsonify, make_response, request, json
from flask_restful import Resource
from flask_cors import cross_origin

from sqlalchemy import Time, cast

from tables import *

def make_error(message, code):
    error = {
        'error' : {
            'message': message,
            'code': code
        }
    }
    return make_response(jsonify(error), code)

class ProductList(Resource):

    def get(self):
        products = ProductDB.query.all()
        return jsonify([s.to_dict() for s in products])

    def post(self):
        data = request.get_json()

        if not data:
            return make_error("Need json data", 400)

        if not data.has_key('name'):
            return make_error("Need parameter 'name'", 400)

        if not data.has_key('price'):
            return make_error("Need parameter 'price'", 400)

        # optional inputs
        description = None
        if data.has_key('description'):
            description = data['description']

        organizer_id = None
        if data.has_key('organizer_id'):
            organizer_id = data['organizer_id']

        id = str(uuid.uuid4())

        # save to database
        product = ProductDB(id=id, name=data['name'], price=data['price'],
                            description=description, organizer_id=organizer_id)
        db.session.add(product)
        db.session.commit()

        response = {
            'message': 'Post received',
            'id': id
        }
        return make_response(jsonify(response), 200)

class Product(Resource):

    def get(self, id):
        product = ProductDB.query.get(id)

        if product:
            return make_response(jsonify(product.to_dict()), 200)
        else:
            return make_error("Product with id '" + str(id) + "' does not exist", 400)


    def put(self, id):
        pass

    def delete(self, id):
        product = ProductDB.query.get(id)

        if product:
            db.session.delete(product)
            db.session.commit()
            return make_response(jsonify({'message': 'Product was deleted'}), 200)
        else:
            return make_error("Product with id '" + str(id) + "' does not exist", 400)

class EventList(Resource):

    def get(self):
        events = EventDB.query.all()
        return jsonify([s.to_dict() for s in events])

    def post(self):
        data = request.get_json()
        print(request)
        print(data)
        # check for required parameters
        if not data:
            return make_error("Need json data", 400)

        if not data.has_key('name'):
            return make_error("Need parameter 'name'", 400)

        if not data.has_key('price'):
            return make_error("Need parameter 'price'", 400)

        if not data.has_key('start_time'):
            return make_error("Need parameter 'start_time'", 400)

        if not data.has_key('start_timezone'):
            return make_error("Need parameter 'start_timezone'", 400)

        if not data.has_key('end_time'):
            return make_error("Need parameter 'end_time'", 400)

        if not data.has_key('end_timezone'):
            return make_error("Need parameter 'end_timezone'", 400)

        # optional inputs
        description = None
        if data.has_key('description'):
            description = data['description']

        organizer_id = None
        if data.has_key('organizer_id'):
            organizer_id = data['organizer_id']

        # other inputs
        id = str(uuid.uuid4())
        start_time = datetime.strptime(data['start_time'], '%Y-%m-%dT%I:%M:%S')
        end_time = datetime.strptime(data['end_time'], '%Y-%m-%dT%I:%M:%S')

        # save to database
        event = EventDB(id=id, name=data['name'], price=data['price'],
                            description=description, organizer_id=organizer_id,
                            start_time=start_time, start_timezone=data['start_timezone'],
                            end_time=end_time, end_timezone=data['end_timezone'])
        db.session.add(event)
        db.session.commit()

        response = {
            'message': 'Post received',
            'id': id
        }
        return make_response(jsonify(response), 200)

class Event(Resource):

    def get(self, id):
        event = EventDB.query.get(id)

        if event:
            return make_response(jsonify(event.to_dict()), 200)
        else:
            return make_error("Event with id '" + str(id) + "' does not exist", 400)


    def put(self, id):
        pass

    def delete(self, id):
        event = ProductDB.query.get(id)

        if event:
            db.session.delete(event)
            db.session.commit()
            return make_response(jsonify({'message': 'Event was deleted'}), 200)
        else:
            return make_error("Event with id '" + str(id) + "' does not exist", 400)

class RecentEventList(Resource):

    def get(self):
        recent_events = EventDB.query.filter(EventDB.syndicated == False)
        return jsonify([s.to_dict() for s in recent_events])

class RecentEvent(Resource):

    # update events to syndicated=True
    def put(self, id):
        syndicated_rows = EventDB.query.filter_by(id=id).update(dict(syndicated=True))
        db.session.commit()

        return jsonify(syndicated_rows)

