#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("C:/EIVP")
fichier="EIVP_KM.csv"
data=pd.read_csv(fichier,delimiter=';')

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

def MAX(fichier,caractéristique):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==1]
    a=0
    for index,row in data.iterrows():
        if row[caractéristique]>a:
            a=row[caractéristique]
    return a

def MIN(fichier,caractéristique):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==1]
    a=30
    for k in range (len(data)):
        if data.loc[k,caractéristique]<a:
            a=data[k,caractéristique]
    return a

def MOYENNE(fichier,caractéristique):
    data=pd.read_csv(fichier,delimiter=';')
    moy=0
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        moy+=row[caractéristique]
    moy=moy/data.shape[0]
    return moy

def VARIANCE(fichier,caractéristique):
    data=pd.read_csv(fichier,delimiter=';')
    var=0
    moy=MOYENNE(fichier,caractéristique)
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        var+=(row[caractéristique]-moy)**2
    var=var/data.shape[0]
    return var

def MEDIANE(fichier,caractéristique):
    data=pd.read_csv(fichier,delimiter=';')
    L=[]
    med=0
    data=data.loc[data['id']==1]
    for index,row in data.iterrows():
        if row[caractéristique] not in L:
            L.append(row[caractéristique])
    for j in L:
        med+=j
    med=med/len(L)
    return med

nn