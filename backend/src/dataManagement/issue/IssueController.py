from datetime import datetime

from flask import jsonify

from src.dataManagement.Facade import InterfaceFacade
from src.models.Issue import Issue
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

        issue = Issue(
            descrizione=issueJson["descrizione"],
            timestampApertura=datetime.now(),
            timestampChiusura=timestamp_chiusura,
            stato=issueJson["stato"],
            tipologiaProblema=issueJson["tipologiaProblema"],
            posizione=issueJson["posizione"],
            operatoreSala_id=issueJson["operatoreSala_id"],
            operatoreMobile_id=issueJson["operatoreMobile_id"],
            operazione_id=issueJson["operazione_id"]
        )
        # utilizzo dell'interfaccia Facade pcd er accedere ai vari oggetti entity per l'individuazione del qrcode e dell'operazione
        qrcode, operazione = qrcode_facade.ottieniQrcodeValidazione(issueJson["operazione_id"])

        # invalidazione qrcode
        qrcode.isValido = False
        qrcode_dao.aggiorna_qrCode(qrcode)

        # set stato operazione in issue aperta
        operazione.stato = "In corso / Issue aperta"
        operazione_dao.aggiorna_operazione(operazione)

        result = issue_dao.aggiungi_issue(issue)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la creazione dell'issue: {str(e)}")
        return {"message": "Errore durante la creazione dell'issue"}


def modificaIssue(issueJson):
    try:
        issue_id = issueJson["id"]
        issue = issue_dao.ottieni_issue_per_id(issue_id)

        if issue:
            timestamp_chiusura = None

            issue.descrizione = issueJson["descrizione"]
            issue.timestampChiusura = timestamp_chiusura
            issue.stato = issueJson["stato"]
            issue.tipologiaProblema = issueJson["tipologiaProblema"]
            issue.posizione = issueJson["posizione"]
            issue.operatoreSala_id = issueJson["operatoreSala_id"]
            issue.operatoreMobile_id = issueJson["operatoreMobile_id"]
            issue.operazione_id = issueJson["operazione_id"]

            # utilizzo dell'interfaccia Facade per accedere ai vari oggetti entity per l'individuazione del qrcode e dell'operazione
            qrcode, operazione = qrcode_facade.ottieniQrcodeValidazione(issueJson["operazione_id"])

            if issue.stato == "Chiusa":
                # validazione qrcode
                qrcode.isValido = True
                qrcode_dao.aggiorna_qrCode(qrcode)

                # salvataggio della data di chiusura dell'issue
                issue.timestampChiusura = datetime.now()

                # set stato operazione in regolare
                operazione.stato = "In corso"
                operazione_dao.aggiorna_operazione(operazione)

            result = issue_dao.aggiorna_issue(issue)
            return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiornamento dell'issue: {str(e)}")
        return {"message": "Errore durante l'aggiornamento dell'issue"}
