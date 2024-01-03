from sqlalchemy.orm import sessionmaker
from src.config.database import engine
from sqlalchemy.orm.exc import NoResultFound

from src.models.UtenteRegistrato import OperatoreSala, OperatoreIngresso, OperatoreMobile, OperatoreMagazzino, Autotrasportatore

def login(email, password):
    #DOVREI SCRIVERE LA CONNESSIONE???
    Session = sessionmaker(bind=engine)
    session = Session()

    #Cerco l'utente in ciascuna tabella
    try:
        operatore_magazzino = session.query(OperatoreMagazzino).filter_by(email=email, password=password).one()
        return 200, "Operatore Magazzino", operatore_magazzino

    except NoResultFound:
        pass

    try:
        operatore_mobile = session.query(OperatoreMobile).filter_by(email=email, password=password).one()
        return 200, "Operatore Mobile", operatore_mobile

    except NoResultFound:
        pass

    try:
        operatore_sala = session.query(OperatoreSala).filter_by(email=email, password=password).one()
        return 200, "Operatore Sala", operatore_sala

    except NoResultFound:
        pass

    try:
        operatore_ingresso = session.query(OperatoreIngresso).filter_by(email=email, password=password).one()
        return 200, "Operatore Ingresso", operatore_ingresso

    except NoResultFound:
        pass

    try:
        autotrasportatore = session.query(Autotrasportatore).filter_by(email=email, password=password).one()
        return 200, "Autotrasportatore", autotrasportatore

    except NoResultFound:
        return 401, "Credenziali errate", None

    # Se nessuna corrispondenza è stata trovata, l'utente non esiste o la password è errata
    return 404, "Utente non trovato", None

#Prova
status, message, user = login("simone@email.com", "pass12345")

if status == 200:
    print(f"Login riuscito per {message}")
elif status == 401:
    print(f"Errore: {message}")
elif status == 404:
    print(f"Errore: {message}")
else:
    print(f"Errore interno del server: {message}")
