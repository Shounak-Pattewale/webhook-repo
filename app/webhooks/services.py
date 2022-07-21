import json

from flask import Response, request, jsonify
# from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, ValidationError, DoesNotExist

from app.basic_errors import InternalServerError, SchemaValidationError, NoAuthorizationError
from app.webhooks.models import *

# class BasicBlogsApi(Resource):
#     def get(self):
#         try:
#             return jsonify(Blogs.objects())
#         except NoAuthorizationError:
#             raise NoAuthorizationError

#     def post(self):
#         try:
#             body = request.get_json()
#             datetime_now = datetime.utcnow()
#             body['created_on'] = datetime_now
#             body['modified_on'] = datetime_now
#             blog = Blogs(**body).save()
#             blog.save()
#             id = blog.id
#             return {'id': str(id)}, const.status_created_201
#         except (FieldDoesNotExist, ValidationError):
#             raise SchemaValidationError
#         except Exception:
#             raise InternalServerError