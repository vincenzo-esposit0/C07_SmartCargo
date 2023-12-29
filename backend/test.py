from flask import Flask
from flask import jsonify
from flask_cors import CORS

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
    return jsonify(all_obj)

@app.route('/detail/<id>', methods=['GET'])
def detail(id):

    for x in all_obj:
      if int(x['id']) == int(id):
        return jsonify(x)

    return "Record not found", 400

app.run()