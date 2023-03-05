import requests, os, random
from project import app
from project.twi import Twi
from datetime import date, time, datetime, timedelta
from flask import current_app, render_template, redirect, url_for, flash, request, Response
from flask_mail import Message
import json

# ---------------------
# Base
# ---------------------

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():    
    return render_template('index.html')

#------------------------
# PING
#------------------------

@app.route('/ping', methods=['GET', 'POST'])
def ping():    
    return "pong"

@app.route('/pong')
def pong():
    print("---header---")
    print(request.headers)
    
    print("------data------")
    request_data = request.get_json()
    print(request_data)

    return "ping"


#------------------------
# TWILIO 
#------------------------

@app.route('/outbound', methods=['GET', 'POST'])
def outbound():

    mc = Twi()
    mc.Call()

    return "hello"

#
# http://demo.twilio.com/welcome/voice
# 
@app.route('/inbound', methods=['GET', 'POST'])
def inbound():

    ac = Twi()
    return ac.Hear()


@app.route('/press', methods=['GET', 'POST'])
def press():

    ac = Twi()
    return ac.Press()


@app.route('/set_pin', methods=['GET', 'POST'])
def set_pin():
    print("---header---")
    print(request.headers)
    
    print("------form------")
    print(request.form)

    print("------data------")
    j = json.loads(request.data)
    print(j)

    resp = "You new PIN has been set"
    code = 0
    if j['PIN1'] != j['PIN2']:
        resp = "Your pins are different. Please ensure you key the same PIN"
        code = 1

    if j['PIN1'] == "111111":
        resp = "Sorry. We are unable to locate your profile. Please ensure that you have keyed in the correct ID number"
        code = 2

    raw = {'message' : resp, 'code' : code}
    fmt = json.dumps(raw)
    print(fmt)
    return Response(fmt, status=200, content_type='application/json')