nom_fichier = 'inexistant.txt'

try:
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
except Exception as e:
    print(f"Une erreur s'est produite lors de l'ouverture du fichier : {e}")
