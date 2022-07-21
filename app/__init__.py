import json
from flask import Flask, request
from config import DefaultConfig
from .webhooks.services import GithubData

app = Flask(__name__)

# Load default configuration for the application (common across environments)
app.config.from_object(DefaultConfig)

# Db config settings
app.config['MONGODB_SETTINGS'] = {
    'db': app.config['DB_NAME'],
    'host': app.config['DB_URI'],
    'connect': False
}

@app.get('/')
def home():
    return "Success"

@app.post("/github_push")
def github_push():
    if request.headers['Content-Type']=='application/json':
        data = request.json
        GithubData.push(data['head_commit'], 'push')

        # Serializing json
        json_object = json.dumps(request.json, indent=4)
        
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        return json.dumps(request.json)
    return "hello"



if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
