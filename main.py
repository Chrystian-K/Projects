from flask import Flask, render_template, request
from wtforms import Form, TextField, validators, StringField, SubmitField
from scripts import getResponseFromApi, saveToJson, readFromJson

app = Flask(__name__)
 
# home
class SearchForm(Form):
    # create the fiels
    technology = TextField('Technologia:',  validators=[validators.required()])
    place = TextField('Lokalizacja:')
 
@app.route('/')
def index():
    form = SearchForm(request.form)
    return render_template('index.html', form=form)
 
#results
@app.route('/results', methods=('GET', 'POST'))
def search_resluts():
 
    if request.method == 'POST':
        #Get data from forms input
        description = request.form['technology']
        location = request.form['place']
        #Pass data to function and get the request
        saveToJson(description, location)
 
    #read JSON file
    all_jobs = readFromJson()
 
    return render_template('results.html', jobs = all_jobs, description = description , location = location)
 
if __name__=='__main__':
    app.run(debug=True)