#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet.csv',delimiter=';')

def CORRELATION(fichier,labels1='var1',labels2='var2'):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==1]
    cov=0
    for k in range(len(data)):
        a=+(data[labels1][k]-MOYENNE(fichier,labels1))*((data[labels2][k]-MOYENNE(fichier,labels2)))
    a=a/(len(data)-1)
    return a

def CORRELATION(fichier,labels1='var1',labels2='var2'):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==1]
    cov=0
    for index,row in data.iterrows():
        a=+(row[labels1]-MOYENNE(fichier)*((row['co2']-MOYENNE(fichier)))
    a=a/(data.shape[0]-1)
    return a