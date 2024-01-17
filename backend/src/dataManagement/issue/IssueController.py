from datetime import datetime

from flask import jsonify
from src.models.Issue import Issue
from src.dataManagement.InterfaceFacade import InterfaceFacade
from src.models.QrCodeDAO import QrCodeDAO
from src.models.OperazioneDAO import OperazioneDAO
from src.models.IssueDAO import IssueDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

qrcode_facade = InterfaceFacade()
qrcode_dao = QrCodeDAO()
operazione_dao = OperazioneDAO()
issue_dao = IssueDAO()
autotrasportatore_dao = AutotrasportatoreDAO()

def nuovaIssue(issueJson):
    try:
        timestamp_chiusura = None

        if issueJson["timestampChiusura"]:
            timestamp_chiusura = datetime.strptime(issueJson["timestampChiusura"], "%Y-%m-%dT%H:%M:%S")

        issue = Issue(
            descrizione=issueJson["descrizione"],
            timestampApertura=datetime.strptime(issueJson["timestampApertura"], "%Y-%m-%dT%H:%M:%S"),
            timestampChiusura=timestamp_chiusura,
            stato=issueJson["stato"],
            tipologiaProblema=issueJson["tipologiaProblema"],
            posizione=issueJson["posizione"],
            operatoreSala_id=issueJson["operatoreSala_id"],
            operatoreMobile_id=issueJson["operatoreMobile_id"],
            operazione_id=issueJson["operazione_id"]
        )
        """"
        #ricerca qrcode attraverso l'id dell'operazione
        operazione = operazione_dao.ottieni_operazione_per_id(issueJson["operazione_id"])
        autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)
        qrcode = qrcode_dao.ottieni_qrCode_per_id(autotrasportatore.qrCode_id)
        """
        qrcode, operazione = qrcode_facade.ottieniQrcodeValidazione(issueJson["operazione_id"])

        #invalidazione qrcode
        qrcode.isValido = False
        qrcode_dao.aggiorna_qrCode(qrcode)

        #set stato operazione in issue aperta
        operazione.stato = "In corso / Issue aperta"
        operazione_dao.aggiorna_operazione(operazione)

        result = issue_dao.aggiungi_issue(issue)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la creazione dell'issue: {str(e)}")
        return {"message": "Errore durante la creazione dell'issue"}

def aggiornaIssue(issueJson):
    try:
        issue_id = issueJson["id"]
        issue = issue_dao.ottieni_issue_per_id(issue_id)

        if issue:
            timestamp_chiusura = None

            if issueJson["timestampChiusura"]:
                timestamp_chiusura = datetime.strptime(issueJson["timestampChiusura"], "%Y-%m-%dT%H:%M:%S")

            issue.descrizione = issueJson["descrizione"]
            issue.timestampApertura = datetime.strptime(issueJson["timestampApertura"], "%Y-%m-%dT%H:%M:%S")
            issue.timestampChiusura = timestamp_chiusura
            issue.stato = issueJson["stato"]
            issue.tipologiaProblema = issueJson["tipologiaProblema"]
            issue.posizione = issueJson["posizione"]
            issue.operatoreSala_id = issueJson["operatoreSala_id"]
            issue.operatoreMobile_id = issueJson["operatoreMobile_id"]
            issue.operazione_id = issueJson["operazione_id"]

            #ricerca qrcode attraverso l'id dell'operazione
            operazione = operazione_dao.ottieni_operazione_per_id(issueJson["operazione_id"])
            autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)
            qrcode = qrcode_dao.ottieni_qrCode_per_id(autotrasportatore.qrCode_id)

            if issue.stato == "Chiusa":
                #validazione qrcode
                qrcode.isValido = True
                qrcode_dao.aggiorna_qrCode(qrcode)

                #set stato operazione in regolare
                operazione.stato = "In corso / Regolare"
                operazione_dao.aggiorna_operazione(operazione)

            result = issue_dao.aggiorna_issue(issue)
            return jsonify(result.__json__())

    ##aggiornare stato issue (da discutere)
    except Exception as e:
        print(f"Errore durante l'aggiornamento dell'issue: {str(e)}")
        return {"message": "Errore durante l'aggiornamento dell'issue"}