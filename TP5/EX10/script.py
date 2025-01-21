import csv
import os

FICHIER_CONTACTS = "contacts.csv"

# 1. Fonction pour ajouter un contact
def ajouter_contact():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    telephone = input("Téléphone : ")
    
    with open(FICHIER_CONTACTS, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nom, prenom, telephone])
    
    print(f"Contact {nom} ajouté avec succès !")

# 2. Fonction pour afficher tous les contacts
def afficher_contacts():
    if not os.path.exists(FICHIER_CONTACTS):
        print("Aucun contact enregistré.")
        return
    
    with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = list(reader)
    
    if contacts:
        print("\n Liste des contacts :")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact[0]} {contact[1]} - {contact[2]}")
    else:
        print("Aucun contact trouvé.")

# 3. Fonction pour rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Entrez le nom à rechercher : ").strip().lower()
    
    with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = [contact for contact in reader if contact[0].strip().lower() == nom_recherche]
    
    if contacts:
        print("\n Résultats de la recherche :")
        for contact in contacts:
            print(f"{contact[0]} {contact[1]} - {contact[2]}")
    else:
        print("Aucun contact trouvé avec ce nom.")

# 4. Fonction pour supprimer un contact
def supprimer_contact():
    nom_supprime = input("Entrez le nom du contact à supprimer : ").strip().lower()
    
    with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = list(reader)
    
    contacts_modifies = [contact for contact in contacts if contact[0].strip().lower() != nom_supprime]

    if len(contacts) == len(contacts_modifies):
        print("Aucun contact trouvé avec ce nom.")
        return
    
    with open(FICHIER_CONTACTS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(contacts_modifies)
    
    print(f"Contact {nom_supprime} supprimé avec succès !")

# 5. Menu principal
def menu():
    while True:
        print("\n Gestion des Contacts")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Lancer le programme
menu()
