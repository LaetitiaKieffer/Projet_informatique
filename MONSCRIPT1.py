LK

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#'/Users/laetitia/Desktop/Projet_informatique/donnees_projet.csv'

def MONSCRIPT1(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    for id in data:
        plt.plot(data.sent_at,data.temp)
    plt.show()


data1=data[data['id']==1]

09/11/20
JV

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("C:/EIVP")

data=pd.read_csv("EIVP_KM.csv",sep='/;')

sent_at,temp=data['sent_at'],data['temp']

plt.plot(sent_at,temps,"+",label="temperature en fonction du temps")
plt.xlabel ("date",fontsize=5)
plt.ylabel ("temperature",fontsize=8)
plt.xticks(rotation='vertical')
plt.legend()

plt.show()