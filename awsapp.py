# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:13:45 2023

@author: aspdi
"""

from flask import Flask, request
import joblib
model=joblib.load("drug-model.pkl")

app=Flask(__name__)

@app.route('/',methods=['POST'])
           

def output():
    data=request.get_json(force=True)
    print(data)
    data=data['input']   
    print(data)
    out=model.predict(data)
    
    return str(out)

app.run(host='0.0.0.0')

