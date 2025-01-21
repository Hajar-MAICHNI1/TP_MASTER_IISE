import os
import shutil

# Création du fichier "journal.txt" 
with open("journal.txt", "w") as file:
    file.write("Ceci est une entrée de journal.\nDeuxième ligne du journal.")

# Copie du fichier "journal.txt" vers "journal_copie.txt"
shutil.copy("journal.txt", "journal_copie.txt")

# Création du dossier "archives" 
if not os.path.exists("archives"):
    os.makedirs("archives")

# Déplacement de "journal_copie.txt" dans le dossier "archives"
shutil.move("journal_copie.txt", os.path.join("archives", "journal_copie.txt"))

print("Opérations terminées avec succès !")
