from flask import Flask

def create_app(): 
    app = Flask(__name__)

    # factory 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/petfax-app_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    @app.route('/pets')
    def pets():
        return 'These are our pets available for adoption though init.py!'

    return app


# factory 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 