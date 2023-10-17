# app.py
from flask import Flask, request, render_template, session, redirect           # import flask

app = Flask(__name__)  
from models import Schema
from service import ToDoService

@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())
@app.route("/todo", methods=["POST"])
def update_todo():
    return ToDoService().update(request.get_json())
@app.route("/todo", methods=("POST", "GET"))
def print_data():                      
    return render_template('home.html', tables=[ToDoService().show().to_html(classes='data')], titles=ToDoService().show().columns.values)
## requests.post("http://localhost:5000/todo", json={"Title":"my first todo", "Description":"my first todo", "DueDate":'2023-01-01', 'UserId':'12'})
## requests.post("http://localhost:5000/todo", json={'images_ls':['batch20230817141858/images/subject019371/og_094d3c584b4a46598fa960b5339f853e.png','batch20230817141858/images/subject018490/og_4c7ce4d6347b4dcdb85e8c77a3e3bb4b.png'], 'vendor':'appen'})

if __name__ == "__main__":
    Schema()
    app.run(debug=True)
    