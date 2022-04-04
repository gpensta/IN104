# IN104 : Classifieur de sons

## Objectif :

Produire un programme C compilé permettant d'effectuer une prédiction de genres musicaux. 

## Sources utiles :

Base de données de fichiers audios : http://marsyas.info/downloads/datasets.html (bibliographie https://arxiv.org/pdf/1306.1461.pdf)


Projet permettant d'extraire les STFT d'un son : https://github.com/Steboss/music_retrieval/tree/master/stft

Bibliothèque Python d'algorithmes de classification : https://scikit-learn.org/stable/modules/svm.html#svm-classification

Tableau d'avancement : https://docs.google.com/spreadsheets/d/1iR_tJWAhS-ZisnpE-PrqFb7A_0W4x8w9xwW4t1x4P6A/edit?usp=sharing

## Séance du 22 mars

**Objectifs** : Compréhension du projet et initialisation de Git

Normalement chaque groupe doit avoir initialisé un Git et l'avoir poussé sur Github afin de pouvoir communiquer entre collègues. 

Penser à mettre à jour le tableau d'avancement.

## Séance du 29 mars

**Objectifs** : Lire un fichier audio de issu de la base de données et effectuer sa STFT.

Pour utiliser le script features-encoding/stft.c, il faut avoir installé :

```
sudo apt install libfftw3-dev
sudo apt install fftw3 
```

Penser à lier les bibliothèques -math et fftw3- lors de la compilation :

```
gcc wave.c -Wall -lfftw3 -lm -o wave
```
Penser à mettre à jour le tableau d'avancement.

## Séance du 12 avril

Si vous ne savez pas quels arguments spécifier dans la fonction STFT, les lignes 30 - 56 de https://github.com/Steboss/music_retrieval/blob/master/stft/installer/stft.pyx vous éclairent. 

**Objectifs** : Compresser le tableau des STFT en un vecteur 1D en prenant la moyenne et l'écart-type (selon l'axe des fréquences ou selon l'axe du temps) et écrire ce vecteur dans un fichier csv précédé du label correspondant au genre musical représenté le son encodé (entier compris entre 0 et 9, e.g. blues := 0, metal := 6, rock := 9). Par exemple, pour du classique, nous devrions écrire la ligne suivante :

```
1; mu_1; sigma_1; ...; ...; mu_n, sigma_n;
```

Afin de contenir le temps de calcul pour l'optimisation du classifieur tout en préservant une certaine précision, le vecteur sera d'une dimension d'environ 512.

Penser à mettre à jour le tableau d'avancement.

## Séance du 19 avril