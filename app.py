from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib.pyplot as plt
from flask_cors import CORS
from tensorflowpredict import predict
from PIL import Image
from io import BytesIO
import numpy as np

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

    print(request.method)
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

        # image.append(request.json.get('image'))
        keys = request.args.keys()
        print(keys)
        print(request)
        image_data = request.files['image']
        print(type(image_data))
        # img = Image.open(BytesIO(image_data.read()))
        # print(type(img))
        # # Assuming you have the file object `file_storage` which contains the image
        # # You can convert it to a numpy array like this


        image = Image.open(image_data)
        # image = Image.open(image_data.read())

        image.save("./image.jpg")

        # image_array = np.frombuffer(image_bytes, np.uint8)
        
        prediction=predict("./image.jpg")
        return jsonify({'success': True,
                        'prediction': prediction.tolist()}), 200,headers


@app.route("/view",methods=["GET","POST","OPTIONS"])
def view():
    # print(image)
    if len(image)>0:
        return image[-1]
     





if __name__=="__main__":
    print("the app is running :) ~ Adwaith")
    app.run(debug=True)
    