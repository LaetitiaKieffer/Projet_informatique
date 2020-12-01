#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tabeau excel Laetitia
fichier='/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv'
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

#import tableau excel Joséphine
os.chdir("C:/EIVP")
fichier="EIVP_KM.csv"
data=pd.read_csv(fichier,delimiter=';')

#méthode 1 : avec des listes
def alpha(fichier,capteur):
    data =pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    a=17.27
    b=237.7
    Liste_alpha=[]
    for k in range (len(data)):
        c=(a*data['temp'][k])/(b+data['temp'][k])+np.log10(data['humidity'][k])
        Liste_alpha.append(c)
    return Liste_alpha

def temperature_rosee(fichier,capteur):
    a=17.27
    b=237.7
    rosee=[]
    for j in range(len(alpha(fichier,capteur))):
        rosee.append((b*alpha(fichier,capteur)[j])/(a-alpha(fichier,capteur)[j]))
    return rosee

def humidex(fichier,capteur):
    T_air=data['temp']
    H=[]
    for i in range(len(temperature_rosee(fichier,capteur))):
        b=5417,7530*((1/273,16)-(1/temperature_rosee(fichier,capteur)[i]))
        c=6,11*np.exp(b)-10
        d=T_air[i]+0,555*c
        H.append(d)
    return H

#méthode 2 : avec le dataframe

#définition des constantes
a=17.27
b=237.7

def humidex_tableau(fichier,capteur):
    datacapteur=data.loc[data['id']==capteur]
    datacapteur_copy=datacapteur.copy()
    datacapteur_copy['alpha']=\
    (datacapteur_copy['temp']*a)/(b+datacapteur_copy['temp'])+np.log10(datacapteur_copy['humidity'])
    datacapteur_copy["température_rosée"]=(b*datacapteur_copy["alpha"])/(a-datacapteur_copy["alpha"])
    datacapteur_copy['b']=5417.7350*((1/273.16)-(1/datacapteur_copy["température_rosée"]))
    datacapteur_copy['c']=6.11*np.exp(b)-10
    datacapteur_copy['humidex']=datacapteur_copy['temp']+0.555*datacapteur_copy['c']
    return datacapteur_copy
