# Da aggiungere al file gitignore, così non dobbiamo modificare ogni volta la passwordandree
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Specifica i dettagli di connessione al database MySQL
username = 'root'
password = 'Sorre2811!'
host = 'localhost'
port = '3306'
# La porta di default per MySQL è 3306
database_name = 'smartcargodb'

# Crea l'URL di connessione per SQLAlchemy
connection_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'

# Crea l'oggetto engine per la connessione al database
engine = create_engine(connection_url)

#Crea una sessione associata al motore
Session = sessionmaker(bind=engine)