import const as const
from flask import Blueprint, request, jsonify
from api.services import GithubData

api = Blueprint('api', __name__, template_folder='templates',
                static_folder='static', url_prefix='/api')


@api.get('/get')
def get():
    try:
        page = request.args.get('page', 1, type=int)
        pagination = GithubData.get(page)  # receiving pagination object

        return jsonify({
            'data': pagination.items,
            'total_pages': pagination.pages
            })

    except Exception as error:
        return error


@api.post("/github_push")  # webhook endpoint for Push action
def github_push():
    try:
        if request.headers['Content-Type'] == 'application/json':
            data = request.json

            return GithubData.put(data, 'PUSH')

        return {'Response': 'Bad Request'}, const.STATUS_BADREQUEST_400

    except Exception as error:
        return error


@api.post("/github_pull_request")  # webhook endpoint for Pull Request action
def github_pull_request():
    try:
        if request.headers['Content-Type'] == 'application/json':
            data = request.json

            return GithubData.put(data, 'PULL_REQUEST')

        return {'Response': 'Bad Request'}, const.STATUS_BADREQUEST_400

    except Exception as error:
        return error
