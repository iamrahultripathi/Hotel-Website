import os
import re
from flask import Flask,render_template,redirect,request
from flask.helpers import get_load_dotenv, total_seconds
from model1 import db,Feedback

app = Flask(name,template_folder='templates')
app.secret_key = 'super secret key'

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        location=request.form['dropdown']
        ordertype=request.form['papa']
        #improvement=improvement
        message=request.form['message']
        
        
        feedback = Feedback(name=name,email=email,location=location,ordertype=ordertype,message=message)

        db.session.add(feedback)
        db.session.commit()
        return render_template('/')
    else:
        return render_template('feedback.html')

