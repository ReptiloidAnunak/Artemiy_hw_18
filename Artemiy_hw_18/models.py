# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)

# Пример
from setup_db import db
from marshmallow import fields, Schema

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre = db.relationship("Genre")
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director = db.relationship("Director")
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Integer()
    director_id = fields.Integer()

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()