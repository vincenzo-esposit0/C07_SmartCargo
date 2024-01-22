from flask_cors import CORS
from flask import Flask, request, jsonify

#from sqlalchemy.orm import sessionmaker
#from src.config.database import engine

from src.dataManagement.account import AccountAutotrasportatoreController
from src.dataManagement.autenticazione import LoginController
from src.dataManagement.issue import IssueController
from src.dataManagement.ingresso import IngressoController
from src.dataManagement.monitoraggio import MonitoraggioController
from src.dataManagement.account import AccountController
from src.dataManagement.operazioni import OperazioniController


from src.dataManagement.services import OperazioneService
from src.dataManagement.services import OperatoreMobileService

from src.dataManagement.services import AutotrasportatoreService
from src.dataManagement.services import IssueService
from src.dataManagement.services import MerceService
from src.dataManagement.services import VeicoloService

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
    return IssueController.modificaIssue(data)


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
    result = MonitoraggioController.visualizzaStorico(data)
    return jsonify(result)


@app.route('/monitoraggio/esitoOp', methods=['POST'])
def segnalaEsito():
    data = request.get_json()
    return OperazioniController.segnalazione_esito_operazione(data)

@app.route('/monitoraggio/getOpCarScar', methods=['POST'])
def getOpCarScar():
    data = request.get_json()
    return OperazioneService.ottieniOperazioniConDettagliPerOpMagazzino(data["id"])

@app.route('/modificaOperatore', methods=['POST'])
def modificaAccount():
    data = request.get_json()
    return AccountController.modificaAccount(data)

@app.route('/issue/getOpMob', methods=['GET'])
def ottieniTuttiOpMobili():
    result = OperatoreMobileService.ottieniTuttiOperatoriMobile()
    return jsonify(result)

@app.route('/operazioniPerAuto/getAll/', methods=['POST'])
def ottieniOperazioniPerAutotrasportatore():
    data = request.get_json()
    result = OperazioneService.ottieniOperazioniConDettagliPerAutotrasportatore(data)
    return jsonify(result)



app.run()
