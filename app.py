from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib.pyplot as plt
from flask_cors import CORS
from tensorflowpredict import loadeverything

app= Flask(__name__)
app.debug=True

CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db' #three slashes for relative url and 4 slashes for absolute url

db =SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    completed=db.Column(db.Integer,default=0)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        pass
    else:
        return render_template('index.html')
    
image=[]
result=[]


@app.route("/upload",methods=["GET","POST","OPTIONS"])
def upload():

    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type'}
    # return "hello",200,headers
    if request.method == 'OPTIONS':
        print("options")
        # Handle preflight request
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, headers
    else:
        # Handle actual request
        image.append(request.json.get('image'))


        print(image)
        # Process the selected image here
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        print(image.dtype)
        return jsonify({'success': True}), 200,headers


@app.route("/view",methods=["GET","POST","OPTIONS"])
def view():
    # print(image)
    if len(image)>0:
        return image[-1]
     

@app.route("/predict",methods=["GET","POST","OPTIONS"])
def predict():
    loadeverything()
    



if __name__=="__main__":
    print("the app is running :) ~ Adwaith")
    app.run(debug=True)
    