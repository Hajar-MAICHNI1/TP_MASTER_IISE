#Ouverture de Fichier
#fichier=open("TP5/exemple.txt", "r" )

with open("TP5/exemple.txt", "r")as fichier:
    ligne = fichier.readline()
    #Affiche chaque ligne du texte avec son numéro
    for index, ligne in enumerate(fichier, start=1):
         print(f"{index}: {ligne.strip()}")