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

def MAX(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    a=data.loc[data.index[0],caractéristique]
    for index,row in data.iterrows():
        if row[caractéristique]>a:
            a=row[caractéristique]
    return a

def MIN(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    a=data.loc[data.index[0],caractéristique]
    for k in range(data.index[0],data.index[0]+len(data)):
        if data.loc[k,caractéristique]<a:
            a=data.loc[k,caractéristique]
    return a

def MOYENNE(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    moy=0
    data=data.loc[data['id']==capteur]
    for index,row in data.iterrows():
        moy+=row[caractéristique]
    moy=moy/data.shape[0]
    return moy

def VARIANCE(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    var=0
    moy=MOYENNE(fichier,caractéristique,capteur)
    data=data.loc[data['id']==capteur]
    for index,row in data.iterrows():
        var+=(row[caractéristique]-moy)**2
    var=var/data.shape[0]
    return var

def MEDIANE(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    datatrié=data.sort_values(by=[caractéristique])
    n=len(data)
    if n%2==0:
        med=(datatrié['temp'][int((data.index[0]+n)/2)]+datatrié['temp'][int((data.index[0]+n)/2)+1])/2
    else:
        med=datatrié['temp'][int((data.index[0]+n)/2)]
    return med

def affichercourbes(caractéristique,capteurr):
    data_capteur=data.loc[data['id']==capteurr]
    plt.plot_date(matplotlib.dates.date2num(convertion(capteurr)),data_capteur[caractéristique],linestyle="-")
    plt.title (caractéristique+" as a function of time")
    plt.xlabel ("date",fontsize=9)
    plt.ylabel ("temperature",fontsize=9)
    plt.xticks(rotation='vertical')
    l1=plt.axhline(y=MIN(fichier,caracteristique,capteurr),label='minimum',color='red')
    l2=plt.axhline(y=MAX(fichier,caracteristique,capteurr),label='maximum',color='pink')
    l3=plt.axhline(y=MOYENNE(fichier,caracteristique,capteurr),label='maximum',color='magenta')
    plt.legend([l1,l2,l3], ['minimum', 'maximum', 'moyenne'],loc = 'upper right',frameon = True, title = 'Legende')
    # plt.legend('variance=VARIANCE(fichier,caracteristique,capteurr)')
    plt.show()
