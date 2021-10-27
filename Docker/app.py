from logging import info
from flask import *
import requests
import json

retorno = list()

app = Flask(__name__, 
            static_url_path='',
            static_folder='web/static/',
            template_folder='web/templates/')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/images', methods=['GET','POST'])
def images():
    if request.method == 'GET':
        retorno.clear()
        for image in json.loads(requests.get('http://localhost:5555/images/json').content):
            retorno.append(dict(image = image['RepoTags'][0], id = image['Id']))
    return jsonify(retorno)

@app.route('/containers', methods=['GET', 'POST'])
def container():
    if request.method == 'GET':
        retorno.clear()
        for info in json.loads(requests.get('http://localhost:5555/containers/json').content):
            retorno.append(dict(id = info['Id'], image = info['Image'], port = info['Ports'][0], status = info['State'], nome= info['Names'][0])) 
    return jsonify(retorno)

app.run(debug=True)