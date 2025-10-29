from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate

migrate = Migrate()    

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # DB & Migrate initialiseren
    db.init_app(app)
    migrate.init_app(app, db)  

    # Zorg dat modellen geladen zijn vóór migraties draaien
    with app.app_context():
        from . import models   # belangrijk voor auto-generatie van migraties
        # db.create_all()  VERWIJDERd — migraties nemen dit over

    # Blueprints registreren
    from .routes import main
    app.register_blueprint(main)

    return app