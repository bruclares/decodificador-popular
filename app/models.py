from app import db

class Termo(db.Model):
  __tablename__ = 'termos'

  id = db.Column(db.Integer, primary_key=True)
  expressao_original = db.Column(db.String(200), unique=True, nullable=False)
  traducao_popular = db.Column(db.String(500), nullable=False)
  nivel_risco = db.Column(db.String(50), nullable=False) # Ex: Alto, Médio
  categoria_semiotica = db.Column(db.String(100)) # Ex: Suavização, Coerção

  #método para facilitar transformar em JSON depois
  def to_dict(self):
    return {
      'termo': self.expressao_original,
      'traducao': self.traducao_popular,
      'risco': self.nivel_risco,
      'tipo': self.categoria_semiotica
    }

  def __repr__(self):
    return f'<Termo {self.expressao_original}>'