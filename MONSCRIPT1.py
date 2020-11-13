#LK
#import des bibliothèques
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv('/Users/laetitia/Desktop/Projet_informatique_sujet/donnees_projet.csv',delimiter=';')

def GRAPH(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    for i in data['id'].items():
        plt.plot(data['sent_at'],data['temp'])
    plt.show()

def GRAPH2(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    dataconst=data.loc[data['id']==1]
    i=1
    while i < 7:
        datainter=data.loc[data['id']==i]
        i=i+1
        return datainter
        #plt.plot(dataconst['sent_at'],datainter['temp'])
    #plt.show

def GRAPH3(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    dataconst=data.loc[data['id']==1]
    for i in range (1,7):
        data=data.loc[data['id']==i]
        #return dataconst['sent_at']
        #return data['temp'].astype(object)
        plt.plot(dataconst['sent_at'],data['temp'].astype(object))
plt.show




def essai(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    L=[]
    for i in data['id'].items():
        L.append(data.temp)
    return L


data1=data[data['id']==1]

#09/11/20
#JV

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("C:/EIVP")

data=pd.read_csv("EIVP_KM.csv",sep='/;')

sent_at,temp=data['sent_at'],data['temp']

plt.plot(sent_at,temp,"+",label="temperature en fonction du temps")
plt.xlabel ("date",fontsize=5)
plt.ylabel ("temperature",fontsize=8)
plt.xticks(rotation='vertical')
plt.legend()

plt.show()