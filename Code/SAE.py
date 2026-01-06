import csv

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
#   EMMR[i][3]=int(EMMR[i][3])
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





# for i in range(len(EMMR)) : 
    
    


'''
for i in range(len(EMMR))
    if 
'''