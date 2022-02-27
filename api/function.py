import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
from currency_converter import CurrencyConverter

model1=pickle.load(open('model.pkl','rb'))

def vehicle(eng_size,cylinder,fuel,type):
    type_d,type_e,type_n,type_x,type_z=0,0,0,0,0
    if type=="D":
        type_d+=1
    elif type=="E":
        type_e+=1
    elif type=="N":
        type_n+=1
    elif type=="X":
        type_x+=1
    else:
        type_z+=1
    y_pred = model1.predict([[eng_size,cylinder,fuel,type_d,type_e,type_n,type_x,type_z]])[0]
    return y_pred


def convert(amount, currency):
    
    c = CurrencyConverter()
    convert = c.convert(amount, str(currency), 'USD')
    
    return convert 

def foot_print(electric_bill, gas_bill, oil_bill, yearly_mileage, 
               less_flight, more_flight, newspaper, aluminium, currency):
    
    electric = int(convert(electric_bill, currency)*105)
    
    gas = int(convert(gas_bill, currency)*105)

    oil = int(convert(oil_bill, currency)*113)

    mileage = float((yearly_mileage) * 0.79)
    less_flight = int(less_flight * 1100)
    more_flight = int(more_flight* 4400)
    total =  electric+gas+oil+mileage+less_flight+more_flight
    
    if newspaper == "True" :
        pass
    else: 
        total +=  184
    
    if aluminium == "True" :
        pass
    else: 
        total +=  166 
    
    return total
         