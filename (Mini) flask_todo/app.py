from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("__name__")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db" # 4 slashes = absolute path, 3 slashes = relative path
db = SQLAlchemy(app) #initialize db with the settings from this app

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) # nullable=False because we don't wan't this to be left blank
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # return a string every time we create a new el:
    def __repr__(self):
        return "<Task %r>" % self.id

# with app.app_context():
#     db.create_all()

@app.route("/", methods=["POST", "GET"]) # route() accepts only GET method by default
def index():
    if request.method == "POST": # if "Add Task" is pressed...
        task_content = request.form["content"] # var value = input of type "content"
        new_task = Todo(content=task_content) # the Obj created with class Todo (look for upper code)
        try:
            db.session.add(new_task)  # push it to a db
            db.session.commit()
            return redirect("/")
        except:
            return "there was a problem adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # look to all of the db contents in order created and return all of them
        return render_template("index.html", tasks=tasks) # last argument passes it to index.html table

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "there was an error deleting that task"
    
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "there was an issue updating that task"
    else:
        return render_template("update.html", task=task)

if __name__ == "__main__":
    app.run(debug=True)