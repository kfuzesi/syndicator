

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Base table with to_dict function that all tables will inherit
class BaseDB(db.Model):
    __abstract__ = True

    def to_dict(self):
        db_dict = {}
        for key in self.__table__.columns._data.keys():
            db_dict[key] = getattr(self, key)
        return db_dict

class ProductDB(BaseDB):
    __tablename__ = 'product'
    id = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500), nullable=True)
    organizer_id = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float)
    syndicated = db.Column(db.Boolean, default=False)

class EventDB(BaseDB):
    __tablename__ = 'event'
    id = db.Column(db.String, primary_key=True, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500), nullable=True)
    organizer_id = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    start_timezone = db.Column(db.String(50))
    end_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_timezone = db.Column(db.String(50))
    currency = db.Column(db.String(50))
    syndicated = db.Column(db.Boolean, default=False)
