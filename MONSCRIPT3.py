#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

def alpha1(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=17,27
    b=237,7
    alpha=[]
    for index,row in data.iterrows():
        c=(a*row['temp'])/((b+row['temp'])+np.ln(row['humidity']))
        alpha.append(c)
    return alpha

def alpha2(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=17,27
    b=237,7
    alpha=[]
    for i in range(len(data)):
        c=(a*data.loc[i,'temp'])/(b+data.loc[i,'temp']+np.ln(data.loc[i,'humidity']))
        alpha.append(c)
    return alpha

def alpha3(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=17,27
    b=237,7
    alpha=[]
    for i in range(len(data)):
        c=(a*data[i]['temp']/(b+data[i]['temp']+np.ln(data[i]['humidity']))
        alpha.append(c)
    return alpha

def temperature_rosee(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=17,27
    b=237,7
    return ((b*alpha(fichier))/(a-alpha(fichier)))

def humidex(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    T_air=data['temp']
    b=5417,7530*((1/273,16)-(1/temperature_rosee(fichier)))
    c=6,11*np.exp(b)-10
    d=T_air+0,555*c
    return d