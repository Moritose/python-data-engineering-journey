Projet : Trier automatiquement des fichiers selon leur extension

Dans ce projet, vous allez développer un programme Python capable de classer automatiquement des fichiers en fonction de leur extension (par exemple : .pdf, .jpg, .png, .mp3, .mp4, .docx, etc.).

L'objectif est de parcourir un dossier, d'identifier le type de chaque fichier, puis de le déplacer dans un sous-dossier correspondant à son extension. Par exemple :

Les fichiers .pdf seront déplacés dans un dossier PDF.
Les fichiers .jpg et .png seront déplacés dans un dossier Images.
Les fichiers .mp3 seront déplacés dans un dossier Musique.
Les fichiers .mp4 seront déplacés dans un dossier Vidéos.
Les fichiers .docx seront déplacés dans un dossier Documents.

Ce type de programme est très pratique au quotidien. Par exemple, vous pouvez l'exécuter régulièrement dans votre dossier Téléchargements afin de garder vos fichiers bien organisés sans avoir à les ranger manuellement.

Objectifs pédagogiques

Ce projet vous permettra de mettre en pratique plusieurs notions fondamentales de Python :

la manipulation des fichiers et des dossiers ;
les boucles (for) ;
les conditions (if, elif, else) ;
les dictionnaires pour associer des extensions à des catégories ;
les fonctions afin de rendre le code plus lisible ;
la gestion des exceptions (try / except) pour éviter les erreurs lors du déplacement des fichiers.
Utilisation de pathlib

Pour réaliser ce projet, il est recommandé d'utiliser la bibliothèque pathlib, intégrée à Python. Elle permet de manipuler les chemins de fichiers de manière plus simple, plus lisible et plus moderne que le module os.

Grâce à pathlib, vous pourrez notamment :

parcourir facilement le contenu d'un dossier ;
récupérer le nom ou l'extension d'un fichier ;
vérifier si un chemin correspond à un fichier ou à un dossier ;
créer des dossiers s'ils n'existent pas encore.

Vous constaterez que cette bibliothèque rend le code plus clair et plus intuitif.

Fonctionnement attendu

À la fin du projet, votre programme devra être capable de :

sélectionner un dossier à organiser ;
parcourir tous les fichiers présents dans ce dossier ;
identifier l'extension de chaque fichier ;
créer automatiquement les dossiers nécessaires si ceux-ci n'existent pas ;
déplacer chaque fichier dans le dossier correspondant à son type ;
afficher un message indiquant les fichiers déplacés ou signaler les éventuelles erreurs.