import random


def nombre_mystere():
    print("NB : Vous avez 3 chances pour trouver le nombre mystère")

    nombre_min = 1
    nombre_max = 100
    nb_mystere = random.randint(nombre_min, nombre_max)

    for i in range(1, 4):
        # print(f"Le nombre mystère est : {nb_mystere}")  # à décommenter pour débugger

        choix = int(input("Veuillez choisir un nombre entre 1 et 100 : "))

        if choix > nb_mystere:
            print("Le nombre mystère est plus petit.")
        elif choix == nb_mystere:
            print("Bravo ! Vous avez trouvé le nombre mystère.")
            break
        else:
            print("Le nombre mystère est plus grand.")

        # Calcul des essais restants APRÈS la tentative
        essais_restants = 3 - i

        if choix == nb_mystere:
            pass  # déjà géré au-dessus avec le break
        elif essais_restants == 0:
            print("Vous avez perdu.")
            print(f"Le nombre mystère était {nb_mystere}")
        elif essais_restants == 1:
            print(f"Il vous reste {essais_restants} essai.")
        else:
            print(f"Il vous reste {essais_restants} essais.")


nombre_mystere()