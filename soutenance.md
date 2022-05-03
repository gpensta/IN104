# Soutenance du 24 mai 2022 de 14 h 45 à 18 h

## Déroulement de la soutenance 

Les soutenances se dérouleront en salle 2413 de 14h45 à 18h, la sortie du vidéo-projecteur vers votre ordinateur est VGA ou HDMI, voir si vous disposez de ces ports sur votre ordinateur.
Un planning de passage est disponible [ici](https://docs.google.com/spreadsheets/d/1x39D_9GIRYmTh7bnlPFFJCIwaDIV3mlcG8qN1mbHVsg/edit?usp=sharing). Je vous conseille d'assister à la présentation de vos collègues.

La durée de la soutenance est de 14' avec 10' maximum de présentation / démo  et 4' de questions.

    * Présentation des solutions techniques et des résultats obtenus, discussion de ces résultats (env. 5')

    * Démonstration en direct, compilation du projet, encodage et prédiction du genre d'un son (env. 4')

Au cours de la soutenance, mettez également en valeur les points indiqués dans le barême indicatif ci-dessous.

## Barème indicatif de notation du projet

### Gestion de projet et présentation : 12 pts

    * Git / GitHub à jour avec un projet compilable sur la branche principale.
      Les fichiers compilés et la base de données ne sont pas suivis sur GitHub ; les instructions de compilation, les tâches accomplies (et éventuellement les tâches restantes à être effectuées) sont indiquées dans `README.md` : 3 pts 

    * Le code est séparé en modules *.h et *.c :  2 pts
    
    * Un Makefile permet de compiler le projet :  2 pts
  
    * Soutenance : clarté des explications et des réponses aux éventuelles questions 5 pts 

### Solution technique proposée : 13 pts

    * Encodage des sons par STFT :  3 pts

    * Calcul des écart-types et moyennes, et écritures des vecteurs dans un fichier CSV :  4 pts 

    * Présentation des résultats de la classification :  2 pts

    * Prédiction de la classe d'un son : 4 pts

    * BONUS si score > 0.7 : + 2 pts

    * BONUS si un autre encodage (MFCC, Batch Normalization), ou un autre algorithme de classification est testé : env. + 2 pts

    * BONUS si tests unitaires : + 1 pt

