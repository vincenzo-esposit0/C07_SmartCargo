import sys
sys.path.append('C:\\Users\\maria\\IdeaProjects\\C07_SmartCargo')

from flask import Flask
from flask import jsonify
from flask_cors import CORS

from backend.src.models.VeicoloDAO import VeicoloDAO

veicolo_dao = VeicoloDAO()

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

all_obj = [ { 'id': 1, 'name': 'name1' },
  { 'id': 2, 'name': 'name2' },
  { 'id': 3, 'name': 'name3' },
  { 'id': 4, 'name': 'name4' },
  { 'id': 5, 'name': 'name5' },
  { 'id': 6, 'name': 'name6' },
  { 'id': 7, 'name': 'name7' },
  { 'id': 8, 'name': 'name8' },
  { 'id': 9, 'name': 'name9' },
  { 'id': 10, 'name': 'name10' }]

@app.route('/list', methods=['GET'])
def heroes():
    tutti_veicoli = veicolo_dao.ottieni_tutti_veicoli()
    # Estrai i dati di ogni veicolo come dizionario
    veicoli_data = [veicolo.__json__() for veicolo in tutti_veicoli]

    return jsonify(veicoli_data)

@app.route('/detail/<id>', methods=['GET'])
def detail(id):

    veicolo = veicolo_dao.ottieni_veicolo_per_id(id)

    return jsonify(veicolo.__json__())


app.run()