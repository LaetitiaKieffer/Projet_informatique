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
