from flask_cors import CORS
from flask import Flask, request, jsonify

#from sqlalchemy.orm import sessionmaker
#from src.config.database import engine

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

"""
Session = sessionmaker(bind=engine)
session = Session()
"""

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

"""
@app.route('/logout', methods=['POST'])
def logout():
    # Invalida la sessione
    session.clear()
    return jsonify({"stato": 200, "message": "Sessione invalidata"})
"""

@app.route('/operazioni/getAll/', methods=['GET'])
def ottieniOperazioni():
    result = OperazioneService.ottieniOperazioniPerOpAttive()
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
    result = MonitoraggioController.trova_operazioni_per_filtri(data)
    return jsonify(result)


@app.route('/monitoraggio/esitoOp', methods=['POST'])
def segnalaEsito():
    data = request.get_json()
    return MonitoraggioController.aggiorna_stato_operazione(data)

@app.route('/monitoraggio/getOpCarScar', methods=['POST'])
def getOpCarScar():
    data = request.get_json()
    return OperazioneService.ottieniOperazioniConDettagliPerOpMagazzino(data["id"])


app.run()
