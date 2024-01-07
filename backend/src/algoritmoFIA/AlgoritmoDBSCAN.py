import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from sklearn.cluster import DBSCAN
from sklearn import metrics
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from haversine import haversine, Unit
from backend.src.dataManagement.service import PercorsoService

#costante che rappresenta il numero di chilometri in radianti
kms_per_radian = 6371.0088

# Funzione per la detenzione di percorsi che non sono ammessi
def detection(df, soglia): #la soglia rappresenta la distanza massima consentita
    no_path = []  # Percorsi non ammessi
    ok_path = []  # Percorsi ammessi
    index = 0
    clusters = rs[['latitude', 'longitude']].to_numpy()
    path = df[['latitude', 'longitude']].to_numpy()
    #va a dimensionare i due array
    for p in path:
        min_dist = 100
        for i in clusters:
            #è utilizzata per calcolare la distanza tra due punti sulla superficie della Terra, dati i loro valori di latitudine e longitudine
            distance = haversine(p, i, unit=Unit.METERS)
            if distance < min_dist:
                min_dist = distance
        if min_dist >= soglia:
            no_path.append(index)
        else:
            ok_path.append(index)
        index += 1

    path_labels = [i for i in range(path.size)]
    ok_path_df = pd.DataFrame(path[ok_path], columns=['latitude', 'longitude'])
    no_path_df = pd.DataFrame(path[no_path], columns=['latitude', 'longitude'])

    fig, ax = plt.subplots(figsize=[10, 6])
    ok_scatter = ax.scatter(ok_path_df['longitude'], ok_path_df['latitude'], c='#1f77b4', edgecolor='None', alpha=0.7, s=120)
    no_scatter = ax.scatter(no_path_df['longitude'], no_path_df['latitude'], c='#e377c2', edgecolor='None', alpha=0.7, s=120)
    path_scatter = ax.scatter(df['longitude'], df['latitude'], c='k', alpha=0.9, s=3)
    ax.set_title('Path analysis')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend([path_scatter, no_scatter, ok_scatter], ['Full path', 'Not on path', 'On path'], loc='upper left')
    plt.show()

    #prova
    return ok_path_df

# Costruisco il DataFrame tramite il DataSet di Training
df = pd.read_excel('training/22July_porto.xlsx')
df.to_csv('training.csv', index=None, header=True)

#prendo le prime istanze per vedere se effettivamente sto costruendo bene il DataFrame
df.head()

# Estraggo le coordinate dal DataFrame e creo un array numpy
coords = df[['latitude', 'longitude']].to_numpy()

# Definisco un epsilon che verrà utilizzata all'interno dell'algoritmo DBSCAN
epsilon = 0.001 / kms_per_radian

start_time = time.time()

# Algoritmo DBSCAN, necessario per trovare i cluster dei punti nel DataFrame
db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))

cluster_labels = db.labels_

# Restituisce il numero di cluster trovati
num_clusters = len(set(cluster_labels))

# Messaggio di conferma di creazione dei cluster
message = 'Clustered {:,} points down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'
print(message.format(len(df), num_clusters, 100 * (1 - float(num_clusters) / len(df)), time.time() - start_time))

# Accuratezza dei cluster
print('Silhouette coefficient: {:0.03f}'.format(metrics.silhouette_score(coords, cluster_labels)))

# Trasforma i gruppi in una serie di pandas, dove ogni elemento è un gruppo di punti
clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])

def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)

#calcolo le coordinate dei punti più centrali di ciascun cluster
centermost_points = clusters.map(get_centermost_point)

# Decomprime l'elenco delle tuple dei punti più centrali (lat, lon) in elenchi separati di lat e lon
#divide le coordinate in due array contenenti rispettivamente latitudine e longitudine
lats, lons = zip(*centermost_points)

# Dai dati di lats/lons crea un nuovo DataFrame di un punto rappresentativo per ogni cluster
#questo array contiene le coordinate dei punti più centrali di ciascun cluster
rep_points = pd.DataFrame({'lon': lons, 'lat': lats})
#prendo le ultime righe del dataset, per verificare rapidamente i risultati ottenuti
rep_points.tail()

# Estraggo la riga dal set di dati originali (per prendere le restanti informazioni su ciascuna coppia di coordinate) in cui lat/lon corrisponde alla lat/lon di ciascuna riga dei punti rappresentativi
rs = rep_points.apply(lambda row: df[(df['latitude'] == row['lat']) & (df['longitude'] == row['lon'])].iloc[0], axis=1)
rs.to_csv('DBSCAN.csv', encoding='utf-8')
rs.tail()

# Mostro l'insieme di cluster che indicano il percorso ammesso
fig, ax = plt.subplots(figsize=[10, 6])
rs_scatter = ax.scatter(rs['longitude'], rs['latitude'], c='#99cc99', edgecolor='None', alpha=0.7, s=120)
df_scatter = ax.scatter(df['longitude'], df['latitude'], c='k', alpha=0.9, s=3)
ax.set_title('Full data set vs DBSCAN reduced set')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.legend([df_scatter, rs_scatter], ['Full set', 'Reduced set'], loc='upper left')
plt.show()

# Percorso di test 1
df_test_1 = pd.read_excel('test/22JulyDOS.xlsx')
df_test_1.to_csv('test_1.csv', index=None, header=True)

# Prende il percorso e la soglia
ok_path_df = detection(df_test_1, 100)

"""
print("Coordinate del percorso corretto:")
print(ok_path_df)
"""

# Dividi i punti di ok_path_df in array separati per latitudine e longitudine
latitudini = ok_path_df['latitude'].to_numpy()
longitudini = ok_path_df['longitude'].to_numpy()

# Concatena i punti di ok_path_df in una stringa per latitudini e longitudini
latitudini_string = ','.join(map(str, latitudini))
longitudini_string = ','.join(map(str, longitudini))

"""
print(latitudini)
print(longitudini)

print(latitudini_string)
print(longitudini_string)
"""

messaggio = PercorsoService.aggiornaPercorsoByAlgoritmo(1, latitudini_string, longitudini_string)

print(messaggio)

# Percorso di test 2
df_test_2 = pd.read_excel('test/23JulyDOS.xlsx')
df_test_2.to_csv('test_2.csv', index=None, header=True)

# Prende il percorso e la soglia
ok_path_df2 = detection(df_test_2, 100)

# Dividi i punti di ok_path_df in array separati per latitudine e longitudine
latitudini = ok_path_df2['latitude'].to_numpy()
longitudini = ok_path_df2['longitude'].to_numpy()

# Concatena i punti di ok_path_df in una stringa per latitudini e longitudini
latitudini_string = ','.join(map(str, latitudini))
longitudini_string = ','.join(map(str, longitudini))

messaggio = PercorsoService.aggiornaPercorsoByAlgoritmo(2, latitudini_string, longitudini_string)
print(messaggio)

# Percorso di test 3
df_test_3 = pd.read_excel('test/29JulyDOS.xlsx')
df_test_3.to_csv('test_3.csv', index=None, header=True)

# Prende il percorso e la soglia
ok_path_df3 = detection(df_test_3, 100)

# Dividi i punti di ok_path_df in array separati per latitudine e longitudine
latitudini = ok_path_df3['latitude'].to_numpy()
longitudini = ok_path_df3['longitude'].to_numpy()

# Concatena i punti di ok_path_df in una stringa per latitudini e longitudini
latitudini_string = ','.join(map(str, latitudini))
longitudini_string = ','.join(map(str, longitudini))

messaggio = PercorsoService.aggiornaPercorsoByAlgoritmo(3, latitudini_string, longitudini_string)
print(messaggio)