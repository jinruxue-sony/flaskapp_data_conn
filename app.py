# app.py
from flask import Flask, request, render_template, session, redirect           # import flask

app = Flask(__name__)  
from models import Schema
from service import ToDoService

@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())
@app.route("/todo", methods=("POST", "GET"))
def print_data():                      
    return render_template('home.html', tables=[ToDoService().show().to_html(classes='data')], titles=ToDoService().show().columns.values)


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
    