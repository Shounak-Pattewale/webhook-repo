import json
import const as const

from flask import Response, request, jsonify
from mongoengine.errors import FieldDoesNotExist, ValidationError, DoesNotExist

from api.basic_errors import InternalServerError, SchemaValidationError, NoAuthorizationError
from api.models import WebhooksData

# Pull Request and Merge logic

# Pull_request_merge
# if : pull_request.state=="closed" and merged=="true" (mergeable==null)
# then : merged_by.login, merged_at, head.ref -> base.ref

# Pull_request
# if : pull_request.state=="open" and merged=="false" (mergeable==true)
# then : pull_request.user.login, created_at, head.ref -> base.ref


class GithubData:
    def __init__(self):
        pass

    def get(page):
        try:
            # Fetching latest entries
            return WebhooksData.objects.order_by('-_id').paginate(page=page, per_page=const.records_per_page)
        except NoAuthorizationError:
            raise NoAuthorizationError

    def put(data, action):
        try:
            if action == 'PUSH':
                # Push action
                body = {
                    'request_id': data['head_commit']['id'],
                    'author': data['pusher']['name'].replace('-', ' '),
                    'action': action,
                    'from_branch': data['ref'].split('/')[-1],
                    'to_branch': data['ref'].split('/')[-1],
                    'timestamp': data['head_commit']['timestamp']
                }

            if action == 'PULL_REQUEST':
                # Pull request
                if data['pull_request']['state'] == 'open' and not data['pull_request']['merged']:
                    body = {
                        'request_id': str(data['pull_request']['id']),
                        'author': data['pull_request']['user']['login'].replace('-', ' '),
                        'action': action,
                        'from_branch': data['pull_request']['head']['ref'],
                        'to_branch': data['pull_request']['base']['ref'],
                        'timestamp': data['pull_request']['created_at']
                    }
                # Pull request merged
                elif data['pull_request']['state'] == 'closed' and data['pull_request']['merged']:
                    action = 'MERGE'
                    body = {
                        'request_id': str(data['pull_request']['id']),
                        'author': data['pull_request']['merged_by']['login'].replace('-', ' '),
                        'action': action,
                        'from_branch': data['pull_request']['head']['ref'],
                        'to_branch': data['pull_request']['base']['ref'],
                        'timestamp': data['pull_request']['merged_at']
                    }

            webhook = WebhooksData(**body).save()
            return {'id': str(webhook.id)}, const.status_created_201

        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError
