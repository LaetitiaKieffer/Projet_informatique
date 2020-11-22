#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

def MAX(fichier,labels='variable'):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==1]
    a=0
    for index,row in data.iterrows():
        if row[labels]>a:
            a=row[labels]
    return a

def MIN(fichier,labels='variable'):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==1]
    a=30
    for k in range (len(data)):
        if data.loc[k,labels]<a:
            a=data[k,labels]
    return a

def MOYENNE(fichier,labels='variable'):
    data=pd.read_csv(fichier,delimiter=';')
    moy=0
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        moy+=row[labels]
    moy=moy/data.shape[0]
    return moy

def VARIANCE(fichier,labels='variable'):
    data=pd.read_csv(fichier,delimiter=';')
    var=0
    moy=MOYENNE(fichier,labels)
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        var+=(row[labels]-moy)**2
    var=var/data.shape[0]
    return var

def MEDIANE(fichier,labels='variable'):
    data=pd.read_csv(fichier,delimiter=';')
    L=[]
    med=0
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        if row[labels] not in L:
            L.append(row[labels])
    for j in L:
        med+=j
    med=med/len(L)
    return med

#représentation graphique du capteur 1
data_capteur_1=data.loc[data['id']==1]
plt.plot(data_capteur_1['sent_at'],data_capteur_1['temp'])




