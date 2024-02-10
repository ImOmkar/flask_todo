from flask import render_template, request, url_for, flash, redirect
from flask_todo import app, db
from .models import Todo
from .forms import TodoForm


@app.route("/")
@app.route("/home")
def home():
    form = TodoForm()
    return render_template('home.html', form=form, title="Home")

@app.route("/todos", methods=['GET'])
def todos():
    todos = Todo.query.order_by(Todo.date_created)
    if todos:
        return render_template('todos.html', todos=todos)
    else:
        return render_template('todos.html', legend="nothing")

@app.route("/create/", methods=['GET', 'POST'])
def create_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo = form.todo.data
        todo_data = Todo(todo=todo)
        db.session.add(todo_data)
        db.session.commit()
        flash('New todo added', 'success')
        return redirect(url_for('todos'))
    elif request.method == 'GET':
        form = TodoForm()
    else:
        flash('Failed to add new todo', 'error')
        return redirect(url_for('todos'))
    return render_template('create.html', form=form)

@app.route("/todos/<int:id>/delete/", methods=['POST'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted', 'success')
    return redirect(url_for('todos'))

@app.route("/todos/<int:id>/update/", methods=['GET', 'POST'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        todo.todo = form.todo.data
        db.session.commit()
        flash('Todo updated!', 'success')
        return redirect(url_for('todos'))
    elif request.method == 'GET':
        form.todo.data = todo.todo
    else:
        flash('Failed to update todo', 'success')
        return redirect(url_for('todos'))
    return render_template('update.html', form=form, todo=todo)