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

# FONCTION POUR CALCULER LA PRODUCTION TOTALE DES RÉGIONS SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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

# FONCTION POUR CALCULER LE POURCENTAGE DE PRODUCTION VERTE SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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

# FONCTION POUR CALCULER LA CONSOMMATION TOTALE DES RÉGIONS SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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


# FONCTION POUR CALCULER LA PRODUCTION TOTALE MENSUEL D'UNE RÉGION SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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
    plt.title(f"Production électrique totale mensuel pour {region} en {année}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()


# FONCTION POUR CALCULER LA PRODUCTION TOTALE MENSUEL D'UNE RÉGION SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
def prodtotaleannee(region) :
    ListeVal=[]
    ListeAnnee=[]
    for i in range(len(PAR)) :
        ANNEE=PAR[i][0] 
        REGION=PAR[i][1] 
        valeur=PAR[i][3]
        if REGION==region :
            ListeVal.append(valeur)
            ListeAnnee.append(ANNEE)   
    plt.figure(figsize=(14,6))
    plt.bar(ListeAnnee, ListeVal, color="Blue")
    plt.ylabel("Production électrique totale (TWh)")
    plt.title(f"Production électrique totale anuelle pour {region}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# FONCTION POUR CALCULER LA CONSOMATION TOTALE MENSUEL D'UNE RÉGION SUR UNE ANNÉE DONNÉE PUIS EN FAIRE UN HISTOGRAMME EN BARRES
def constotalemens(année,region) :
    ListeVal=[]
    ListeAnnee=[]
    for i in range(len(CBM)) :
        ANNEE=CBM[i][0][0] 
        REGION=CBM[i][1] 
        valeur=CBM[i][3]
        if ANNEE==année and region==REGION:
            ListeVal.append(valeur)
            ListeAnnee.append(str(ANNEE)+ '-' + str(EMMR[i][0][1]))   
    plt.figure(figsize=(14,6))
    plt.bar(ListeAnnee, ListeVal, color="Blue")
    plt.ylabel("Consommation électrique totale (TWh)")
    plt.title(f"Consommation électrique totale par mois pour {region} en {année}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# FONCTION POUR CALCULER LA PRODUCTION VERTE TOTALE ANNUELLE D'UNE RÉGION PUIS EN FAIRE UN HISTOGRAMME EN BARRES
def prodvertannee(region) :
    compteur = {}
    for i in range(12) :
        compteur[2014+i]=0
    for i in range(len(EMMR)) :
        ANNEE = EMMR[i][0][0]
        REGION = EMMR[i][1]
        moyenprod = EMMR[i][2]
        valeur = EMMR[i][3]
        if REGION == region and moyenprod not in ["Nucléaire", "Thermique fossile", "Energie produite"] :
            compteur[ANNEE]+=valeur
    Annee = sorted(compteur.keys())
    prodvert = [compteur[a] for a in Annee]   
    plt.figure(figsize=(14,6))
    plt.bar(Annee, prodvert, color="Green")
    plt.ylabel("Production électrique verte (TWh)")
    plt.title(f"Production électrique verte totale pour {region}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# FONCTION POUR CALCULER LE POURCENTAGE DE PRODUCTION VERTE POUR UNE REGION (DE 2014 A 2025) PUIS EN FAIRE UN HISTOGRAMME EN BARRES
# POURCENTAGE DE PRODUCTION VERTE = (PRODUCTION VERTE / PRODUCTION TOTALE) * 100 → ET CELA POUR CHAQUE ANNEE
def pctvertannee (region) :
    compteur={}
    for i in range(12) :
        compteur[2014+i]=0
    for i in range(len(EMMR)) :
        ANNEE = EMMR[i][0][0]
        REGION = EMMR[i][1]
        moyenprod = EMMR[i][2]
        valeur = EMMR[i][3]
        if REGION == region and moyenprod not in ["Nucléaire", "Thermique fossile", "Energie produite"] :
            compteur[ANNEE]+=valeur
    compteur2={}
    for m in range(12) :
        compteur2[2014+m]=0
    print(compteur2)
    for i in range(len(PAR)) :
        ANNEE2=PAR[i][0] 
        REGION2=PAR[i][1] 
        valeur2=PAR[i][3]
        if REGION2==region :
            compteur2[ANNEE2]+= valeur
    compteur3={}
    for l in range(12) :
        compteur[2014+l]=0
    for i in range(len(compteur3)) :
        compteur3[compteur3[i]]=(compteur2[compteur3[i]] / compteur[compteur3[i]])*100
    print(compteur3)
    annee = list(compteur3.keys()) 
    pct = list(compteur3.values())   
    plt.figure(figsize=(14,6))
    plt.bar(annee, pct, color=couleurs_noms)
    plt.ylabel("Pourcentage de vertuosité (%)")
    plt.title(f"Pourcentage de vertuosité pour {region} de 2014 à 2025")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  
    return plt.show()

# ON PREPARE NOTRE LISTE PAR (Production Annuelle Région) 
# ON CONVERTIT LES STR EN FLOAT / INT 
for i in range(len(PAR)) :
    PAR[i][3]=PAR[i][3].replace(",",".")
    PAR[i][3]=float(PAR[i][3])
    PAR[i][0]=int(PAR[i][0])

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
    EMMR[i][2]=EMMR[i][2].replace("ÃŽ","I")
    EMMR[i][2]=EMMR[i][2].replace("Ã©","é")
    EMMR[i][2]=EMMR[i][2].replace("Ã´","ô")
for i in range(len(CBM)) : 
    CBM[i][1]=CBM[i][1].replace("ÃŽ","I")
    CBM[i][1]=CBM[i][1].replace("Ã©","é")
    CBM[i][1]=CBM[i][1].replace("Ã´","ô")
    CBM[i][2]=CBM[i][2].replace("ÃŽ","I")
    CBM[i][2]=CBM[i][2].replace("Ã©","é")
    CBM[i][2]=CBM[i][2].replace("Ã´","ô")
for i in range(len(PAR)) : 
    PAR[i][1]=PAR[i][1].replace("ÃŽ","I")
    PAR[i][1]=PAR[i][1].replace("Ã©","é")
    PAR[i][1]=PAR[i][1].replace("Ã´","ô")
    PAR[i][2]=PAR[i][2].replace("ÃŽ","I")
    PAR[i][2]=PAR[i][2].replace("Ã©","é")
    PAR[i][2]=PAR[i][2].replace("Ã´","ô")
    
# ON MODIFIE LES VALEURS COMME : -1,7011392294819E-19 
# ON REMPLACE LES , PAR DES . 
for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].replace(",",".")
    EMMR[i][3]=float(EMMR[i][3])
for i in range(len(PAR)) :
    PAR[i][3]=float(PAR[i][3])


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

plt.close('all')
prodtotalemois(2018,"Auvergne-Rhône-Alpes")
plt.close('all')
constotalemens(2018,"Auvergne-Rhône-Alpes")
plt.close('all')
prodtotaleannee("Auvergne-Rhône-Alpes")
plt.close('all')
prodvertannee("Auvergne-Rhône-Alpes")
pctvertannee("Auvergne-Rhône-Alpes")
