from datetime import datetime
from src.models.Issue import Issue
from src.models.IssueDAO import IssueDAO
from flask import jsonify

issue_dao = IssueDAO()

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

            result = issue_dao.aggiorna_issue(issue)
            return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiornamento dell'issue: {str(e)}")
        return {}
