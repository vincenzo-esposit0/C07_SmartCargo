from backend.src.models.Issue import issue
from backend.src.models.IssueDAO import IssueDAO

# Creazione di un'istanza di IssueDAO
issue_dao = IssueDAO()

# Ottieni tutte le issue
print("Tutte le issue:")
tutte_issue = issue_dao.ottieni_tutte_issues()
for issue in tutte_issue:
    print(f"ID: {issue.id}, Descrizione: {issue.descrizione}, Timestamp Apertura: {issue.timestampApertura}, Timestamp Chiusura: {issue.timestampChiusura}, Stato: {issue.stato}, Tipologia Problema: {issue.tipologiaProblema}, Posizione: {issue.posizione}, Operatore Sala ID: {issue.operatoreSala_id}, Operatore Mobile ID: {issue.operatoreMobile_id}, Operazione ID: {issue.operazione_id}")

# Ottieni un'issue con ID 1
print("\nIssue con ID 1:")
issue_id = 1
issue_1 = issue_dao.ottieni_issue_per_id(issue_id)
if issue_1:
    print(f"ID: {issue_1.id}, Descrizione: {issue_1.descrizione}, Timestamp Apertura: {issue_1.timestampApertura}, Timestamp Chiusura: {issue_1.timestampChiusura}, Stato: {issue_1.stato}, Tipologia Problema: {issue_1.tipologiaProblema}, Posizione: {issue_1.posizione}, Operatore Sala ID: {issue_1.operatoreSala_id}, Operatore Mobile ID: {issue_1.operatoreMobile_id}, Operazione ID: {issue_1.operazione_id}")
else:
    print(f"Nessuna issue trovata con ID {issue_id}")

# Inserisci una nuova issue
nuova_issue = Issue(descrizione='Nuova Issue', timestampApertura='2024-01-01 10:00:00', timestampChiusura='2024-01-01 12:00:00', stato='Aperta', tipologiaProblema='Problema Tecnico', posizione='Ubicazione', operatoreSala_id=1, operatoreMobile_id=2, operazione_id=3)
issue_dao.aggiungi_issue(nuova_issue)

# Ottieni tutte le issue dopo l'inserimento
print("\nTutte le issue dopo l'inserimento:")
tutte_issue_dopo = issue_dao.ottieni_tutte_issues()
for issue in tutte_issue_dopo:
    print(f"ID: {issue.id}, Descrizione: {issue.descrizione}, Timestamp Apertura: {issue.timestampApertura}, Timestamp Chiusura: {issue.timestampChiusura}, Stato: {issue.stato}, Tipologia Problema: {issue.tipologiaProblema}, Posizione: {issue.posizione}, Operatore Sala ID: {issue.operatoreSala_id}, Operatore Mobile ID: {issue.operatoreMobile_id}, Operazione ID: {issue.operazione_id}")

# Elimina un'issue (ad esempio, con ID 2)
issue_da_eliminare_id = 2
issue_dao.elimina_issue(issue_da_eliminare_id)

# Ottieni tutte le issue dopo l'eliminazione
print("\nTutte le issue dopo l'eliminazione:")
tutte_issue_dopo_elim = issue_dao.ottieni_tutte_issues()
for issue in tutte_issue_dopo_elim:
    print(f"ID: {issue.id}, Descrizione: {issue.descrizione}, Timestamp Apertura: {issue.timestampApertura}, Timestamp Chiusura: {issue.timestampChiusura}, Stato: {issue.stato}, Tipologia Problema: {issue.tipologiaProblema}, Posizione: {issue.posizione}, Operatore Sala ID: {issue.operatoreSala_id}, Operatore Mobile ID: {issue.operatoreMobile_id}, Operazione ID: {issue.operazione_id}")
