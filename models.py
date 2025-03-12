from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo da tabela "tarefas"
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(250), nullable=False)
    concluida = db.Column(db.Boolean, default=False)
