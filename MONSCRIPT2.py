#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet.csv',delimiter=';')

def MAX(fichier):
    maxs=[]
    data=pd.read_csv(fichier,delimiter=';')
    a=0
    for index,row in data.iterrows():
        if row['temp']>a:
            a=row['temp']
    L.append(a)


def MAX2(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=0
    maxs=[]
    for i in range (1,7):
        datainter=data.loc[data['id']==i]
        for index,row in data.iterrows():
            if row['temp']>a:
                a=row['temp']
        maxs.append(a)
    return maxs


def MIN(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=30
    mins=[]
    for i in range (1,7):

    for index,row in data.iterrows():
        if row['temp']<a:
            a=row['temp']
    return a

def MOYENNE(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    moy=0
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        moy+=row['temp']
    moy=moy/data.shape[0]
    return moy

def VARIANCE(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    var=0
    moy=MOYENNE(fichier)
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        var+=(row['temp']-moy)**2
    var=var/data.shape[0]
    return var

def MEDIANE(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    L=[]
    med=0
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        if row['temp'] not in L:
            L.append(row['temp'])
    for j in L:
        med+=j
    med=med/len(L)
    return med

#représentation graphique du capteur 1
data_capteur_1=data.loc[data['id']==1]
plt.plot(data_capteur_1['sent_at'],data_capteur_1['temp'])




