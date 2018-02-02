#!/usr/bin/env python3
# Copyright © 2018 nick3499
# ISC License (ISC)

from flask import Flask, flash, redirect, render_template, request
from urllib3 import PoolManager
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Weather API (WUnderground)"

@app.route("/current/")
def current_cond():
    '''GETs current condition weather data from WU API.'''
    d = {'api_key': 'ad8ef392afe1e78f',
         'state_code': 'IL',
         'personal_weather_station': 'pws:KILMORRI2'}
    pm = PoolManager()
    r = pm.request('GET', 'http://api.wunderground.com/api/' +
                   d['api_key'] + '/conditions/q/' + d['state_code'] +
                   '/' + d['personal_weather_station'] + '.json')
    co = json.loads(r.data.decode('utf-8'))['current_observation']
    try:
        lw = co['leaf_wetness']
    except KeyError:
        pass
    r.close()
    return render_template('base.html', **locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
