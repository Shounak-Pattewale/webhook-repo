from db import db

action_choices = ('PUSH', 'PULL_REQUEST', 'MERGE')

# Database Schema


class WebhooksData(db.Document):
    request_id = db.StringField()
    author = db.StringField()
    action = db.StringField(choices=action_choices, default=None)
    from_branch = db.StringField()
    to_branch = db.StringField()
    timestamp = db.StringField()
