from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

_name_ = '_main_'

app = Flask(_name_)

@app.route("/")
def render_main():
        with open('county_demographics.json') as demographics_data:
                counties = json.load(demographics_data)
        if 'states' in request.args:
                return render_template('home.html', states = get_state_options(counties), highestTravelTime = fun_fact(request.args['states'], counties))
        else:
                return render_template('home.html', states = get_state_options(counties))
     
def get_state_options(counties):
        listOfStates = []
        for data in counties:
                if data['State'] not in listOfStates:
                        listOfStates.append(data['State'])
        options = ""
        for data in listOfStates:
                options = options + Markup('<option value="'+data+'">'+data+'</option>')
        return options
def fun_fact(state, counties):
        highestTravelTime = ["county", 0.0]
        for data in counties:
                if data['State'] == state:
                        if highestTravelTime[1] < data['Miscellaneous'] ['Building Permits']:
                                highestTravelTime[1] = data['Miscellaneous'] ['Building Permits']
                                highestTravelTime[0] = data['County']
        return highestTravelTime
if _name_=="_main_":
   app.run(debug=False)
