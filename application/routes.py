from application import app
from flask import render_template, request, redirect, flash, url_for

from bson import ObjectId

from .forms import TodoForm
from application import db
from datetime import datetime


@app.route("/")
def get_todos():
    todos = []
    for todo in db.todos_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)

    return render_template("view_todos.html", todos = todos)
    
@app.route("/add_todo", methods = ['POST', 'GET'])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        name = form.name.data
        print(name)
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data

        db.todos_flask.insert_one({
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity,
            "date_created": datetime.utcnow()
        })
        # flash("Item successfully added", todo_name)
        return redirect("/")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form = form)


@app.route("/delete_todo/<id>")
def delete_todo(id):
    print(id)
    todo = db.todos_flask.find_one({"_id": ObjectId(id)})
    print(todo)
    
    db.todos_flask.find_one_and_delete({"_id": ObjectId(id)})
    # flash("Item successfully deleted", name)
    return redirect("/")


@app.route("/update_todo/<id>", methods = ['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        name = form.name.data
        description = form.description.data
        price = form.price.data
        quantity = form.quantity.data
        print(ObjectId(id))
        db.todos_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity,
            "date_created": datetime.utcnow()
        }})
        # flash("Item successfully updated", "success")
        return redirect("/")
    else:
        form = TodoForm()

        todo = db.todos_flask.find_one({"_id": ObjectId(id)})
        print(todo)
        form.name.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.price.data = todo.get("price", None)
        form.quantity.data = todo.get("quantity", None)

    return render_template("add_todo.html", form = form)