from flask_cors import CORS
from flask import Flask, request, jsonify

from src.dataManagement.account import AccountAutotrasportatoreController
from src.dataManagement.autenticazione import LoginController
from src.dataManagement.issue import IssueController
from src.dataManagement.ingresso import IngressoController
from src.dataManagement.monitoraggio import MonitoraggioController

from src.dataManagement.service import OperazioneService
from src.dataManagement.service import AutotrasportatoreService
from src.dataManagement.service import IssueService
from src.dataManagement.service import MerceService
from src.dataManagement.service import VeicoloService

from src.models import QrCodeDAO
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/registrazione', methods=['POST'])
def registrazione():
    data = request.get_json()
    return AccountAutotrasportatoreController.registrazioneAutotrasportatore(data)


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
    result = IssueService.ottieniIssuePerId(id)
    return jsonify(result)


@app.route('/issue/getAll', methods=['GET'])
def getAllIssue():
    return


@app.route('/autotrasportatore/getById/<id>', methods=['GET'])
def getAutotrasportatoreId(id):
    result = AutotrasportatoreService.ottieniAutotrasportatorePerId(id)
    return jsonify(result)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return LoginController.login(data["username"], data["password"])


@app.route('/operazioni/getAll/', methods=['GET'])
def ottieniOperazioni():
    result = OperazioneService.ottieniTutteOperazioniConDettagli()
    return jsonify(result)


@app.route('/merci', methods=['GET'])
def ottieniTutteMerci():
    result = MerceService.ottieniTutteMerci()
    return jsonify(result)


@app.route('/modello', methods=['GET'])
def ottieniTuttiVeicoli():
    result = VeicoloService.ottieniTuttiVeicoli()
    return jsonify(result)


@app.route('/registrazioneIngresso', methods=['POST'])
def registrazioneIngresso():
    data = request.get_json()
    return IngressoController.registrazioneIngresso(data)

@app.route('/qrCodeIngresso', methods=['POST'])
def AutotrasportatoreByIdQrCode():
    data = request.get_json()
    return AutotrasportatoreService.AutotrasportatoreByIdQrCode(data)

@app.route('/getStorico', methods=['POST'])
def trova_operazioni_per_filtri():
    data = request.get_json()
    return MonitoraggioController.trova_operazioni_per_filtri(data)


app.run()
