#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from datetime import datetime
from datetime import time
import sys

#import tableau excel Laetitia
fichier='/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv'
data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet_informatique.csv',delimiter=';')

#import tableau excel Joséphine
os.chdir("C:/EIVP")
fichier="EIVP_KM.csv"
data=pd.read_csv(fichier,delimiter=';')

#convertion de la colonne 'sent_at' avec création d'une liste
def convertion(capteur):
    L=len(data[data.id==capteur])
    Liste=[]
    for k in range(L):
        Liste.append(datetime.strptime(data.sent_at.loc[k+data[data.id==capteur].index[0]],"%Y-%m-%d %H:%M:%S+02:00"))
    return Liste

#convertion avec un tableau
def convertion_dataframe(fichier,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    data['sent_at_converti']=pd.to_datetime(data['sent_at'])
    return data

#afficher une courbe grâce à la liste convertion obtenue
def affichercourbe(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data_capteur=data.loc[data['id']==capteur]
    plt.plot_date(matplotlib.dates.date2num(convertion(capteur)),data_capteur[caractéristique],linestyle='-',marker=None)
    plt.title (caractéristique+" as a function of time ")
    LegendeCapteur=matplotlib.patches.Rectangle((0,0),0,0,color='white')
    plt.legend([LegendeCapteur], [capteur],loc ='upper right',frameon = True, title = 'capteur numéro')
    plt.xlabel ("date",fontsize=9)
    plt.ylabel (caractéristique,fontsize=9)
    plt.xticks(rotation='vertical')
    plt.show()

#afficher courbe en utilisant un argement en plus dans l'ouverture du fichier csv
def affichercourbe1(fichier,caractéristique,capteur):
    data=pd.read_csv(fichier,delimiter=';',parse_dates=['sent_at'])
    data_capteur=data.loc[data['id']==capteur]
    plt.plot_date(data_capteur['sent_at'],data_capteur[caractéristique],linestyle='-',marker=None)
    plt.title (caractéristique+" as a function of time ")
    LegendeCapteur=matplotlib.patches.Rectangle((0,0),0,0,color='white')
    plt.legend([LegendeCapteur], [capteur],loc ='upper right',frameon = True, title = 'capteur numéro')
    plt.xlabel ("date",fontsize=9)
    plt.ylabel (caractéristique,fontsize=9)
    plt.xticks(rotation='vertical')
    plt.show()

#affichage de tous les capteurs d'une même caractéristique
def affichertteslescourbes(fichier,caractéristique):
    for k in range (1,7):
        affichercourbe(fichier,caractéristique,k)


#___________________________________________________________________BROUILLON__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________________________________________________________-__
#essais de programmes pour pouvoir mettre en entrée start_date et end_date
def affichercourbes1(fichier,caracteristique,capteur,start_date,end_date):
    data=pd.read_csv(fichier,delimiter=';')
    data_capteur=data.loc[data['id']==capteur]
    start_date_converti=datetime.strptime(start_date,"%Y-%m-%d")
    end_date_converti=datetime.strptime(end_date,"%Y-%m-%d")
    data_capteur['sent_at_converti']=datetime.strptime.loc(data_capteur['sent_at'],"%Y-%m-%d %H:%M:%S+02:00")
    #data['sent_at']=pd.to_datetime(data['sent_at']).apply(lambda x: x.replace(time=None))
    data_capteur_selection=data_capteur.loc[start_date_converti<=data['sent_at_converti']<=end_date_converti]
    #data_capteur_selection=data_capteur[data['sent_at'].isin([start_date_converti,end_date_converti])]
    plt.plot_date(data_capteur_selection['sent_at'],data_capteur_selection[caracteristique],linestyle='-',marker=None)
    plt.title (caracteristique+" as a function of time")
    plt.xlabel ("date",fontsize=9)
    plt.ylabel ("temperature",fontsize=9)
    plt.xticks(rotation='vertical')
    plt.show()

#2 programme essayant de convertir la colonne sent_at du dataframe avec la méthode datatime.datetime.strptime
def convertion_dataframe1(fichier,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data=data.loc[data['id']==capteur]
    for index,row in data.iterrows():
        row['sent_at'] = datetime.strptime(row['sent_at'],"%Y-%m-%d %H:%M:%S+02:00")
    return data

def convertion_dataframe2(fichier,capteur):
    data=pd.read_csv(fichier,delimiter=';')
    data_capteur=data.loc[data['id']==capteur]
    for k in range(len(data)):
        data_capteur['sent_at'][k] = datetime.strptime(data_capteur['sent_at'][k],"%Y-%m-%d %H:%M:%S+02:00")
    return data_capteur

