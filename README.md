# webhook-repo
### Virtual Environment Setup
* venv on Windows
1. py -m pip install --upgrade pip
2. py -m pip install --user virtualenv
3. py -m venv env
4. .\env\Scripts\activate
5. deactivate

* venv on Unix/macOS
1. python3 -m pip install --user --upgrade pip
2. python3 -m pip install --user virtualenv
3. python3 -m venv ./venv
4. source ./venv/bin/activate
5. deactivate

### Installing Packages
pip install -r requirements.txt

### Run Command
* Windows
1. set FLASK_APP=app.py
2. set FLASK_ENV=development
3. flask run

* Unix/macOS
1. export FLASK_APP=app.py
2. export FLASK_ENV=development
3. flask run

### Dot-Env Format (.env)
```HOST_MACHINE_IP="0.0.0.0"
HOST_MACHINE_PORT=5000
DEBUG=True
DEV_TESTING=True	
DB_URI="mongodb+srv://kay:myRealPassword@cluster0.mongodb.net/your-db-name?w=majority"
DB_NAME="your-db-name"
DB_PORT=27017
DB_CONNECTION_TIMEOUT=100000```
