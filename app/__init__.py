import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
  app = Flask(__name__)

  database_url = os.getenv('DATABASE_URL', 'sqlite:///soberania.db')

  if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

  app.config['SQLALCHEMY_DATABASE_URI'] = database_url
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
  migrate.init_app(app, db)

  # importa e registra as rotas
  from app.controllers import main_bp, termos_bp
  app.register_blueprint(main_bp)
  app.register_blueprint(termos_bp, url_prefix="/api/termos")

  return app
