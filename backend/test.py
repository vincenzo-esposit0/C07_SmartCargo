from flask_cors import CORS
from flask import Flask, request, jsonify

from src.dataManagement.autenticazione import LoginController
from src.dataManagement.issue import IssueController

from src.dataManagement.service import OperazioneService
from src.dataManagement.service import AutotrasportatoreService
from src.dataManagement.service import IssueService


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/registrazione', methods=['POST'])
def registrazione():
    data = request.get_json()
    return AutotrasportatoreController.registrazioneAutotrasportatore(data)

@app.route('/issue/newIssue', methods=['POST'])
def nuovaIssue():
    data = request.get_json()
    return IssueController.nuovaIssue(data)

@app.route('/issue/updateIssue', methods=['POST'])
def aggiornaIssue():
    data = request.get_json()
    return IssueController.aggiornaIssue(data)


@app.route('/issue/getIssue/<id>', methods=['GET'])
def ottieniIssue(id):
    result = IssueService.ottieniIssue(id)
    return jsonify(result)


@app.route('/issue/getAll', methods=['GET'])
def getAllIssue():
    return


@app.route('/autotrasportatore/getById/<id>', methods=['GET'])
def getAutotrasportatoreId(id):
    result = AutotrasportatoreService.ottieniAutotrasportatore(id)
    return jsonify(result)



@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return LoginController.login(data["username"], data["password"])


@app.route('/operazioni/getAll/', methods=['GET'])
def ottieniOperazioni():
    result = OperazioneService.ottieniTutteOperazioniConDettagli()
    return jsonify(result)

app.run()