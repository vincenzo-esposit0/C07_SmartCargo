from sqlalchemy.orm import sessionmaker
from src.models.Issue import Issue
from src.config.database import engine


class IssueDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_issue(self, issue):
        session = self.Session()
        session.add(issue)
        session.commit()
        session.refresh(issue)
        session.close()
        return issue

    def ottieni_tutte_issues(self):
        session = self.Session()
        issues = session.query(Issue).all()
        session.close()
        return issues

    def ottieni_issue_per_id(self, issue_id):
        session = self.Session()
        issue = session.query(Issue).filter_by(id=issue_id).first()
        session.close()
        return issue

    def ottieni_issue_per_id_operazione(self, op_id):
        session = self.Session()
        issue = session.query(Issue).filter_by(operazione_id=op_id).first()
        session.close()
        return issue

    def aggiorna_issue(self, issue):
        session = self.Session()
        session.merge(issue)
        session.commit()
        session.close()
        return issue

    def elimina_issue(self, issue_id):
        session = self.Session()
        issue = session.query(Issue).filter_by(id=issue_id).first()
        session.delete(issue)
        session.commit()
        session.close()
