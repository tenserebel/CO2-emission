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
        url = f"https://co2-emission1.herokuapp.com/vehicle/{size}/{cylinder}/{fuel_con}/{type1}"
        response = requests.get(url)
        data = response.text
        return data 

    if(request.method == 'GET'):
        return render_template('vehicle.html')    
        
    return render_template('vehicle.html',data=data)


@app.route('/footprint',methods=["GET", "POST"])
def carbon_footprint():
    data=""
    if request.method=='POST':
        currency=request.form.get('currency')
        electric=request.form.get('electric')
        gas=request.form.get('gas')
        oil=request.form.get('oil')
        yearly_mileage=request.form.get('yearly_mileage')
        less_flight=request.form.get('less_flight')
        more_flight=request.form.get('more_flight')
        recycle_paper=request.form.get('recycle_paper')
        recycle_aluminum=request.form.get('recycle_aluminum')
        print(electric,currency,recycle_paper,recycle_aluminum)
        url = f"https://co2-emission1.herokuapp.com/personal/{electric}.0/{gas}.0/{oil}.0/{yearly_mileage}.0/{less_flight}/{more_flight}/{recycle_paper}/{recycle_aluminum}/{currency}"
        print(url)
        response = requests.get(url)
        data = response.text
        
        return data

    if(request.method == 'GET'):
        return render_template('carbon_footprint.html')

    return render_template('carbon_footprint.html',data=data)

if __name__ == '__main__':
    app.run() 