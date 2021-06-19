from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
from user import User




@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)


@app.route("/newuser")
def page():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["em"]
    }
    User.save(data)
    return redirect('/')

if __name__=="__main__":   
        app.run(debug=True)    
