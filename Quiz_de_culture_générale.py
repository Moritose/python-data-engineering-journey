# Quiz de culture générale et informatique (version avec liste + boucle)

questions = [
    {
        "question": "Quelle est la capitale de l'Australie ?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
        "reponse": "C"
    },
    {
        "question": "Combien de continents y a-t-il sur Terre ?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "reponse": "C"
    },
    {
        "question": "Qui a peint la Joconde ?",
        "options": ["A. Vincent van Gogh", "B. Léonard de Vinci", "C. Pablo Picasso", "D. Claude Monet"],
        "reponse": "B"
    },
    {
        "question": "En quelle année a eu lieu la Révolution française ?",
        "options": ["A. 1789", "B. 1799", "C. 1804", "D. 1815"],
        "reponse": "A"
    },
    {
        "question": "Quel est le symbole chimique de l'or ?",
        "options": ["A. Ag", "B. Au", "C. Fe", "D. Or"],
        "reponse": "B"
    },
    {
        "question": "Combien de joueurs y a-t-il dans une équipe de football sur le terrain ?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "reponse": "C"
    },
    {
        "question": "Quelle planète est surnommée la 'planète rouge' ?",
        "options": ["A. Vénus", "B. Jupiter", "C. Mars", "D. Saturne"],
        "reponse": "C"
    },
    {
        "question": "Qui a écrit 'Les Misérables' ?",
        "options": ["A. Émile Zola", "B. Victor Hugo", "C. Albert Camus", "D. Molière"],
        "reponse": "B"
    },
    {
        "question": "Quelle est la monnaie officielle du Japon ?",
        "options": ["A. Le yuan", "B. Le won", "C. Le yen", "D. Le ringgit"],
        "reponse": "C"
    },
    {
        "question": "Quel est le plus long fleuve du monde ?",
        "options": ["A. Le Nil", "B. L'Amazone", "C. Le Mississippi", "D. Le Yangtsé"],
        "reponse": "A"
    },
    {
        "question": "Quelle est la complexité temporelle moyenne d'une recherche dans une table de hachage ?",
        "options": ["A. O(n)", "B. O(log n)", "C. O(1)", "D. O(n log n)"],
        "reponse": "C"
    },
    {
        "question": "Dans Git, que fait 'git rebase' par rapport à 'git merge' ?",
        "options": [
            "A. Elle supprime définitivement l'historique des commits",
            "B. Elle réécrit l'historique en appliquant les commits d'une branche par-dessus une autre",
            "C. Elle synchronise automatiquement le dépôt distant sans intervention",
            "D. Elle sert uniquement à résoudre les conflits de fichiers binaires"
        ],
        "reponse": "B"
    },
    {
        "question": "Quel type de jointure SQL retourne uniquement les lignes ayant une correspondance dans les deux tables ?",
        "options": ["A. LEFT JOIN", "B. RIGHT JOIN", "C. INNER JOIN", "D. FULL OUTER JOIN"],
        "reponse": "C"
    },
    {
        "question": "Dans un graphe orienté acyclique (DAG), quel algorithme permet d'obtenir un ordre d'exécution valide des tâches ?",
        "options": ["A. Recherche binaire", "B. Tri topologique", "C. Algorithme de Dijkstra", "D. Tri à bulles"],
        "reponse": "B"
    },
    {
        "question": "Que signifie l'acronyme ACID en base de données ?",
        "options": [
            "A. Atomicity, Consistency, Isolation, Durability",
            "B. Access, Control, Integrity, Data",
            "C. Asynchronous, Cache, Index, Distribution",
            "D. Aggregation, Concurrency, Indexing, Deployment"
        ],
        "reponse": "A"
    },
    {
        "question": "Quelle est la principale différence entre une image et un conteneur Docker ?",
        "options": [
            "A. Il n'y a aucune différence",
            "B. Une image est un modèle statique, un conteneur est une instance en cours d'exécution",
            "C. Une image ne peut contenir qu'un seul fichier",
            "D. Un conteneur est stocké sur Docker Hub, une image est stockée localement"
        ],
        "reponse": "B"
    },
    {
        "question": "Quelle structure de données est la plus adaptée pour implémenter un parcours en largeur (BFS) ?",
        "options": ["A. Une pile (stack)", "B. Une file (queue)", "C. Un tableau trié", "D. Un arbre binaire de recherche"],
        "reponse": "B"
    },
    {
        "question": "Dans un pipeline CI/CD avec GitHub Actions, à quoi sert un 'runner' ?",
        "options": [
            "A. C'est un langage de script propre à GitHub",
            "B. C'est une machine virtuelle ou un conteneur qui exécute les jobs du workflow",
            "C. C'est un outil de gestion des branches Git",
            "D. C'est le nom donné au fichier de configuration YAML"
        ],
        "reponse": "B"
    },
    {
        "question": "Quelle est la complexité temporelle du tri rapide (quicksort) dans le pire des cas ?",
        "options": ["A. O(n log n)", "B. O(n)", "C. O(n²)", "D. O(log n)"],
        "reponse": "C"
    },
    {
        "question": "En Python, que retourne pandas.merge() par défaut lorsqu'on ne précise pas le paramètre 'how' ?",
        "options": ["A. Un outer join", "B. Un left join", "C. Un inner join", "D. Un right join"],
        "reponse": "C"
    },
]


def Quiz():
    print("Bienvenue dans le quiz de culture générale.")
    print("Vous allez répondre à une série de questions à choix multiples (A, B, C ou D) : tapez la lettre correspondant à votre réponse, et votre score s'affichera à la fin.")

    note = 0

    for i, q in enumerate(questions, start=1):
        print(f"\n{i}. {q['question']}")
        for option in q["options"]:
            print(option)
        reponse_utilisateur = input("Votre réponse : ")

        if reponse_utilisateur.upper() == q["reponse"]:
            note += 1
            print("Bonne réponse !")
        else:
            print(f"Mauvaise réponse, la bonne réponse était : {q['reponse']}")
        print(f"-----Note: {note} -----")

    print(f"\nQuiz terminé ! Vous avez obtenu {note} bonne(s) réponse(s) sur {len(questions)}.")


Quiz()