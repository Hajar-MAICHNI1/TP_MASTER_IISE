import os
from datetime import datetime
import math

# Afficher le répertoire courant
repertoire_courant = os.getcwd()
print("Répertoire courant :", repertoire_courant)

# Afficher la date et l'heure actuelles
date_actuelle = datetime.now()
print("Date et heure actuelles :", date_actuelle.strftime("%Y-%m-%d %H:%M:%S"))

# Calculer la racine carrée d'un nombre 
nombre = float(input("Tapez un nombre : "))
racine_carre = math.sqrt(nombre)
print(f"La racine carrée de {nombre} est {racine_carre:.2f}.")
