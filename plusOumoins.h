#ifndef PLUSOUMOINS_H_INCLUDED
#define PLUSOUMOINS_H_INCLUDED
typedef struct personne
{
    char nom[30];
    char prenom[50];
    int age;
    int homme; //homme=1 et femme=0
    struct personne * suivant;
}Personne;
typedef Personne * suivantPersonne;

int continuerPartie();
void menu ();
void PlusOuMoins(int maxi, int mini);
int sommeTableau (int tableau[], int tailleTableau);
double moyenneTableau(int tableau[], int tailleTableau);


#endif // PLUSOUMOINS_H_INCLUDED
