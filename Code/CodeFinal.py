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

# CONVERSITON DES VALEURS DANS TOUTE LES LISTES 
for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].replace(",",".")
    EMMR[i][3]=float(EMMR[i][3])
for i in range(len(CBM)) :
    CBM[i][3]=CBM[i][3].replace(",",".")
    CBM[i][3]=float(CBM[i][3])
for i in range(len(PAR)) :
    PAR[i][3]=PAR[i][3].replace(",",".")
    PAR[i][3]=float(PAR[i][3])
    PAR[i][0]=int(PAR[i][0])

# ON MODIFIE "2014-01" en [2014, 01] ET CELA POUR TOUTE LES DATES DE EMMR ET CBM 
for i in range(len(EMMR)) :
    EMMR[i][0]=EMMR[i][0].split('-')
    EMMR[i][0][0]=int(EMMR[i][0][0])
    EMMR[i][0][1]=int(EMMR[i][0][1])
for i in range(len(CBM)) :
    CBM[i][0]=CBM[i][0].split('-')
    CBM[i][0][0]=int(CBM[i][0][0])
    CBM[i][0][1]=int(CBM[i][0][1])

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

# FONCTION POUR CALCULER LE POURCENTAGE DE PRODUCTION VERTE SUR UNE ANNÉE DONNÉE POUR TOUTES LES REGIONS PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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
    plt.bar(ListeMois, ListeVal, color="Blue")
    plt.ylabel("Production électrique totale (TWh)")
    plt.title(f"Production électrique totale mensuel pour {region} en {année}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  


# FONCTION POUR CALCULER LA PRODUCTION TOTALE ANNUELLE D'UNE RÉGION ENTRE 2014 ET 2025 PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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
    Listemois=[]
    for i in range(len(CBM)) :
        ANNEE=CBM[i][0][0] 
        REGION=CBM[i][1] 
        valeur=CBM[i][3]
        if ANNEE==année and region==REGION:
            ListeVal.append(valeur)
            Listemois.append(str(ANNEE)+ '-' + str(EMMR[i][0][1]))   
    plt.bar(Listemois, ListeVal, color="Blue")
    plt.ylabel("Consommation électrique totale (TWh)")
    plt.title(f"Consommation électrique totale par mois pour {region} en {année}" )
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()  

# FONCTION POUR CALCULER LA PRODUCTION VERTE TOTALE ANNUELLE D'UNE RÉGION ENTRE 2014 ET 2025 PUIS EN FAIRE UN HISTOGRAMME EN BARRES
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

# DICTIONNAIRE POUR ABREGER LE NOM DES REGIONS POUR STOCKER LES FICHIERS 

abreviation_region={"Auvergne-Rhône-Alpes": "ARA","Bourgogne-Franche-Comté": "BFC","Bretagne": "BRE","Centre-Val de Loire": "CVL","Corse": "COR","Grand Est": "GE","Hauts-de-France": "HDF","Ile-de-France": "IDF","Normandie": "NOR","Nouvelle-Aquitaine": "NA","Occitanie": "OCC","Pays de la Loire": "PDL","Provence-Alpes-Côte d’Azur": "PAC"}


# FIGURES POUR LES FONCTIONS DU TYPE PAR ANNEE MAIS POUR TOUTE LES REGIONS 

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
    plt.close(fig)

# FIGURES POUR LES FONCTIONS DU TYPE PAR REGION ET POUR TOUTES LES ANNEES 

for region in Listeregion :

    fig, axes = plt.subplots(3, 1, figsize=(16, 10))
    plt.sca(axes[0])  # CASE 0 (EN HAUT)
    prodtotaleannee(region)
    plt.sca(axes[1])  # CASE 1 (AU MILIEU)
    prodvertannee(region)
    plt.sca(axes[2])  # CASE 2 (EN BAS)
    pctvertannee(region)

    abbr = abreviation_region.get(region, region)
    nom_fichier = f"Annee/bilan_annuel_{abbr}.png"
    fig.savefig(nom_fichier, dpi=300)
    fig.tight_layout()
    plt.close(fig)

# FIGURES POUR LES FONCTIONS DU TYPE PAR ANNEE ET PAR REGION 

for region in Listeregion :
    for annee in ListeAnnee :
        
        fig, axes = plt.subplots(3, 1, figsize=(16, 10))
        plt.sca(axes[0])  # CASE 0 (EN HAUT)
        prodtotalemois(annee,region)
        plt.sca(axes[1])  # CASE 1 (AU MILIEU)
        constotalemens(annee,region)
        plt.sca(axes[2])  # CASE 2 (EN BAS)
        soustracProdCons(annee,region)

        abbr = abreviation_region.get(region, region)
        nom_fichier = f"Mois/bilan_{annee}_{abbr}.png"
        fig.savefig(nom_fichier, dpi=300)
        fig.tight_layout()
        plt.close(fig)

# ON PREPARE DES DICTIONNAIRES AVEC LA MEME METHODE QUE POUR LES FONCTIONS MAIS POUR REALISER LES CLASSEMENT 

compteur={}
for i in range(len(Listeregion)) : 
    compteur[Listeregion[i]]=0
for i in range(len(EMMR)) :
    ANNEE=EMMR[i][0][0] 
    region=EMMR[i][1] 
    moyenprod=EMMR[i][2]
    valeur=EMMR[i][3]
    if moyenprod=="Energie produite" and ANNEE==2024:
        compteur[region]+= valeur
compteur2={}
for i in range(len(Listeregion)) : 
    compteur2[Listeregion[i]]=0
for i in range(len(EMMR)) :
    ANNEE=EMMR[i][0][0] 
    region=EMMR[i][1] 
    moyenprod=EMMR[i][2]
    valeur=EMMR[i][3]
    if moyenprod!="Nucléaire" and moyenprod!="Thermique fossile" and moyenprod!="Energie produite" and ANNEE==2024:
        compteur2[region]+= valeur
compteur3={}
for i in range(len(Listeregion)) : 
    compteur3[Listeregion[i]]=0
for i in range(len(Listeregion)) :
    compteur3[Listeregion[i]]=round((compteur2[Listeregion[i]] / compteur[Listeregion[i]])*100,1)
sorted_compteur3 = dict(sorted(compteur3.items(), key=lambda x: x[1], reverse=True))
regions = list(sorted_compteur3.keys()) 
pct = list(sorted_compteur3.values()) 
print("CLASSEMENT POURCENTAGE PRODUCTION VERTE 2024".center(50, "=")) # ON AFFICHE L'EN-TETE DE L'AFFICHAGE DU CLASSEMENT 
print(f"{"Rang":<5} {"Région":<30} {"% production verte":>5}")
print("-"*50)
tri = sorted(zip(pct, regions), reverse=True) # ON TRIE LES DEUX LISTES DANS L'ORDRE QUE L'ON SOUHAITE ET ON LES COMBINE EN TUPLE
rang = 1
print()
for pct, region in tri:  # BOUCLE QUI VA AFFICHER CHAQUE LIGNE DU CLASSEMENT 
    print(f"{rang:<5} {region:<30} {pct:>5}")
    rang += 1

print()

# ON REFAIT UN CLASSEMENT 

compteur4={}
for i in range(len(Listeregion)) : 
    compteur4[Listeregion[i]]=0
for i in range(len(PAR)) :
    ANNEE=PAR[i][0] 
    region=PAR[i][1] 
    moyenprod=PAR[i][2]
    valeur=PAR[i][3]
    if ANNEE==2024  :
        compteur4[region]=valeur
compteur5={}
for i in range(len(Listeregion)) : 
    compteur5[Listeregion[i]]=0
for i in range(len(CBM)) :
    ANNEE=CBM[i][0][0]
    region=CBM[i][1] 
    moyenprod=CBM[i][2]
    valeur=CBM[i][3]
    if ANNEE==2024 and moyenprod=="Consommation brute" :
        compteur5[region]+=valeur
compteur6={}
for i in range(len(Listeregion)) : 
    compteur6[Listeregion[i]]=0
for region in Listeregion :
    compteur6[region]=round(compteur4[region]-compteur5[region],2)
sorted_compteur6 = dict(sorted(compteur6.items(), key=lambda x: x[1], reverse=True))
diff = list(sorted_compteur6.values()) 
regions2 = list(sorted_compteur6.keys()) 
print("CLASSEMENT PRODUCTION-CONSOMMATION 2024".center(50, "="))
print(f"{"Rang":<5} {"Région":<30} {"Production-Consommation (TWh)":>5}")
print("-"*50)
tri = sorted(zip(diff, regions2), reverse=True)
rang = 1
print()
for diff, region in tri:
    print(f"{rang:<5} {region:<30} {diff:>5}")
    rang += 1

print()

#DERNIER CLASSEMENT 

for cle in compteur5 :
    compteur5[cle]=round(compteur5[cle],2)
regions3 = list(compteur5.keys()) 
cons2 = list(compteur5.values())
print("CLASSEMENT CONSOMMATION 2024".center(50, "="))
print(f"{"Rang":<5} {"Région":<30} {"Consommation (TWh)":>5}")
print("-"*50)
tri = sorted(zip(cons2, regions3))
rang = 1
print()
for cons, region in tri:
    print(f"{rang:<5} {region:<30} {cons:>5}")
    rang += 1
print()

# ON REALISE LE CLASSEMENT FINAL : ON ADDITIONNE LE RANG DES TROIS CLASSEMENTS POUR TOUTE LES REGIONS POUR FAIRE LE CLASSEMENT FINAL
# LE PLUS PETIT TOTAL SERA 1ER

regions_final = Listeregion[:] # ON COPIE LA LISTE 

# ON CALCULE LES RANGS POUR LE % DE PRODUCTION VERT (DESCENDANT = MIEUX)
rangs_verte = {}
valeurs = list(compteur3.values())
ordre = sorted(valeurs, reverse=True)
for reg in regions_final:
    rangs_verte[reg] = ordre.index(compteur3[reg]) + 1

# ON CALCULE LES RANGS POUR LE SOLDE (DESCENDANT = MIEUX)
rangs_solde = {}
valeurs = list(compteur6.values())
ordre = sorted(valeurs, reverse=True)
for reg in regions_final:
    rangs_solde[reg] = ordre.index(compteur6[reg]) + 1

# ON CALCULE LES RANGS POUR LA CONSOMMATION (ASCENDANT = mieux)
rangs_conso = {}
valeurs = list(compteur5.values())
ordre = sorted(valeurs)   # PLUS PETIT = MEILLEUR RANG 
for reg in regions_final:
    rangs_conso[reg] = ordre.index(compteur5[reg]) + 1

# SCORE FINAL = SOMME DES 3 RANGS
score_final = {}
for reg in regions_final:
    score_final[reg] = rangs_verte[reg] + rangs_solde[reg] + rangs_conso[reg]

# TRI FINAL
classement_final = sorted(score_final.items(), key=lambda x: x[1])

# AFFICHAGE COMME POUR LES AUTRES CLASSEMENTS 
print("CLASSEMENT FINAL (somme des 3 rangs)".center(60, "="))
print(f"{'Rang':<5} {'Région':<30} {'Score final':>12}")
print("-"*60)

rang = 1
for reg, score in classement_final:
    print(f"{rang:<5} {reg:<30} {score:>12}")
    rang += 1
