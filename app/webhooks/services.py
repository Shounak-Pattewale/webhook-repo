import json

from flask import Response, request, jsonify
# from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, ValidationError, DoesNotExist

from app.basic_errors import InternalServerError, SchemaValidationError, NoAuthorizationError
from app.webhooks.models import *

class GithubData:
    def __init__(self):
        pass

    def get():
        try:
            return jsonify(WebhooksData.objects())
        except NoAuthorizationError:
            raise NoAuthorizationError

    def push(data,action):
        try:
            if action=='push':
                body['request_id'] = data['id']
                body['author'] = data['name']
                body['action'] = action
                body['from_branch'] = ''
                body['to_branch'] = ''
                body['timestamp'] = data['timestamp']
                webhook = WebhooksData(**body).save()
                print("ID : ",str(webhook.id))
                return {'id': str(webhook.id)}, const.status_created_201
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError