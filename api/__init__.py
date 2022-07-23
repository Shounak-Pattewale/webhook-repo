from flask import Flask, url_for, render_template
import const as const
from config import DefaultConfig
from api.webhooks.webhooks_service import *

app = Flask(__name__)

# Load default configuration for the application (common across environments)
app.config.from_object(DefaultConfig)

app.config['MONGODB_SETTINGS'] = {
    'db': app.config['DB_NAME'],
    'host': app.config['DB_URI'],
    'connect': False
}

@app.get('/')
def home():
    try:
        return render_template('home.html')
    except Exception as error:
        return error

# Output in tabular format
@app.get('/table')
def table():
    try:
        return render_template('table.html')
    except Exception as error:
        return error

# Fetching data from db
@app.get('/get')
def get():
    try:
        return GithubData.get()
    except Exception as error:
        return error

# Webhook endpoint for Push Action
@app.post("/github_push")
def github_push():
    try:
        if request.headers['Content-Type']=='application/json':

            data = request.json

            return GithubData.put(data, 'PUSH')
        return {'Response' : 'Bad Request'},const.status_badrequest_400

    except Exception as error:
        return error

# Webhook endpoint for Pull Request Action
@app.post("/github_pull_request")
def github_pull_request():
    try:
        if request.headers['Content-Type']=='application/json':

            data = request.json

            return GithubData.put(data, 'PULL_REQUEST')
        return {'Response' : 'Bad Request'},const.status_badrequest_400
    
    except Exception as error:
        return error

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
