import const as const
from flask import Blueprint, render_template, request
from api.services import GithubData

views = Blueprint('views', __name__,
                  template_folder='templates', static_folder='static')


@views.get('/')
def home():
    try:
        page = request.args.get('page', 1, type=int)
        pagination = GithubData.get(page)  # receiving pagination object

        return render_template('home.html', page=page, 
                                total_pages=pagination.pages, 
                                max_btn_length=const.PAGINATION_BTN_LENGTH)

    except Exception as error:
        return error


@views.get('/table')
def table():
    try:
        page = request.args.get('page', 1, type=int)
        pagination = GithubData.get(page)  # receiving pagination object

        return render_template('table.html', page=page, 
                                total_pages=pagination.pages, 
                                max_btn_length=const.PAGINATION_BTN_LENGTH)

    except Exception as error:
        return error
