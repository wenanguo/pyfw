from flask import Blueprint
from flask_restful import Api


from app.api_1_0.respful import Users

api = Blueprint('api', __name__)
rest_api = Api(api, catch_all_404s=True)


rest_api.add_resource(Users, '/users')

#from . import authentication, users, errors,devops
