from flask import Flask, render_template, request, jsonify
from models import db, Tarefa
import sqlite3


app = Flask(__name__)  

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todolist.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/criar")
def criar():
    return render_template("form.html")

@app.route("/tarefa", methods=["POST"])
def tarefa():
    titulo = request.form["titulo"]  
    descricao = request.form["descricao"]
    nova_tarefa = Tarefa(titulo=titulo, descricao=descricao)  
    db.session.add(nova_tarefa)  
    db.session.commit() 
    return jsonify({"mensagem": "Tarefa criada com sucesso!"})  

@app.route("/lista")
def lista():
    tarefas = Tarefa.query.all() 
    total_tarefas = Tarefa.query.count()
    return render_template("lista.html", tarefas=tarefas, contagem = total_tarefas)

@app.route("/concluir")
def concluir():
    return

@app.route("/excluir")
def excluir():
    return


if __name__ == "__main__": 
    app.run(debug=True)
