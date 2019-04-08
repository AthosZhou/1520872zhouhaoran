import os
from flask import *
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from wtforms import Form,TextField,PasswordField,validators
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from db import *

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)



class LoginForm(FlaskForm):
    username=StringField("What is your name?",validators=[DataRequired()])
    password=PasswordField("Can you tell me your pwd?",validators=[DataRequired()])
    loginbtn=SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Your name?", validators=[DataRequired()])
    password = PasswordField("Your secret?", validators=[DataRequired()])
    registerbtn = SubmitField("Register")


@app.route("/")
def index():
    session['sorryname'] = False
    return render_template("index.html",thinks=allthinks())


@app.route("/login",methods=["GET","POST"])
def login():
    myForm=LoginForm(request.form)
    if request.method=='POST':
        if isExist(myForm.username.data,myForm.password.data):
            session['username'] = myForm.username.data
            return redirect(url_for('index'))
        else:
            return render_template("login.html",form=myForm)
    return render_template("login.html",form=myForm)


@app.route("/logout")
def logout():
    session['username'] = False
    return redirect(url_for('index'))


@app.route("/register",methods=["GET","POST"])
def register():
    myForm = RegisterForm(request.form)
    if request.method == 'POST':
        if havsExist(myForm.username.data):
            session['sorryname'] = True
            return render_template("register.html", form=myForm)
        else:
            session['sorryname'] = False
            adduser(myForm.username.data,myForm.password.data)
            session['username']=myForm.username.data
            return redirect(url_for('index'))
    return render_template("register.html", form=myForm)


@app.route("/User/<username>",methods=["GET","POST"])
def user(username):
    return render_template("user.html",thethink=histhink(username),username=username)


if __name__ == '__main__':
    app.run(debug=True)