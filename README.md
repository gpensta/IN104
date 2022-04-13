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

Concernant la gestion de projet, j'ai ajouté des éléments aux slides ainsi qu'au descriptif détaillé. Un Makefile générique est par ailleurs disponible. 
Si vous souhaitez importer/télécharger ces modifications et que vous avez cloné gpensta/IN104, il vous suffit d'effectuer la commande `git pull` ou `git pull origin master`. 

Concernant l'objectif de la séance du 29 mars, si vous ne savez pas quels arguments spécifier dans la fonction STFT, les lignes 30 - 56 de https://github.com/Steboss/music_retrieval/blob/master/stft/installer/stft.pyx vous éclairent. 

**Objectifs** : Compresser le tableau des STFT en un vecteur 1D en prenant la moyenne et l'écart-type (selon l'axe des fréquences ou selon l'axe du temps) et écrire ce vecteur dans un fichier csv précédé du label correspondant au genre musical représenté par le son encodé (entier compris entre 0 et 9, e.g. blues := 0, metal := 6, rock := 9). Par exemple, pour du classique, nous devrions écrire la ligne suivante :

```
1; mu_1; sigma_1; ...; ...; mu_n, sigma_n;
```

Afin de contenir le temps de calcul pour l'optimisation du classifieur tout en préservant une certaine précision, le vecteur sera d'une dimension d'environ 512.

Penser à organiser votre code en plusieurs fichiers de modules (*.c et *.h), à compiler le projet avec un Makefile et à mettre à jour le tableau d'avancement.

Voici un exemple d'organisation : 

```
├── README.md
├── Makefile
└── src
    ├── include
    │   ├── audioread.c 
    │   ├── audioread.h
    │   ├── encoding.c 
    │   ├── encoding.h
    │   ├── prediction.c
    │   ├── prediction.h
    │   ├── stft.c
    │   ├── stft.h
    │   ├── utils.c (fonctions mathématiques élémentaires (argmax, produit matriciel ... ))
    │   └── utils.h
    └── main.c
```

## Séance du 19 avril

Je l'ai indiqué à beaucoup de groupes lors de la séance du 12 avril, pour les autres groupes les arguments de STFT sont les suivants :

```C
double* stft(double *wav_data, int samples, int windowSize, int hop_size, double *magnitude, int sample_freq, int length)
```

**wav_data** := signal audio en entrée (sortie de audio_read), cette taille vous est donnée par la fonction audioread.

**samples** := la dimension du tableau magnitude (sortie de stft), elle vaut nCols x nRows = int( (length/(windowSize/2))*((windowSize/2)+1)) (c.f ligne 36 de https://github.com/Steboss/music_retrieval/blob/master/stft/installer/stft.pyx).

**windowSize** := la taille de la fenêtre, on peut choisir 512 afin d'avoir un vecteur encodé de taille raisonnable.

**hop_size** := facteur de recouvrement, 512 (les fenêtres seront disjointes car de la taille de **windowSize**).

**magnitude** := sortie de la STFT, il s'agit d'un vecteur 1D de **samples** elements, il représente un tableau 2D où nCols := (length/(windowSize/2)) et nRows = ((windowSize/2)+1)) (c.f. construction de la variable **samples**). On peut accéder à l'élément (i, j) de ce tableau en prenant l'élément en position i * nCols + j de **magnitude**. 

**sample_freq** := fréquence d'échantillonage du signal dans notre base de donnée, elle est de 22050 Hz.

**length** := nombre d'échantillons contenus dans le signal audio i.e. taille de **wav_data**.

### Objectifs de la séance

Terminer les tâches du 12 avril. Valider votre case dans le tableau d'avancement.
Quand cela est terminé, encoder les 1000 fichiers audios de la base de données dans le fichier csv : une ligne par son. 

## Séance du 3 Mai