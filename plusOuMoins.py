import random


def continuer_partie():
    print("Voulez vous continuer? (0:non) (1:oui)")
    a = int(input())
    return a


def plus_ou_moins(player):
    """
    L'ordinateur tire au sort un nombre entre 1 et 100.
    Il vous demande de deviner le nombre.
    Vous entrez donc un nombre entre 1 et 100.
    L'ordinateur compare le nombre que vous avez entré avec le nombre « mystère »
    qu'il a tiré au sort. Il vous dit si le nombre mystère est supérieur
    ou inférieur à celui que vous avez entré.
    Puis l'ordinateur vous redemande le nombre. …
    il vous indique si le nombre mystère est supérieur ou inférieur.
    Et ainsi de suite, jusqu'à ce que vous trouviez le nombre mystère.
    :param player: le nom du joueur
    :return:
    """
    print("Tour de ", player)
    nombre_mystere = random.randint(0, 100)  # random integer in range [0, 100]
    cpt = 1     # compteur  qui incrémente à chaque fois que vous passez dans la boucle
    guessing = 1
    print("Donner un nombre svp:\t")
    while guessing == 1:
        guess = int(input())
        if guess == nombre_mystere:
            print(player + " a trouvé le nombre mystere en ", cpt, "coups\n")
            guessing = 0
        else:
            if guess < nombre_mystere:
                print("le nombre mystere est superieur a ", guess)
            else:
                print("le nombre mystere est inferieur a ", guess)
            cpt = cpt+1
    return cpt


def joueur():
    """
    Creer les differents joueurs
    :return:
    """
    name = input("entrer le nom et prenom du joueur SVP: ")
    return name


def jeu():
    """
    Le but du jeu, bien sûr, est de trouver le nombre mystère en un minimum de coups.
    Celui qui ttrouve avec moins de coups gqgne le jeu
    :return:
    """
    joueur1 = joueur()
    joueur2 = joueur()
    compteur1 = plus_ou_moins(joueur1)
    compteur2 = plus_ou_moins(joueur2)

    if compteur1 < compteur2:
        print("*"*55)
        print("Bravo!!!", joueur1, " a gagné en ", compteur1, " coups")
        print("*" * 55)
    else:
        print("*" * 55)
        print("Bravo!!!", joueur2, " a gagné en ", compteur2, " coups")
        print("*" * 55)


jeu()
