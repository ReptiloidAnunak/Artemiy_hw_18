import json
from flask_restx import Resource, Namespace

from models import Movie, MovieSchema
from setup_db import db
from flask import request

movies_ns = Namespace('movies')

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query.all()
        return MovieSchema(many=True).dump(movies), 200

    def post(self):
        new_movie_data = json.loads(request.data)
        new_movie = Movie(**new_movie_data)
        db.session.add(new_movie)
        db.session.commit()
        return '', 201, {"location": f"/movies/{new_movie.id}"}

@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = Movie.query.get(mid)
        return MovieSchema().dump(movie), 200

    def put(self, mid):
        movie = Movie.query.get(mid)
        new_movie_data = json.loads(request.data)
        movie.title = new_movie_data.get("title")
        movie.description = new_movie_data.get("description")
        movie.trailer = new_movie_data.get("trailer")
        movie.year = int(new_movie_data.get("year"))
        movie.rating = float(new_movie_data.get("rating"))
        movie.genre_id = int(new_movie_data.get("genre_id"))
        movie.director_id = int(new_movie_data.get("director_id"))
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, mid):
        movie = Movie.query.get(mid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204

@movies_ns.route('/director_id/<int:did>')
class MoviesDirView(Resource):
    def get(self, did):
        movies_raw = Movie.query.all()
        movies_lst = MovieSchema(many=True).dump(movies_raw)
        result = []
        for movie in movies_lst:
            if movie["director_id"] == did:
                result.append(movie)
        return MovieSchema(many=True).dump(result), 200

@movies_ns.route('/genre_id/<int:gid>')
class MoviesDirView(Resource):
    def get(self, gid):
        movies_raw = Movie.query.all()
        movies_lst = MovieSchema(many=True).dump(movies_raw)
        result = []
        for movie in movies_lst:
            if movie["genre_id"] == gid:
                result.append(movie)
        return MovieSchema(many=True).dump(result), 200

@movies_ns.route('/year/<int:y>')
class MoviesYear(Resource):
    def get(self, y):
        movies_raw = Movie.query.all()
        movies_lst = MovieSchema(many=True).dump(movies_raw)
        result = []
        for movie in movies_lst:
            if movie["year"] == y:
                result.append(movie)
        return MovieSchema(many=True).dump(result), 200