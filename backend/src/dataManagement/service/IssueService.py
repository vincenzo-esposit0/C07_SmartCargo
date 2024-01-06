from src.models.IssueDAO import IssueDAO

issue_dao = IssueDAO()

def ottieniIssuePerId(issue_id):
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

def ottieniTuttiIssue():
    try:
        issues = issue_dao.ottieni_tutte_issues()

        if issues:
            # Utilizza una lista per ottenere una lista di JSON
            issuesJson = [issue.__json__() for issue in issues]

            # Restituisce la lista di JSON come risultato
            return issuesJson
        else:
            return {"message": "Issue non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle issue: {str(e)}")
        return {}
