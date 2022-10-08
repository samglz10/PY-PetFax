from flask import Flask

def create_app(): 
    app = Flask(__name__)
    
    from . import pet
    app.register_blueprint(pet.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    @app.route('/pets')
    def pets():
        return 'These are our pets available for adoption though init.py!'

    return app

