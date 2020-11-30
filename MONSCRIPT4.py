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
    a=a/len(data)
    cov=a/(b*c)
    return cov

def representation_correlation_entre_deux_variables(fichier,caractéristique1,caractéristique2,capteur):
    data_capteur=data.loc[data['id']==capteur]
    fig, ax1 = plt.subplots()
    color1='teal'
    color2='goldenrod'
    ax1.plot_date(matplotlib.dates.date2num(convertion(capteur)),data_capteur[caractéristique1],linestyle='-',marker=None,color=color1)
    ax1.set_xlabel('date',fontsize=9,color=color1)
    ax1.tick_params(axis='x',rotation=90)
    ax1.tick_params(axis='y',labelcolor=color1)
    ax1.set_ylabel(caractéristique1,fontsize=9,color=color1)
    ax2=ax1.twinx()
    ax2.plot_date(matplotlib.dates.date2num(convertion(capteur)),data_capteur[caractéristique2],linestyle='-',marker=None,color=color2)
    ax2.set_ylabel(caractéristique2,fontsize=9,color=color2)
    ax2.tick_params(axis='x',rotation=90)
    ax2.tick_params(axis='y',labelcolor=color2)
    LegendeCorrelation=matplotlib.patches.Rectangle((0,0),0,0,color='white')
    plt.title (caractéristique1+" et "+caractéristique2+" en fonction du temps")
    plt.legend([LegendeCorrelation], [CORRELATION(fichier,caractéristique1,caractéristique2,capteur)],loc ='upper right',frameon = True, title = 'indice de corrélation')
    plt.show()
