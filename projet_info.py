def calcul_min(fichier):
    data=pd.read_csv(fichier,delimiter=';')
    a=0
    for i in data[:].min():
        if a>i: 
            a=i
        return a
            


