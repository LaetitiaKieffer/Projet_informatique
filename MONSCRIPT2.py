#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet.csv',delimiter=';')


def MAX(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=0
    for index,row in data.iterrows():
        if row['temp']>a:
            a=row['temp']
    return a


def MIN(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=30
    for index,row in data.iterrows():
        if row['temp']<a:
            a=row['temp']
    return a
