#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "C:\Users\mamadoumbaye\Desktop\IG IT\Langage C\OpenClassroom\bibliotheque\plusOumoins.h"



int main()
{
    int choix;
    do
    {
        menu();
        scanf("%d",&choix);
        switch (choix)
        {
            case 1:
                 PlusOuMoins(100,1);
                break;

            case 2:
                PlusOuMoins(1000,1);
                break;
            case 3:
                PlusOuMoins(10000,1);
                break;
            default : printf("entrer un nombre entre 1 et 3 svp");
        }
    }while (continuerPartie() == 1);
    return 0;
}
