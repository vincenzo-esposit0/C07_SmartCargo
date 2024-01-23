from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UtenteRegistrato(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    cognome = Column(String(30), nullable=False)
    dataNascita = Column(DateTime, nullable=False)
    codiceFiscale = Column(String(16), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(20), nullable=False)
    indirizzo = Column(String(255), nullable=False)

    def __init__(self, nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.codiceFiscale = codiceFiscale
        self.email = email
        self.password = password
        self.indirizzo = indirizzo


class OperatoreSala(UtenteRegistrato):
    __tablename__ = 'operatoreSala'

    def __init__(self, nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo):
        # Chiamata al costruttore della superclasse
        super().__init__(nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo)

    def __json__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cognome': self.cognome,
            'dataNascita': str(self.dataNascita),
            'codiceFiscale': self.codiceFiscale,
            'email': self.email,
            'password': self.password,
            'indirizzo': self.indirizzo
        }


class OperatoreIngresso(UtenteRegistrato):
    __tablename__ = 'operatoreIngresso'

    def __init__(self, nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo):
        # Chiamata al costruttore della superclasse
        super().__init__(nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo)

    def __json__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cognome': self.cognome,
            'dataNascita': str(self.dataNascita),
            'codiceFiscale': self.codiceFiscale,
            'email': self.email,
            'password': self.password,
            'indirizzo': self.indirizzo
        }


class OperatoreMobile(UtenteRegistrato):
    __tablename__ = 'operatoreMobile'

    def __init__(self, nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo):
        # Chiamata al costruttore della superclasse
        super().__init__(nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo)

    def __json__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cognome': self.cognome,
            'dataNascita': str(self.dataNascita),
            'codiceFiscale': self.codiceFiscale,
            'email': self.email,
            'password': self.password,
            'indirizzo': self.indirizzo
        }


class OperatoreMagazzino(UtenteRegistrato):
    __tablename__ = 'operatoreMagazzino'

    def __init__(self, nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo):
        # Chiamata al costruttore della superclasse
        super().__init__(nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo)

    def __json__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cognome': self.cognome,
            'dataNascita': str(self.dataNascita),
            'codiceFiscale': self.codiceFiscale,
            'email': self.email,
            'password': self.password,
            'indirizzo': self.indirizzo
        }


class Autotrasportatore(UtenteRegistrato):
    __tablename__ = 'autotrasportatore'

    azienda = Column(String(255), nullable=False)
    qrCode_id = Column(Integer, nullable=False)

    def __init__(self, nome, cognome, azienda, dataNascita, codiceFiscale, email, password, indirizzo, qrCode_id):
        super().__init__(nome, cognome, dataNascita, codiceFiscale, email, password, indirizzo)
        self.azienda = azienda
        self.qrCode_id = qrCode_id  # Aggiunta del qrCode_id come argomento

    def __json__(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cognome': self.cognome,
            'azienda': self.azienda,
            'dataNascita': str(self.dataNascita),
            'codiceFiscale': self.codiceFiscale,
            'email': self.email,
            'password': self.password,
            'indirizzo': self.indirizzo,
            'qrCode_id': self.qrCode_id
        }
