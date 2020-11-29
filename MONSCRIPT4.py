#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

def CORRELATION(fichier,caractéristique1,caractéristique2,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    cov=0
    a=0
    b=0
    c=0
    moycar1=MOYENNE(fichier,caractéristique1,capteur)
    moycar2=MOYENNE(fichier,caractéristique2,capteur)
    for index,row in data.iterrows():
        a=+(row[caractéristique1]-moycar1)*((row[caractéristique2]-moycar2))
        b=+(row[caractéristique1]-moycar1)**2
        c=+(row[caractéristique2]-moycar2)**2
    b=b/len(data)
    c=c/len(data)
    b=np.sqrt(b)
    c=np.sqrt(c)
    a=a/(len(data)-1)
    cov=a/(b*c)
    return cov
