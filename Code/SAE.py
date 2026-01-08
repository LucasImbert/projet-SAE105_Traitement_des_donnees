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

del EMMR[0]
del PAR[0]

timemois=[EMMR[i][0] for i in range(len(EMMR))]

x=""
Z=True
Listeregion=[]
Listemoyenprod=[]
for i in range(len(EMMR)) : 
    k=EMMR[i][1]
    z=EMMR[i][2]
    if k==x :
        pass
    else :
        Listeregion.append(k)
        x=k
    for i in range(len(Listemoyenprod)) :
        if z==Listemoyenprod[i] :
            Z=False 
            break
        else :
            Z=True
    if Z==False :
        pass
    if Z==True :
        Listemoyenprod.append(z)

print(Listeregion)
print(Listemoyenprod)

Z2=True
timemois2=[]
for i in range(len(timemois)) :
    v=timemois[i]
    for i in range(len(timemois2)) :
        if v==timemois2[i] :
            Z2=False
            break
        else :
            Z2=True 
    if Z2== False :
        pass
    if Z2== True :
        timemois2.append(v)

print(timemois2)

for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].replace(",",".")
for i in range(len(PAR)) :
    PAR[i][3]=PAR[i][3].replace(",",".")
    PAR[i][3]=float(PAR[i][3])

for i in range(len(EMMR)) :
    EMMR[i][3]=EMMR[i][3].split('E')

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
        
for i in range(len(EMMR)) :
    if len(EMMR[i][3])==2 :
        EMMR[i][3][0]=float(EMMR[i][3][0])
        EMMR[i][3][1]=float(EMMR[i][3][1])
    else : 
        EMMR[i][3][0]=float(EMMR[i][3][0])

for i in range(len(EMMR)) :
    if len(EMMR[i][3])==2 :
        EMMR[i][3]=EMMR[i][3][0]*10**(-1*EMMR[i][3][1])
    else :
        EMMR[i][3]=EMMR[i][3][0]

prodIDF=0
for i in range(len(EMMR)) :
    if EMMR[i][1]=='ÃŽle-de-France' :
        prodIDF+=EMMR[i][3]
print(prodIDF)

ProdmensIDF=[]
for i in range(len(PAR)) :
    if PAR[i][1]=='ÃŽle-de-France' :
        ProdmensIDF.append(PAR[i][3])
print(ProdmensIDF)

plt.figure()

def tauxvertueux (année) :
    