#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

def alpha(fichier,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    a=17,27
    b=237,7
    Liste_alpha=[]
    for k in range (len(data)):
        c=(a*data['temp'][k])/(b+data['temp'][k])+np.log10(data['humidity'][k])
    return c

def temperature_rosee(fichier,capteur):
    a=17,27
    b=237,7
    rosee=[]
    for j in range(len(alpha(fichier))):
        rosee.append((b*alpha(fichier)[j])/(a-alpha(fichier)[j]))
    return rosee

def humidex(fichier,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    T_air=data['temp']
    H=[]
    for i in range(len(temperature_rosee(fichier))):
        b=5417,7530*((1/273,16)-(1/temperature_rosee(fichier)[i]))
        c=6,11*np.exp(b)-10
        d=T_air[i]+0,555*c
        H.append(d)
    return H
