

def position(liste:list,element:int) -> int:
    """Fonction qui renvoie l'index d'un élément dans une liste

    Args:
        liste (list): Liste dans laquelle sera fait la recherche
        element (int): Element a chercher

    Returns:
        int: index de l'élement ou -1 si pas présent
    """
    res = -1
    if len(liste) > 0:
        i = -1
        for el in liste:
            if el == element:
                res = element
            i+=1
    return i

def nb_occurence(lst:list,element:int) ->int:
    """Fonction retournant le nombre d'occurence element  dans la liste lst """
    nombre_occurence = 0
    for index,value in enumerate(lst):
        if(value==element):
            nombre_occurence +=1
    return nombre_occurence

def est_triee(liste:list) -> bool:
    """Retourne True si liste est triée par ordre croissant

    Args:
        liste (list): liste d'entier passés en paramètres

    Returns:
        bool: Retourne True si triée par ordre croissant False sinon
    """

    listeEstTriee = True
    i = 1
    if(liste == []):
        listeEstTriee = False
    while i < len(liste) and listeEstTriee:
        if liste[i-1] > liste[i]:
            listeEstTriee = False
        i+=1
    return listeEstTriee

def position_tri(lst:list,element:int)->int:
    """ fonction permettant de chercher un nombre element sur une liste triée

    Args:
        lst (list): liste triée
        element (int) : nombre a chercher

    Returns:
        int: index ou l element se trouve
    """
    debut =0
    fin = len(lst)-1
    trouve = False
    index = 0

    if(est_triee(lst)):
        while(not trouve and debut<=fin):
            index = int((debut+fin)/2)
            if(lst[index] == element):
                trouve = True
            elif(element > lst[index]):
                debut = index + 1
            else:
                fin = index-1
    if(not trouve):
        return -1
    return index


def a_repetitions(liste:list) -> bool:
    """Indique si il y a répétition dans la liste

    Args:
        liste (list): liste a verifier

    Returns:
        bool: retourne True si répétition, False sinon
    """
    res = False
    flag = [] # Liste qui va recevoir les éléments de la liste en paramètre
    i = 0
    while i < len(liste) and not res:
        if not liste[i] in flag:
            flag.append(liste[i])
        else: # Il y a répétition
            res = True
        i+=1
    return res