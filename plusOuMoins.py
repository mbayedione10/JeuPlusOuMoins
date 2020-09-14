"""
jeu « Plus ou moins ».
Le principe est le suivant.
L'ordinateur tire au sort un nombre entre 1 et 100.
Il vous demande de deviner le nombre.
Vous entrez donc un nombre entre 1 et 100.
L'ordinateur compare le nombre que vous avez entré avec le nombre « mystère »
qu'il a tiré au sort. Il vous dit si le nombre mystère est supérieur
ou inférieur à celui que vous avez entré.
Puis l'ordinateur vous redemande le nombre. …
il vous indique si le nombre mystère est supérieur ou inférieur.
Et ainsi de suite, jusqu'à ce que vous trouviez le nombre mystère.
Le but du jeu, bien sûr, est de trouver le nombre mystère en un minimum de coups.
"""

import random

def continuerPartie():
    print("Voulez vous continuer? (0:non) (1:oui)")
    a = int(input())
    return a

def PlusOuMoins():
    print("Nom:")
    nom = input()
    print("Prenom:")
    prenom = input()
    #Return random integer in range [a, b], including both end points
    nombreMystere = random.randint(0, 100)
    #la variable Cpt est un compteur  qui incrémente à chaque fois que vous passez dans la boucle
    cpt = 1
    a = 1
    #La boucle du programme.Elle se repete tant quee lútilisateur n'as pas trouvé le nombre mystere
    while(a==1):
        print("Donner un nombre svp:\t")
        nombre = int(input())
        if(nombre == nombreMystere):
            print("Bravo",prenom +" " + nom ,"!  vous avez trouve le nombre mystere en ", cpt, "coups\n")
            a = 0
        else:
            if(nombre<nombreMystere):
                print("le nombre mystere est superieur a ", nombre)
            else:
                print("le nombre mystere est inferieur a ", nombre)
        cpt = cpt+1





PlusOuMoins()

