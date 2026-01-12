# ON IMPORTE LES BIBLIOTHEQUES QUI NOUS SERVIRONT POUR LE PROGRAMME 
import csv
import matplotlib.pyplot as plt

# ON IMPORTE LES FICHIER CSV DANS DES LISTES 
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

CBM=[]
with open('Consommation_brute_mensuelle.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        CBM.append(row)      

# ON ENLEVE LES DESCRIPTEURS DE CHAQUE LISTE 
del EMMR[0]
del PAR[0]
del CBM[0]

# ON CREER UNE LISTE DE COULEUR QUI NOUS SERVIRA POUR LES GRAPHIQUES 
couleurs = [("Blue",    "#0000FF"),("Orange",  "#FFA500"),("Green",   "#008000"),("Red",     "#FF0000"),("Purple",  "#800080"),("Brown",   "#A52A2A"),("Pink",    "#FFC0CB"),("Gray",    "#808080"),("Olive",   "#808000"),("Cyan",    "#00FFFF"),("Magenta", "#FF00FF"),("Yellow",  "#FFFF00"),("Black",   "#000000")]
couleurs_hexadécimal = [i[1] for i in couleurs]
couleurs_noms = [i[0] for i in couleurs]



# FONCTION POUR CALCULER LA PRODUCTION VERTE DES RÉGIONS SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
#PRODUCTION VERTE = SANS NUCLÉAIRE NI THERMIQUE FOSSILE 
def prodvert (année) :
    compteur={}
    for i in range(len(Listeregion)) : # CRÉATION D'UN DICTIONNAIRE AVEC COMME CLÉ LES RÉGIONS DE FRANCE MÉTROPOLITAINE
        compteur[Listeregion[i]]=0
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        region=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if moyenprod!="Nucléaire" and moyenprod!="Thermique fossile" and moyenprod!="Energie produite" and ANNEE==année:
            compteur[region]+= valeur
    regions = list(compteur.keys()) # ON EXTRAIT DU DICTIONNAIRE LES CLÉS ET ON EN FAIT UNE LISTE 
    productions = list(compteur.values()) # PAREIL POUR LES VALEURS DU DICTIONNAIRE 
    plt.figure(figsize=(14,6))
    plt.bar(regions, productions, color=couleurs_noms)
    plt.ylabel("Production verte (TWh)")
    plt.title("Production d'électricité verte par région")
    plt.xticks(rotation=45, ha='right')  # ON TOURNE LES NOMS DES RÉGIONS POUR UNE MEILLEURE LISIBILITÉ
    plt.tight_layout() # MEILLEUR RENDU ESTHETIQUE (MARGE, TEXTE, ETC...) 
    return plt.show()

# FONCTION POUR CALCULER LA PRODUCTION TOTALE DES RÉGIONS SUR UNE ANNÉE DONNÉE
def prodtotale (année) :
    compteur={}
    for i in range(len(Listeregion)) : 
        compteur[Listeregion[i]]=0
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        region=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if moyenprod=="Energie produite" and ANNEE==année:
            compteur[region]+= valeur
    regions = list(compteur.keys())  
    productions = list(compteur.values())  
    plt.figure(figsize=(14,6))
    plt.bar(regions, productions, color=couleurs_noms)
    plt.ylabel("Production totale (TWh)")
    plt.title("Production totale d'électricité par région")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# FONCTION POUR CALCULER LE POURCENTAGE DE PRODUCTION VERTE SUR UNE ANNÉE DONNÉE
# POURCENTAGE DE PRODUCTION VERTE = (PRODUCTION VERTE / PRODUCTION TOTALE) * 100 → ET CELA POUR CHAQUE RÉGION
def pctvert (année) :
    compteur={}
    for i in range(len(Listeregion)) : 
        compteur[Listeregion[i]]=0
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        region=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if moyenprod=="Energie produite" and ANNEE==année:
            compteur[region]+= valeur
    compteur2={}
    for i in range(len(Listeregion)) : 
        compteur2[Listeregion[i]]=0
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        region=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if moyenprod!="Nucléaire" and moyenprod!="Thermique fossile" and moyenprod!="Energie produite" and ANNEE==année:
            compteur2[region]+= valeur
    compteur3={}
    for i in range(len(Listeregion)) : 
        compteur3[Listeregion[i]]=0
    for i in range(len(Listeregion)) :
        compteur3[Listeregion[i]]=(compteur2[Listeregion[i]] / compteur[Listeregion[i]])*100

    regions = list(compteur3.keys()) 
    pct = list(compteur3.values())   
    plt.figure(figsize=(14,6))
    plt.bar(regions, pct, color=couleurs_noms)
    plt.ylabel("Pourcentage de vertuosité (%)")
    plt.title("Pourcentage de vertuosité par région")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# FONCTION POUR CALCULER LA CONSOMMATION TOTALE DES RÉGIONS SUR UNE ANNÉE DONNÉE
def constotale (année) :
    compteur={}
    for i in range(len(Listeregion)) : 
        compteur[Listeregion[i]]=0
    for i in range(len(CBM)) :
        ANNEE=CBM[i][0][0] 
        region=CBM[i][1] 
        valeur=CBM[i][3]
        if année==ANNEE : 
            compteur[region]+=valeur
    regions = list(compteur.keys()) 
    cons = list(compteur.values())   
    plt.figure(figsize=(14,6))
    plt.bar(regions, cons, color=couleurs_noms)
    plt.ylabel("Consommation électrique totale (TWh)")
    plt.title("Consommation électrique totale par région")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# FONCTION POUR CALCULER LA PRODUCTION TOTALE MENSUEL D'UNE RÉGION SUR UNE ANNÉE DONNÉE
def prodtotalemois(année,region) :
    ListeVal=[]
    ListeMois=[]
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        REGION=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if ANNEE==année and REGION==region and moyenprod=="Energie produite" :
            ListeVal.append(valeur)
            ListeMois.append(str(ANNEE)+ '-' + str(EMMR[i][0][1]))   
    plt.figure(figsize=(14,6))
    plt.bar(ListeMois, ListeVal, color="Blue")
    plt.ylabel("Production électrique totale (TWh)")
    plt.title("Consommation électrique totale mensuel")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

"""
# FONCTION POUR CALCULER LA PRODUCTION TOTALE MENSUEL D'UNE RÉGION SUR UNE ANNÉE DONNÉE
def prodtotaleannee(region) :
    ListeVal=[]
    ListeAnnee=[]
    for i in range(len(PAR))) :
        ANNEE=PAR[i][0] 
        REGION=PAR[i][1] 
        valeur=PAR[i][3]
        if REGION==region and moyenprod=="Energie produite" :
            ListeVal.append(valeur)
            ListeMois.append(str(ANNEE)+ '-' + str(EMMR[i][0][1]))   
    plt.figure(figsize=(14,6))
    plt.bar(ListeMois, ListeVal, color="Blue")
    plt.ylabel("Production électrique totale (TWh)")
    plt.title("Consommation électrique totale mensuel")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()
"""

# ON PREPARE NOTRE LISTE PAR (Production Annuelle Région) 
# ON CONVERTIT LES STR EN FLOAT 
for i in range(len(PAR)) :
    PAR[i][3]=PAR[i][3].replace(",",".")
    PAR[i][3]=float(PAR[i][3])

# ON PREPARE NOTRE LISTE CBM (Consommation Brute Mensuel) 
# ON CONVERTIT LES STR EN FLOAT 
for i in range(len(CBM)) :
    CBM[i][3]=CBM[i][3].replace(",",".")
    CBM[i][3]=float(CBM[i][3])

# PUIS ON MODIFIE "2014-01" en [2014, 01] ET CELA POUR TOUTE LES DATES  
for i in range(len(CBM)) :
    CBM[i][0]=CBM[i][0].split('-')
    CBM[i][0][0]=int(CBM[i][0][0])
    CBM[i][0][1]=int(CBM[i][0][1])

# ON CREER UNE LISTE DE TOUS LES MOIS ENTRE 2014 ET 2025
timemois=[EMMR[i][0] for i in range(len(EMMR))]

timemois2=[]
for i in range(len(timemois)) :
    v=timemois[i]
    if v not in timemois2 :
        timemois2.append(v)

# ON REGLE LES PROBLEMES D'ACCENTS POUR TOUTES LES LISTES 
for i in range(len(EMMR)) :
    EMMR[i][1]=EMMR[i][1].replace("ÃŽ","I")
    EMMR[i][1]=EMMR[i][1].replace("Ã©","é")
    EMMR[i][1]=EMMR[i][1].replace("Ã´","ô")
for i in range(len(CBM)) : 
    CBM[i][1]=CBM[i][1].replace("ÃŽ","I")
    CBM[i][1]=CBM[i][1].replace("Ã©","é")
    CBM[i][1]=CBM[i][1].replace("Ã´","ô")
    
# ON MODIFIE LES VALEURS COMME : -1,7011392294819E-19 
# ON REMPLACE LES , PAR DES . 
for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].replace(",",".")
for i in range(len(PAR)) :
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

