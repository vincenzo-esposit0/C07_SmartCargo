import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Specifica i dettagli di connessione al database MySQL
# Le credenziali si leggono dalle variabili d'ambiente (vedi backend/.env.example)
username = os.environ.get('DB_USER', 'root')
password = os.environ.get('DB_PASSWORD', '')
host = os.environ.get('DB_HOST', 'localhost')
port = os.environ.get('DB_PORT', '3306')
# La porta di default per MySQL è 3306
database_name = os.environ.get('DB_NAME', 'smartcargodb')

# Crea l'URL di connessione per SQLAlchemy
connection_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'

# Crea l'oggetto engine per la connessione al database
engine = create_engine(connection_url)

#Crea una sessione associata al motore
Session = sessionmaker(bind=engine)