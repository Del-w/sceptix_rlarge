from flask import Flask 

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from website.routes import routes

    app.register_blueprint(routes)
  
    return app