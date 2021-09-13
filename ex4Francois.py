import matplotlib.pyplot as plt
from ex1 import val_max

def histo(lst_f: list) -> list:
    """fonction permettant de definir l'histogramme a partir de lst_f

    Args:
        lst_f (list): tableau d'entier

    Returns:
        list: histogramme de l'entrée
    """
    lst_h = []
    index_h = 0
    for index in range(len(lst_f)):
        lst_h.append(0)
    while index_h < len(lst_f):
        element_lst_f = lst_f[index_h]
        for value in lst_f:
            if(value == element_lst_f):
                lst_h[index_h] += 1
        index_h += 1
    return lst_h
histo([1,2,3,4,5,6,7,8,9])

def est_injective(lst_f: list) -> bool:
    """fonction permettant de determiner si lst_f est surjective

    Args:
        lst_f (list): tableau d'entier

    Returns:
        bool: si true list_f est injective
    """
    lst_h = histo(lst_f)
    injective = True
    index = 0
    tailleTableau = len(lst_h)
    while(index < tailleTableau and injective):
        if(lst_h[index] > 1):
            injective = False
    return injective


def est_surjective(lst_f: list) -> bool:
    """fonction permettant de determiner si lst_f est surjective

    Args:
        lst_f (list): tableau d'entier

    Returns:
        bool: si true surjective
    """
    lst_h = histo(lst_f)
    surjective = True
    index = 0
    tailleTableau = len(lst_h)
    while(index < tailleTableau and injective):
        if(lst_h[index] < 1):
            injective = False
    return injective


def est_bijective(lst_f: list) -> bool:
    """fonction permettant de determiner si lst_f est bijective

    Args:
        lst_f (list): tableau d'entier

    Returns:
        bool: si true bijective else non bijective
    """
    return (est_surjective(lst_f) and est_injective(lst_f))


def afficheHisto(liste:list) -> None:
    """
    Procédure d'affichage d'un histogramme dans la console
    Args:
        liste (list): histogramme sous forme de liste
    """

    MARGE_HAUTEUR = 2

    structure_tableau = ""
    points_abscice = "---"
    taille_tableau = len(liste)
    caractere_colonne = " "
    valeur_max_liste = val_max(liste)

    print("\nListe : {} \n\n".format(liste))

    for line in range(valeur_max_liste+MARGE_HAUTEUR):  # affichage lignes
        for col in range(taille_tableau):      # creation lignes
            if taille_tableau - line + 1 <= liste[col]: # Si un point doit etre mis
                caractere_colonne = "*"
                if col == taille_tableau - 1:
                    caractere_colonne += " |"
            else:
                caractere_colonne = " "
                if col == taille_tableau - 1:
                    caractere_colonne += " |"

            structure_tableau += " | {}".format(caractere_colonne)

            if line == valeur_max_liste + MARGE_HAUTEUR - 1: # Affichage abscices
                points_abscice += "{}---".format(col)

        print(structure_tableau)
        structure_tableau = ""

    print(points_abscice)

    cpt = 0
    for el in liste:
        plt.bar(cpt,el)
        cpt+=1
    plt.show()

# afficheHisto([3,0,6,7,4,2,1,5])
afficheHisto(
    histo([0,0,0,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,5,5,6,7,7,7,7,7]))