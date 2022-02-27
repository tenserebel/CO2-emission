from flask import Flask, request, jsonify, make_response,render_template,redirect,url_for
from flask_cors import CORS, cross_origin
import requests
import json

app=Flask(__name__)
cors=CORS(app, supports_credentials=True)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route("/vehicle", methods=["GET", "POST"])
def vehicle():
    data=''
    if request.method=='POST':
        size=request.form.get('size')
        cylinder=request.form.get('cylinder')
        fuel_con=request.form.get('fuel_con')
        type1=request.form.get('type')
        url = f"https://co2.kk-001.repl.co/vehicle/{size}/{cylinder}/{fuel_con}/{type1}"
        response = requests.get(url)
        data = response.text
        
    return render_template('vehicle.html',data=data)

@app.route('/footprint',methods=["GET", "POST"])
def carbon_footprint():
    return render_template('carbon_footprint.html')

if __name__ == '__main__':
    app.run(host = 'localhost', port=8080,use_reloader=False) 