from datetime import datetime
from db import db

class WebhooksData(db.Document):
    request_id = db.StringField()
    author = db.StringField()
    action = db.StringField()
    from_branch = db.StringField()
    to_branch = db.StringField()
    timestamp = db.StringField()