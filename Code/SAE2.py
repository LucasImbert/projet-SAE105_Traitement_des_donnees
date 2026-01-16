# ON IMPORTE LES BIBLIOTHEQUES QUI NOUS SERVIRONT POUR LE PROGRAMME 
import matplotlib
matplotlib.use("Agg")
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
    plt.bar(regions, productions, color=couleurs_noms)
    plt.ylabel("Production verte (TWh)")
    plt.title(f"Production d'électricité verte par région en ({année})")
    plt.xticks(rotation=45, ha='right')  # ON TOURNE LES NOMS DES RÉGIONS POUR UNE MEILLEURE LISIBILITÉ
    plt.tight_layout() # MEILLEUR RENDU ESTHETIQUE (MARGE, TEXTE, ETC...) 

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
    plt.bar(regions, productions, color=couleurs_noms)
    plt.ylabel("Production totale (TWh)")
    plt.title(f"Production totale d'électricité par région en ({année})")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

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
    plt.bar(regions, pct, color=couleurs_noms)
    plt.ylabel("Pourcentage de vertuosité (%)")
    plt.title(f"Pourcentage de vertuosité par région en ({année})")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

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
    plt.bar(regions, cons, color=couleurs_noms)
    plt.ylabel("Consommation électrique totale (TWh)")
    plt.title(f"Consommation électrique totale par région en ({année})")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  


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
    plt.bar(ListeMois, ListeVal, color="Blue")
    plt.ylabel("Production électrique totale (TWh)")
    plt.title(f"Production électrique totale mensuel pour {region} en {année}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  


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
    plt.ylim(0,140)
    plt.bar(ListeAnnee, ListeVal, color="Blue")
    plt.ylabel("Production électrique totale (TWh)")
    plt.title(f"Production électrique totale anuelle pour {region}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

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
    plt.bar(ListeAnnee, ListeVal, color="Blue")
    plt.ylabel("Consommation électrique totale (TWh)")
    plt.title(f"Consommation électrique totale par mois pour {region} en {année}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

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
    plt.ylim(0,140)
    plt.bar(Annee, prodvert, color="Green")
    plt.ylabel("Production électrique verte (TWh)")
    plt.title(f"Production électrique verte totale pour {region}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

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
    for i in range(len(PAR)) :
        ANNEE2=PAR[i][0] 
        REGION2=PAR[i][1] 
        valeur2=PAR[i][3]
        if REGION2==region :
            compteur2[ANNEE2]+= valeur2
    compteur3={}
    for l in range(12) :
        compteur3[2014+l]=0
    for i in range(len(compteur3)) :
        compteur3[2014+i]=(compteur[2014+i] / compteur2[2014+i])*100
    annee = list(compteur3.keys()) 
    pct = list(compteur3.values()) 
    plt.ylim(0,100)  
    plt.bar(annee, pct, color="Red")
    plt.ylabel("Pourcentage de vertuosité (%)")
    plt.title(f"Pourcentage de vertuosité pour {region} de 2014 à 2025")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

# FONCTION POUR CALCULER LA SOUSTRACTION DE LA PRODUCTION TOTALE MENSUEL A LA CONSOMMATION MENSUEL PUIS EN FAIRE UN HISTOGRAMME EN BARRES
def soustracProdCons(année,region) :
    ListeVal=[]
    ListeAnnee=[]
    for i in range(len(CBM)) :
        ANNEE=CBM[i][0][0] 
        REGION=CBM[i][1] 
        valeur=CBM[i][3]
        if ANNEE==année and region==REGION:
            ListeVal.append(valeur)
            ListeAnnee.append(str(ANNEE)+ '-' + str(EMMR[i][0][1])) 
    ListeVal2=[]
    for i in range(len(EMMR)) :
        ANNEE=EMMR[i][0][0] 
        REGION=EMMR[i][1] 
        moyenprod=EMMR[i][2]
        valeur=EMMR[i][3]
        if ANNEE==année and REGION==region and moyenprod=="Energie produite" :
            ListeVal2.append(valeur)
    ListeVal3=[]
    for i in range(len(ListeVal)):
        ListeVal3.append(ListeVal2[i]-ListeVal[i])
    somme=0
    for valeur in ListeVal3 :
        somme+=valeur
    Moyenne=somme/len(ListeVal3) 
    plt.bar(ListeAnnee, ListeVal3, color="Red")
    plt.ylabel("Différence entre électricité produite et consommé")
    plt.title(f"Différence de production-consommation électrique pour {region} en {annee}")
    fig.text(0.5, 0.01,f"Moyenne de {Moyenne}",ha="center",fontsize=8,color="gray")
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout() 


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

# ON CREER LA LISTE DES ANNEES DE 2014 A 2025 COMPRIS
ListeAnnee=[]
for i in range(12) : 
    ListeAnnee.append(2014+i)

# ON CREER UNE FONCTION QUI PERMETTERA DE RENDRE N'IMPORTE QUELLE FONCTION INACTIVE. NOOP SIGNIFIE NO-OPERATIONEL 
def noop(*args, **kwargs): 
    # *args = TOUS LES ARGUMENTS POSITIONELS (liste ordonnée). 
    # **kwargs = TOUS LES ARGUMENTS NOMMÉS (dictionnaire). 
    # ON LES METS DONC POUR QUE NOOP SOIT COMPATIBLE AVEC N'IMPORTE QUEL APPEL.
        pass

for annee in ListeAnnee :

    # ON PREPARE UNE FIGURE DE 2/2 
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    plt.sca(axes[0, 0])  # CASE 0,0 (EN HAUT A GAUCHE)
    prodvert(annee)
    plt.sca(axes[0, 1])  # CASE 0,1 (EN HAUT A DROITE)
    prodtotale(annee)
    plt.sca(axes[1, 0])  # CASE 1,0 (EN BAS A GAUCHE)
    pctvert(annee)
    plt.sca(axes[1, 1])  # CASE 1,1 (EN BAS A DROITE)
    constotale(annee)

    # PUIS ON ENREGISTRE CHAQUE FIGURE DANS LE DOSSIER SYNTHESE
    nom_fichier = (f"Synthese/bilan_regions_{annee}.png")
    fig.savefig(nom_fichier, dpi=300)
    fig.tight_layout()
    # plt.show(block=False)
    # plt.pause(0.5)   # TEMPS D'AFFICHAGE DE LA FIGURE EN SECONDE POUR QUE LE PROGRAMME DEROULE VITE (ON POURRAIT AUSSI NE PAS AFFICHER LA FIGURE)
    plt.close(fig)


for region in Listeregion :

    fig, axes = plt.subplots(3, 1, figsize=(16, 10))
    plt.sca(axes[0])  # CASE 0 (EN HAUT)
    prodtotaleannee(region)
    plt.sca(axes[1])  # CASE 1 (AU MILIEU)
    prodvertannee(region)
    plt.sca(axes[2])  # CASE 2 (EN BAS)
    pctvertannee(region)

    region_nom = region.replace(" ", "_").replace("-", "_")
    nom_fichier = (f"Annee/bilan_annuel_{region_nom}.png")
    fig.savefig(nom_fichier, dpi=300)
    fig.tight_layout()
    plt.close(fig)


for region in Listeregion :
    for annee in ListeAnnee :

        fig, axes = plt.subplots(3, 1, figsize=(16, 10))
        plt.sca(axes[0])  # CASE 0 (EN HAUT)
        prodtotalemois(annee,region)
        plt.sca(axes[1])  # CASE 1 (AU MILIEU)
        constotalemens(annee,region)
        plt.sca(axes[2])  # CASE 2 (EN BAS)
        soustracProdCons(annee,region)

        region_nom = region.replace(" ", "_").replace("-", "_")
        nom_fichier = (f"Annee/bilan_mensuel_{region_nom}_{annee}.png")
        fig.savefig(nom_fichier, dpi=300)
        fig.tight_layout()
        plt.close(fig)