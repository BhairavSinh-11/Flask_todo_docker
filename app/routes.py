from flask import Flask,render_template,request,redirect,url_for,Blueprint
from . import db
from .models import Task

main = Blueprint('main', __name__)

@main.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        task_name=request.form['task'].capitalize()
        new_task=Task(task=task_name)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main.home'))    
    
    tasks = Task.query.all()               
    return render_template('home.html', tasks=tasks)         

# delete route

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('main.home'))   

       
        # For Toggling complete and undo 

@main.route('/toggle/<int:task_id>') 
def toggle_task(task_id):
    task_to_toggle = Task.query.get_or_404(task_id)
    task_to_toggle.iscompleted = not task_to_toggle.iscompleted
    db.session.commit()
    return redirect(url_for('main.home'))  