# Quiz de culture générale

## Objectif du projet

Ce projet est volontairement simple. L'idée est de manipuler les mêmes briques de base que dans un jeu plus complexe (poser une question, vérifier une réponse, compter un score) mais **sans avoir plusieurs états à suivre en même temps**.


## Règles du jeu

Le jeu pose une série de questions à l'utilisateur, l'une après l'autre.

Chaque question a exactement une bonne réponse.

Pour chaque question :

1. La question s'affiche à l'écran, avec plusieurs propositions de réponse (par exemple A, B, C, D).
2. L'utilisateur tape la lettre correspondant à sa réponse.
3. Le programme vérifie si la réponse est correcte.
4. Si la réponse est correcte, le score augmente de 1 point et un message de confirmation s'affiche ("Bonne réponse !").
5. Si la réponse est incorrecte, le score n'augmente pas, et le programme affiche la bonne réponse ("Mauvaise réponse, la bonne réponse était : ...").

Une fois que toutes les questions ont été posées, le jeu s'arrête et affiche le score final, sous la forme :

"Vous avez obtenu X bonnes réponses sur Y."


## Étapes suggérées pour construire le projet

Voici une progression logique, à faire dans cet ordre :

1. **Une seule question, sans compter le score.** Affiche une question, demande une réponse, dis juste si c'est correct ou non. Rien d'autre. L'objectif ici est juste de vérifier que tu sais comparer la réponse de l'utilisateur à la bonne réponse.

2. **Une seule question, avec un score.** Reprends l'étape précédente, mais ajoute l'idée de score : s'il répond juste, le score passe à 1. Affiche le score à la fin.

3. **Plusieurs questions, une par une, écrites "en dur".** Répète manuellement le même mécanisme pour 3 ou 4 questions différentes, les unes après les autres. Le score doit s'additionner au fil des questions.

4. **Affichage du score final.** Une fois toutes les questions posées, affiche un message récapitulatif clair avec le score total.

5. *(Optionnel, pour aller plus loin une fois que tout fonctionne)* Range tes questions et réponses dans une structure de données organisée, puis fais parcourir cette structure automatiquement au programme, au lieu d'écrire chaque question "en dur" une par une.

## Conseil de méthode

Ne passe à l'étape suivante que lorsque la précédente fonctionne parfaitement et que tu comprends **pourquoi** elle fonctionne. Ce projet est fait pour être terminé rapidement et proprement, pas pour être impressionnant. L'objectif est de renforcer les bases (conditions, comparaison, comptage) avant de repartir sur quelque chose de plus ambitieux.

## Pour aller plus loin (une fois ce projet terminé)

Une fois que ce quiz fonctionne bien, tu peux revenir au projet de jeu de rôle avec plus de confiance : les mécanismes de base (poser une question, lire une réponse, comparer, mettre à jour un compteur) seront les mêmes, tu n'auras qu'à les combiner avec plus d'éléments à suivre en même temps.