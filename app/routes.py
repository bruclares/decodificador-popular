from flask import Blueprint, render_template, jsonify
from app.models import Termo

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/api/termos')
def get_termos():
  # pega todos os termos do banco
  termos = Termo.query.all()
  # returna como JSON para o JS usar
  return jsonify([t.to_dict() for t in termos])