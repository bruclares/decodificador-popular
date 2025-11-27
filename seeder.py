from app import create_app, db 
from app.models import Termo

app = create_app()

dados_iniciais = [
  {
    "expressao_original": "melhorar sua experiência",
    "traducao_popular": "Monitorar seu comportamento para criar perfil de consumo.",
    "nivel_risco": "ALTO",
    "categoria_semiotica": "Eufemismo"
  },
  {
    "expressao_original": "parceiros selecionados",
    "traducao_popular": "Empresas que pagaram pelos seus dados.",
    "nivel_risco": "MÉDIO",
    "categoria_semiotica": "Ocultação"
  }
]

with app.app_context():
  db.drop_all()
  db.create_all()

  for dado in dados_iniciais:
    novo_termo = Termo(**dado)
    db.session.add(novo_termo)

    db.session.commit()
    print("Banco de dados populado com sucesso! Soberania digital ativada.")