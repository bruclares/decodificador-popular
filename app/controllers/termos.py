from flask import Blueprint, jsonify
from app.models import Termo

termos_bp = Blueprint('termos', __name__)

@termos_bp.route('')
def get_termos():
  # pega todos os termos do banco
  termos = Termo.query.all()
  # returna como JSON para o JS usar
  return jsonify([t.to_dict() for t in termos])