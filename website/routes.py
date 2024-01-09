from flask import render_template , Blueprint , request, redirect, url_for
from website import create_app

routes = Blueprint ('route',__name__)

@routes.route('/')
def index():
    return render_template('homepage.html')

@routes.route('/personnel')
def personnel():
    return render_template('personnel.html')

password_1 = '01001010 00101101 01010010 01000100 00101101 01001110 01001111'
password_2 = '01010000 01010011 01010110 00101101 01010010 01000110 01000010'

@routes.route('/check_password', methods=['POST'])
def check_password():
    entered_password = request.form.get('password')

    if check_password_function(entered_password, password_1):
        return redirect(url_for('route.auth'))
    elif check_password_function(entered_password, password_2):
        return redirect(url_for('route.unauth'))
    else:
        return redirect(url_for('route.invalid_password'))

@routes.route('/auth')
def auth():
    return render_template('auth.html')

@routes.route('/unauth')
def unauth():
    return render_template('unauth.html')

@routes.route('/')
def invalid_password():
    return ('INVALID PASSWORD')

def check_password_function(entered_password, stored_password):
    return entered_password == stored_password

@routes.route('/pass')
def password():
    return render_template('password.html')

@routes.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')
