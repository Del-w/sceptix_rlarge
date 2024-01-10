from flask import render_template, Blueprint, request, redirect, url_for 

routes = Blueprint('route', __name__)

@routes.route('/')
def index():
    return render_template('homepage.html')



password_1_binary = '01001010 00101101 01010010 01000100 00101101 01001110 01001111'  
password_2_binary = '01010000 01010011 01010110 00101101 01010010 01000110 01000010'  


def check_password_function(entered_password, stored_password):

    entered_password = (entered_password)

    return entered_password == stored_password


@routes.route('/personnel', methods=['GET', 'POST'])
def Check_Password():
    error_message = None

    if request.method == 'POST':
        entered_password = request.form.get('password_personnel','')

        if check_password_function(entered_password, password_1_binary):
            return redirect(url_for('route.auth'))
        elif check_password_function(entered_password, password_2_binary):
            return redirect(url_for('route.unauth'))
        else:
            error_message = 'Incorrect Password'

    return render_template('personnel.html', error_message=error_message)


@routes.route('/you-are-now-one-of-us')
def auth():
    return render_template('auth.html')

@routes.route('/u-have-been-warned-do-not-return')
def unauth():
    return render_template('unauth.html')

@routes.route('/repent-for-your-sins')
def p():
    return render_template('p.html')
