from flask import Flask
from config import DefaultConfig
from .webhooks import services

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

@app.post("/github")
def github():
    if request.headers['Content-Type']=='application/json':
        print("Here : ",request.json)
        return json.dumps(request.json)
    return "hello"

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
