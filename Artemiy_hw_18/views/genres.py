
from flask_restx import Resource, Namespace

from models import Genre, GenreSchema
from setup_db import db
from flask import request

genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        return GenreSchema(many=True).dump(genres), 200

@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        return GenreSchema().dump(genre), 200