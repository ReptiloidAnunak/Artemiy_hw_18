
from flask_restx import Resource, Namespace

from models import Director, DirectorSchema

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        return DirectorSchema(many=True).dump((directors)), 200

@directors_ns.route('/<did>')
class DirectorView(Resource):
    def get(self, did):
        director = Director.query.get(did)
        return DirectorSchema().dump(director), 200
