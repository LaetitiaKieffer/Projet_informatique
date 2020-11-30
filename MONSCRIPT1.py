#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from datetime import datetime

#import tableau excel Laetitia
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

#import tableau excel Joséphine
os.chdir("C:/EIVP")
fichier="EIVP_KM.csv"
data=pd.read_csv(fichier,delimiter=';')

def convertion(capteur):
    L=len(data[data.id==capteur])
    Liste=[]
    for k in range(L):
        Liste.append(datetime.strptime(data.sent_at.loc[k+data[data.id==capteur].index[0]],"%Y-%m-%d %H:%M:%S+02:00"))
    return Liste
#print (convertion(1))


#convertion avec un tableau
def convertion_dataframe(fichier,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    data['sent_at_converti'] = datetime.strptime(data.loc['sent_at'],"%Y-%m-%d %H:%M:%S+02:00")
    return data

#essai moyenne
def MOYENNE(fichier,caractéristique,capteur,start_date,end_date):
    data=pd.read_csv(fichier,delimiter=';')
    moy=0
    data=data.loc[data['id']==capteur]
    L=convertion(capteur)
    start_date_converti=datetime.strptime(start_date,"%Y-%m-%d")
    end_date_converti=datetime.strptime(end_date,"%Y-%m-%d")
    data=data.loc[start_date_converti<=L[i]<=end_date_converti]
    for index,row in data.iterrows():
        moy+=row[caractéristique]
    moy=moy/data.shape[0]
    return moy

def affichercourbes(caracteristique,capteurr):
    data_capteur=data.loc[data['id']==capteurr]
    plt.plot_date(matplotlib.dates.date2num(convertion(capteurr)),data_capteur[caracteristique],linestyle='-',marker=None)
    plt.title (caracteristique+" as a function of time")
    plt.xlabel ("date",fontsize=9)
    plt.ylabel ("temperature",fontsize=9)
    plt.xticks(rotation='vertical')
    plt.show()

def affichertteslescourbes(caracteristique):
    for k in range (1,7):
        affichercourbes(caracteristique,k)