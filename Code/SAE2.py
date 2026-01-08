import random
import csv
import matplotlib.pyplot as plt

EMMR=[]
with open('Energie_produite_mensuelle_par_moyen_par_region.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        EMMR.append(row)
        
PAR=[]
with open('Production_annuelle_par_region.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        PAR.append(row)        

# On enlève les descripteurs 
del EMMR[0]
del PAR[0]

# Fonction pour calculer la production verte des régions sur une année donnée puis en faire un histogramme en barre
# Production verte = Pas de nucléaire ni de thermique focile 
def tauxvertueux (année) :
    compteur={}
    for i in range(len(Listeregion)) : # Création d'un dictionnaire avec comme clé les régions de France métropolitaine
        compteur[Listeregion[i]]=0
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        region=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if moyenprod!="Nucléaire" and moyenprod!="Thermique fossile" and moyenprod!="Autre" and moyenprod!="Energie produite" and ANNEE==année:
            compteur[region]+= valeur
    regions = list(compteur.keys()) # On extrait du dictionnaire les clés et on en fait une liste 
    productions = list(compteur.values()) # Pareil pour les valeurs du dictionnaire 
    couleurs = [(random.random(), random.random(), random.random()) for i in regions]
    plt.figure(figsize=(14,6))
    plt.bar(regions, productions, color=couleurs)
    plt.ylabel("Production verte (TWh)")
    plt.xlabel("Régions")
    plt.title("Production d'électricité verte par région")
    plt.xticks(rotation=45, ha='right')  # On tourne les noms des régions pour une meilleure lisibilité
    plt.tight_layout() # Meilleur rendu esthétique 
    return plt.show()

# ON CREER UNE LISTE DE TOUS LES MOIS ENTRE 2014 ET 2025
timemois=[EMMR[i][0] for i in range(len(EMMR))]

timemois2=[]
for i in range(len(timemois)) :
    v=timemois[i]
    if v not in timemois2 :
        timemois2.append(v)

# ON REGLE LES PROBLEMES D'ACCENTS
for i in range(len(EMMR)) :
    EMMR[i][1]=EMMR[i][1].replace("ÃŽ","I")
    EMMR[i][1]=EMMR[i][1].replace("Ã©","é")
    EMMR[i][1]=EMMR[i][1].replace("Ã´","ô")

# MODIFIER LES VALEURS COMME : -1,7011392294819E-19

# ON REMPLACE LES , PAR DES . 
for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].replace(",",".")
for i in range(len(PAR)) :
    PAR[i][3]=PAR[i][3].replace(",",".")
    PAR[i][3]=float(PAR[i][3])

# ON SPLIT LES VALEURS AU NIVEAU DU E 
for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].split('E')

# ON ENLEVE LES -
chaine=""
for i in range(len(EMMR)) :
    if EMMR[i][3][0][0]=="-" :
        for k in range(len(EMMR[i][3][0])-1) :
            chaine+=EMMR[i][3][0][k+1]
        EMMR[i][3][0]=chaine
        chaine=''
    if EMMR[i][3][0][0]==0 or EMMR[i][3][0][0]==1 or EMMR[i][3][0][0]==2 or EMMR[i][3][0][0]==3 :
        pass
    if len(EMMR[i][3])==2 :
        if EMMR[i][3][1][0]=='-' :
            for k in range(len(EMMR[i][3][1])-1) :
                chaine += EMMR[i][3][1][k+1]
        EMMR[i][3][1]=chaine
        chaine=''

# ON CONVERTIT TOUT EN FLOAT        
for i in range(len(EMMR)) :
    if len(EMMR[i][3])==2 :
        EMMR[i][3][0]=float(EMMR[i][3][0])
        EMMR[i][3][1]=float(EMMR[i][3][1])
    else : 
        EMMR[i][3][0]=float(EMMR[i][3][0])

# ON RECALCULE LES VALEURS 
for i in range(len(EMMR)) :
    if len(EMMR[i][3])==2 :
        EMMR[i][3]=EMMR[i][3][0]*10**(-1*EMMR[i][3][1])
    else :
        EMMR[i][3]=EMMR[i][3][0]

#MODIFIER "2014-01" en [2014, 01]
for i in range(len(EMMR)) :
    EMMR[i][0]=EMMR[i][0].split('-')
    EMMR[i][0][0]=int(EMMR[i][0][0])
    EMMR[i][0][1]=int(EMMR[i][0][1])

# ON CREER UNE LISTE CONTENANT LES NOMS DES REGIONS FRANCAISES (France métropolitaine) ET UNE LISTE AVEC TOUS LES TYPES DE PRODUCTION D'ELECTRICITE
 
Listeregion=[]
Listemoyenprod=[]
for i in range(len(EMMR)) : 
    k=EMMR[i][1]
    z=EMMR[i][2]
    if k not in Listeregion :
        Listeregion.append(k)
    if z not in Listemoyenprod :
        Listemoyenprod.append(z)

année=int(input("Quelle années voulez vous observer ? : (2014-2025) "))
tauxvertueux(année)
print(Listeregion)
print(Listemoyenprod)
print(timemois2)