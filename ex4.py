from ex1 import val_max
import matplotlib.pyplot as plt

def histo(liste:list) -> list:
    """
    Fonction qui a partir d'une liste de valeur en paramètre,
    retourne les valeurs d'un histogramme avec en abscice l'index
    de l'élément et la quantité en ordonnée

    Args:
        liste (list): liste contenant série de nombre a analyser

    Returns:
        list: retourne une liste "histogramme" avec l'index en abscice et la quantité en ordonnée
    """

    liste_histo = []
    i = 0

    for i in range(max(liste)+1):
        liste_histo.append(0)
    for el in liste:
        liste_histo[el] += 1

    return liste_histo

def est_injective(liste:list) -> bool:
    """
    Fonction qui determine si une fonction est injective et retourne un boolen

    Args:
        liste (list): liste comprenant les valeurs d'entree

    Returns:
        bool: True si injective, False sinon
    """

    res = True
    i = 0

    while i < len(liste) and res:
        if liste[i] > 1:
            res = False
        i += 1
    return res

# print(
#     est_injective (
#         histo([3,0,6,7,4,2,1,5])
#     )
# )

def est_surjective(liste:list) -> bool:
    """
    Fonction qui determine si une fonction est surjective et retourne un boolen

    Args:
        liste (list): liste comprenant les valeurs d'entree

    Returns:
        bool: True si surjective, False sinon
    """

    res = True
    i = 0

    while i < len(liste) and res:
        if liste[i] < 1:
            res = False
        i += 1
    return res

# print(
#     est_surjective (
#         histo([3,0,6,7,4,2,1,5])
#     )
# )

def est_bijective(liste:list) -> bool:
    """
    Fonction qui determine si une fonction est bijective et retourne un boolen

    Args:
        liste (list): liste comprenant les valeurs d'entree

    Returns:
        bool: True si bijective, False sinon
    """

    return est_surjective(liste) and est_injective(liste)

# print(
#     est_bijective(
#         histo(
#             [3,0,6,7,4,2,1,5]
#         )
#     )
# )

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
    histo(
        [0,0,0,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,5,5,6,7,7,7,7,7]
    )
)