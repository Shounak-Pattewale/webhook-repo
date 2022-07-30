from flask import Blueprint, request, jsonify
import const as const
from api.services import GithubData

api = Blueprint('api', __name__, template_folder='templates', static_folder='static', url_prefix='/api')

# Fetching data from db
@api.get('/get')
def get():
    try:
        page = request.args.get('page', 1, type=int)
        return jsonify(GithubData.get(page).items)
    except Exception as error:
        return error

# Webhook endpoint for Push Action
@api.post("/github_push")
def github_push():
    try:
        if request.headers['Content-Type']=='application/json':

            data = request.json

            return GithubData.put(data, 'PUSH')
        return {'Response' : 'Bad Request'},const.status_badrequest_400

    except Exception as error:
        return error

# Webhook endpoint for Pull Request Action
@api.post("/github_pull_request")
def github_pull_request():
    try:
        if request.headers['Content-Type']=='application/json':

            data = request.json

            return GithubData.put(data, 'PULL_REQUEST')
        return {'Response' : 'Bad Request'},const.status_badrequest_400
    
    except Exception as error:
        return error