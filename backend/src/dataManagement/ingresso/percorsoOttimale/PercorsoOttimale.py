import pandas as pd
from itertools import combinations

from src.dataManagement.ingresso.percorsoOttimale.AlgAStar import distanza_haversine, a_star
from src.dataManagement.ingresso.percorsoOttimale.Node import Node
from src.dataManagement.services import PercorsoService


def percorso_ottimale(gate):
    # Definizione del punto di partenza
    start_point = Node(lat=39.4305577, lon=-0.3351722)
    percorsoId = 0

    # Definizione del punto  di destinazione
    if gate == "M1":
        percorsoId = 1
        end_point = Node(lat=39.4242222, lon=-0.3140294)
    elif gate == "M2":
        percorsoId = 2
        end_point = Node(lat=39.441493, lon=-0.3274658)
    elif gate == "M3":
        percorsoId = 3
        end_point = Node(lat=39.4384956, lon=-0.3037465)
    else:
        raise ValueError("Il gate deve essere 1, 2 o 3.")

    # Legge i dati delle coordinate da un file CSV e crea una lista di tuple (coordinate)
    file_path = "src\dataManagement\ingresso\percorsoOttimale\coordinate.csv"
    df = pd.read_csv(file_path, names=['latitudine', 'longitudine'])

    # Converte la colonna della latitudine in numeri
    df['latitudine'] = pd.to_numeric(df['latitudine'], errors='coerce')

    # Converte la colonna della longitudine in numeri
    df['longitudine'] = pd.to_numeric(df['longitudine'], errors='coerce')

    # Rimuove le righe duplicate
    df_no_duplicates = df.drop_duplicates(subset=['latitudine', 'longitudine']).copy()
    # Rimuove le righe con dati mancanti
    df_no_duplicates = df_no_duplicates.dropna(subset=['latitudine', 'longitudine'])

    # Crea la lista delle coordinate
    dataset = [(row['latitudine'], row['longitudine']) for index, row in df_no_duplicates.iterrows()]

    # Crea il grafo rappresentato come un dizionario delle liste di adiacenza
    graph = {coord: [] for coord in dataset}

    # Trova le coppie di coordinate vicine e aggiunge gli archi al grafo
    for coord1, coord2 in combinations(dataset, 2):
        if distanza_haversine(coord1[0], coord1[1], coord2[0], coord2[1]) < 0.026:  # Soglia di 26 metri per decidere i vicini
            graph[coord1].append(coord2)
            graph[coord2].append(coord1)

    # Individuazione del percorso ottimale utilizzando l'algoritmo A*
    path = a_star(start_point, end_point, graph)

    """
    # Dividi i punti di ok_path_df in array separati per latitudine e longitudine
    latitudini = path['latitudine'].to_numpy()
    longitudini = path['longitudine'].to_numpy()
    """

    latitudini = []
    longitudini = []

    for node in path:
        lat = node[0]
        lon = node[1]

        latitudini.append(lat)
        longitudini.append(lon)

    # Concatena i punti di ok_path_df in una stringa per latitudini e longitudini
    latitudini_string = ','.join(map(str, latitudini))
    longitudini_string = ','.join(map(str, longitudini))

    messaggio = PercorsoService.aggiornaPercorsoByAlgoritmo(percorsoId, latitudini_string, longitudini_string)

    print(messaggio)

    return path