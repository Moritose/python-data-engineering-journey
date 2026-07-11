def commande():
    liste = []
    # Menu principal

    print("Choisissez parmi les 5 options")
    print("____________________________________________________")

    print("Choisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

    while True:
        try:
            choix = int(input("Votre choix : "))

            if choix == 1:
                # Ajout d'un élément à la liste
                ajoute = str(input("Entrez l'élément à ajouter : "))
                liste.append(ajoute)
                print(f"L'élément {ajoute} a bien été ajouté à la liste.")

            elif choix == 2:
                # Retrait d'un élément de la liste
                retire = str(input("Entrez l'élément à retirer : "))
                liste.remove(retire)
                print(f"L'élément {retire} a bien été retiré de la liste.")

            elif choix == 3:
                # Affichage de la liste avec son index
                for i in range(len(liste)):
                    print(f"{i}: {liste[i]}")

            elif choix == 4:
                # Vidage complet de la liste
                liste.clear()
                print("La liste a été vidée.")

            elif choix == 5:
                # Sortie de la boucle et fin du programme
                print("À bientôt")
                break

            else:
                print("Veuillez suivre correctement les instructions.")

        except ValueError:
            print("Entrez un nombre valide.")


commande()