# ON MODIFIE "2014-01" en [2014, 01] ET CELA POUR TOUTE LES DATES
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

annee = int(input("Quelle année voulez-vous observer ? : (2014-2025) "))

# ON PREPARE UNE FIGURE DE 2/2 
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# ON STOCKE LES FONCTIONS DANS DES VARIABLES
figurebase = plt.figure
showbase = plt.show

# ON CREER UNE FONCTION QUI PERMETTERA DE RENDRE N'IMPORTE QUELLE FONCTION INACTIVE. NOOP SIGNIFIE NO-OPERATIONEL 
def noop(*args, **kwargs): 
# *args = TOUS LES ARGUMENTS POSITIONELS (liste ordonnée). 
# **kwargs = TOUS LES ARGUMENTS NOMMÉS (dictionnaire). 
# ON LES METS DONC POUR QUE NOOP SOIT COMPATIBLE AVEC N'IMPORTE QUEL APPEL.
    pass

# ON REND LES FONCTION INACTIVE 
try:
    plt.figure = noop
    plt.show = noop

# DONC ON INJECTE NOS GRAPHIQUES DANS LA BONNE CASE DE LA FIGURE SANS QU'ILS S'AFFICHENT L'UN APRES L'AUTRE 
# (C'ETAIT L'INTÉRET DE noop ET DES VARIABLES showbase ET figurebase)

    plt.sca(axes[0, 0])  # CASE 0,0 (EN HAUT A GAUCHE)
    prodvert(annee)

    plt.sca(axes[0, 1])  # CASE 0,1 (EN HAUT A DROITE)
    prodtotale(annee)

    plt.sca(axes[1, 0])  # CASE 1,0 (EN BAS A GAUCHE)
    pctvert(annee)

    plt.sca(axes[1, 1])  # CASE 1,1 (EN BAS A DROITE)
    constotale(annee)

# ON REMET LES FONCTIONS DE BASE 
finally:
    plt.figure = figurebase
    plt.show = showbase

# PUIS ON AFFICHE LA FIGURE DE 2/2
fig.tight_layout()
plt.show()

prodtotalemois(annee,"Auvergne-Rhône-Alpes")