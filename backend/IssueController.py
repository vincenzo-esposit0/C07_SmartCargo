from datetime import datetime

from src.models.QrCodeDAO import QrCodeDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.OperazioneDAO import OperazioneDAO
from src.models.Issue import Issue
from src.models.IssueDAO import IssueDAO
from flask import jsonify

issue_dao = IssueDAO()
operazione_dao = OperazioneDAO()
autotrasportatore_dao = AutotrasportatoreDAO()
qrcode_dao= QrCodeDAO()

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
        #ricerca qrcode attraverso l'id dell'operazione
        operazione = operazione_dao.ottieni_operazione_per_id(issueJson["operazione_id"])
        autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)
        qrcode = qrcode_dao.ottieni_qrCode_per_id(autotrasportatore.qrCode_id)

        #invalidazione qrcode
        qrcode.isValido = False
        qrcode_dao.aggiorna_qrCode(qrcode)

        result = issue_dao.aggiungi_issue(issue)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiunta dell'issue: {str(e)}")
        return {}

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

 #stato = Chiusa
            result = issue_dao.aggiorna_issue(issue)
            return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiornamento dell'issue: {str(e)}")
        return {}

def ottieniIssue(issue_id):
    try:
        issue = issue_dao.ottieni_issue_per_id(issue_id)

        if issue:
            # Restituisci i dettagli dell'issue come JSON
            return issue.__json__()
        else:
            return {"message": "Issue non trovata"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'issue: {str(e)}")
        return {}
