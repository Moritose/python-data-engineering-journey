# Niveau 1 : Manipulation de base

fruits= ["pomme", "banane", "orange", "kiwi", "mangue"]
print(fruits[0])
print(fruits[0:3])
print(fruits[4])
fruits.append("fraise")
print(fruits)
fruits.insert(0,"citron")
fruits.remove("kiwi")
print(fruits)

# Niveau 2 : Calculs et logique
notes = [12, 15, 8, 19, 6, 14]
longeur=len(notes)
print(longeur)
for note in notes:
    print(f"Note: {note}")
    
from statistics import mean

moyenne_notes = mean(notes)
somme_notes = sum(notes)
print(f"Somme de notes: {somme_notes}")
print(f"Moyenne de notes: {moyenne_notes}")

note_haute= notes[0]
note_bas=notes[0]
for note in notes:
    if note_haute<note:
        note_haute=note
        
    if note_bas>note:
     note_bas=note
    
    
print(f"la note la plus bas: {note_haute}")
print(f"la note la plus haute:{note_bas}")
notes_admises=[]
for liste_note in notes:
    if liste_note>=10:
        notes_admises.append(liste_note)
        
print(notes_admises)
nb_etudiant= len(notes_admises)
print(f"Nombre d'élèves qui ont eu la moyenne: {nb_etudiant}")


prenoms = ["Ali", "Sara", "Omar", "Leila", "Yassin"]
pre= input("Veuillez rentrer votre nom: ")
if pre in prenoms:
    print("Trouvé")
else:
    print("Pas trouvé")
    
    
# Niveau 3 : Manipulation avancée
ages = [34, 12, 56, 23, 8, 45, 19]





langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[0][0]# entrez le code ici
print(langages[0][0])
print(nombres[0:][0])
# deux = nombres[2][0][1]# entrez le code ici
# sept = # entrez le code ici



fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    if fruit == '🍏':
        continue  # On ignore la pomme et on passe à l'itération suivante
    print(f"Je prépare un jus avec : {fruit}")

print("Mon cocktail de fruits est prêt !")

users=['Utilisateur1','Utilisateur2','Utilisateur3','Utilisateur4','Utilisateur5','Utilisateur6','Utilisateur7','Utilisateur8','Utilisateur9','Utilisateur10']
for i in users:
    print(i)
    
    
    
mot="Python"
for i in reversed(mot):
    
    print(f"Reverse: {i}")

mot = "Python"

for i in range(len(mot)):
   print(f"{i}") 
    
    
nombre=7
for i in range(11):
    print(f"{nombre} x {i} = {i*nombre}")
    i+=1
    
    
i = 0

while i < 10:
    resultat = "Exercice réussi !"
    print(resultat)
    i+=1
    pass    
	
reponse = 1
while reponse ==0:
    print("On continue !")
    rep=input("voulez-vous sortie? (1/0)")
    if rep!=1:
        break
        
        
nombres = range(51)
nombres_pairs = [pair for pair in nombres if pair%2==0]
print(f"Nombres pairs: {nombres_pairs}")




while True:
    try:
        nb=int(input("Entrez un premier nombre: "))
        nb_1=int(input("Entrez un deuxieme nombre: "))
        print(f"{nb} + {nb_1} = {nb+nb_1}")
        break
    except ValueError:
        print("Veuillez entrez un nombre valide.")
    
    
    

