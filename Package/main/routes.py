from flask import render_template,Blueprint

main = Blueprint('main',__name__)


@main.route('/')
def hello_world():  # put application's code here
    return render_template('index.html',title='Home')

@main.route('/error')
def error():
    return render_template('Error.html',title='Error')