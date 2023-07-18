# All my routes go in here now..... Follow for all routes format---> table_name/id/actions

from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_model import User


@app.route('/')  #This is the home route for my page
@app.route('/users')  #The "@" decorater associates this route with the function immediately following
def all_users():
    all_users = User.get_all()
    return render_template("Read_All.html", all_users=all_users)



@app.route('/users/new')   #the route to display the new user form
def new_user():
    return render_template("Create.html")

    

@app.route('/users/create', methods=['POST'])  #create a new user when they login
def create_user():
    print("Request form", request.form)
    User.create(request.form)
    return redirect('/users')



@app.route('/users/<int:id>/view') #only asking to get one user view link
def view_one_user(id):
    data = {
        'id': id
    }
    one_user = User.get_one(data)
    return render_template('one_user.html', one_user=one_user)



@app.route('/users/<int:id>/edit')   #editing the user information form
def edit_user_form(id):
    data = {
        'id': id
    }
    one_user = User.get_one(data)
    return render_template("user_edit.html", one_user=one_user)   # after making this step go and make a edit.html form  



@app.route('/users/<int:id>/update', methods=['POST'])  # Update is a action route so we will be returning a redirect back to that action route
def update_user(id):
    print(request.form)
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id': id
    }
    User.update(data)
    return redirect('/')



@app.route('/users/<int:id>/delete')  # Update is a action route so we will be returning a redirect back to that action route
def delete_user(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')