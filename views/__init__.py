from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='templates', static_folder='static')

@views.get('/')
def home():
    try:
        return render_template('home.html')
    except Exception as error:
        return error

# Output in tabular format
@views.get('/table')
def table():
    try:
        return render_template('table.html')
    except Exception as error:
        return error