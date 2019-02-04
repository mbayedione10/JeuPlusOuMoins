#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
   //main pour la somme et la moyenne  des valeurs d'un tableau
    int somme,tab [3] = {10,5,3};
    //int tableau[4] = {15,81,22,13};
    double moy;
    somme = sommeTableau(tab,3);
    printf("la somme est %d\t\n", somme);
    moy = moyenneTableau(tab,3);
    printf("la moyenne est %.2f\t", moy);


    return 0;
}
*/

int continuerPartie()
{
    int a;
    printf("\nvoulez vous continuer? (0:non) (1:oui)\n");
    scanf("%d", &a);
    return a;
}
void menu ()
{
    printf("\t1 = un nombre entre 1 et 100\n ");
    printf("\t2 = un nombre entre 1 et 1000\n ");
    printf("\t3 = un nombre entre 1 et 10000\n ");
}

void PlusOuMoins(int maxi, int mini)
{
    int a,nombreMystere = 0,cpt = 1;
    //MAX=100,MIN=1;
    srand(time(NULL));
    nombreMystere = (rand()%(maxi - mini + 1)) + mini;
    do
    {

        printf("Donner un nombre svp:\t");
        scanf("%i",&a);

        if (a==nombreMystere)
        {
            printf("Bravo, vous avez trouve le nombre mystere en %d coups\n",cpt);
        }
        else
        {
            if (a>nombreMystere)
            {
                printf("le nombre mystere est inferieur\n");
            }
            else
            {
                printf("le nombre mystere est superieur\n");
            }
        }
        cpt = cpt+1;
    }while (a!=nombreMystere);
}

// calcul de la somme des valeurs d'un tableau
int sommeTableau (int tableau[], int tailleTableau)
{
    int somme =0,i=0;
    for  (i = 0;i<tailleTableau; i++)
    {
        somme = somme + tableau[i];
       // i = i+1;

    }
    return  somme;
}
