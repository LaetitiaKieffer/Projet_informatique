#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from datetime import datetime

#import tableau excel Joséphine
os.chdir("C:/EIVP")
fichier="EIVP_KM.csv"
data=pd.read_csv(fichier,delimiter=';')

#import tabeau excel Laetitia
fichier='/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv'
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

def MAX(fichier,caractéristique,capteur):
    data =pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    a=data.loc[data.index[0],caractéristique]
    for index,row in data.iterrows():
        if row[caractéristique]>a:
            a=row[caractéristique]
    return a

def MIN(fichier,caractéristique,capteur):
    data =pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    a=data.loc[data.index[0],caractéristique]
    for k in range(data.index[0],data.index[0]+len(data)):
        if data.loc[k,caractéristique]<a:
            a=data.loc[k,caractéristique]
    return a

def MOYENNE(fichier,caractéristique,capteur):
    data =pd.read_csv(fichier,delimiter=';')
    moy=0
    data=data.loc[data['id']==capteur]
    for index,row in data.iterrows():
        moy+=row[caractéristique]
    moy=moy/data.shape[0]
    return moy

def VARIANCE(fichier,caractéristique,capteur):
    data =pd.read_csv(fichier,delimiter=';')
    var=0
    moy=MOYENNE(fichier,caractéristique,capteur)
    data=data.loc[data['id']==capteur]
    for index,row in data.iterrows():
        var+=(row[caractéristique]-moy)**2
    var=var/data.shape[0]
    return round(var,2)

def MEDIANE(fichier,caractéristique,capteur):
    data =pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    datatrie=data.sort_values(by=[caractéristique])
    n=len(data)
    if n%2==0:
        med=(datatrie[caractéristique][int(data.index[0]+(n/2)-1)]+datatrie[caractéristique][int(data.index[0]+n/2)])/2
    else:
        med=datatrie[caractéristique][int(data.index[0]+n/2)]
    return med

def convertion(capteur):
    L=len(data[data.id==capteur])
    Liste=[]
    for k in range(L):
        Liste.append(datetime.strptime(data.sent_at.loc[k+data[data.id==capteur].index[0]],"%Y-%m-%d %H:%M:%S+02:00"))
    return Liste

def afficher_courbes(caracteristique,capteurr):
    fichier="EIVP_KM.csv"
    data_capteur=data.loc[data['id']==capteurr]
    plt.plot_date(matplotlib.dates.date2num(convertion(capteurr)),data_capteur[caracteristique],linestyle="-",marker=None)
    plt.title (caracteristique+" as a function of time")
    plt.xlabel ("date",fontsize=9)
    plt.ylabel ("temperature",fontsize=9)
    plt.xticks(rotation='vertical')
    LegendeVariance=matplotlib.patches.Rectangle((0,0),0,0,color='white')

    l1=plt.axhline(y=MIN(fichier,caracteristique,capteurr),label='minimum',color='mediumvioletred')
    plt.text((datetime.strptime(data.sent_at.loc[data[data.id==capteurr].index[capteurr*200]],"%Y-%m-%d %H:%M:%S+02:00")),MIN(fichier,caracteristique,capteurr),'capteur '+str(capteurr),fontsize = 7,fontweight = 'bold', rotation = 70)

    l2=plt.axhline(y=MAX(fichier,caracteristique,capteurr),label='maximum',color='pink')
    plt.text((datetime.strptime(data.sent_at.loc[data[data.id==capteurr].index[capteurr*200]],"%Y-%m-%d %H:%M:%S+02:00")),MAX(fichier,caracteristique,capteurr),'capteur '+str(capteurr),fontsize = 7,fontweight = 'bold', rotation = 70)

    l3=plt.axhline(y=MOYENNE(fichier,caracteristique,capteurr),label='maximum',color='magenta')
    plt.text((datetime.strptime(data.sent_at.loc[data[data.id==capteurr].index[capteurr*200]],"%Y-%m-%d %H:%M:%S+02:00")),MOYENNE(fichier,caracteristique,capteurr),'capteur '+str(capteurr),fontsize=7,fontweight='bold', rotation=70)

    l4=plt.axhline(y=MEDIANE(fichier,caracteristique,capteurr),label='maximum',color='deeppink')
    plt.text((datetime.strptime(data.sent_at.loc[data[data.id==capteurr].index[capteurr*200]],"%Y-%m-%d %H:%M:%S+02:00")),MEDIANE(fichier,caracteristique,capteurr),'capteur '+str(capteurr),fontsize = 7,fontweight = 'bold', rotation = 70)

    plt.legend([l1,l2,l3,l4,LegendeVariance], ['minimum','maximum','moyenne','médiane','variance='+str(VARIANCE(fichier,caracteristique,capteurr))],loc ='upper right',frameon = True, title = 'Legende')


    plt.show()
