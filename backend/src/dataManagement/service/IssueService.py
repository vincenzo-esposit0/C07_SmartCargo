from src.models.IssueDAO import IssueDAO

issue_dao = IssueDAO()

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