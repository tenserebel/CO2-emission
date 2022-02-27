from function import vehicle,foot_print
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin

app=Flask(__name__)
cors=CORS(app, supports_credentials=True)

@app.route("/", methods=["GET", "POST"])
def index():
    return "api for CO2 emission"

@app.route('/vehicle/<engine_size>/<int:Cylinders>/<fuel_consumption>/<string:fuel_type>',methods=['GET','POST'])
# @cross_origin()
def co2(engine_size,Cylinders,fuel_consumption,fuel_type):
    engine_size=float(engine_size)
    output=vehicle(engine_size,Cylinders,fuel_consumption,fuel_type)
    output=round(output,2)
    return jsonify(output)

@app.route("/personal/<electric_bill>/<gas_bill>/<oil_bill>/<yearly_mileage>/<less_flight>/<more_flight>/<newspaper>/<aluminium>/<currency>")
def personal(electric_bill, gas_bill, oil_bill, yearly_mileage, 
               less_flight, more_flight, newspaper, aluminium, currency):
        output=foot_print(electric_bill, gas_bill, oil_bill, yearly_mileage, 
               less_flight, more_flight, newspaper, aluminium, currency)
        output=round(output,2)
        return jsonify(output) 


if __name__ == '__main__':
    app.run(host = 'localhost', port =80)   