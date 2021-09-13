def somme(lst:list)->object:
    """Fonction permettant de retourner la somme avec en entrée une liste"""
    #assert len(lst) != 0,"Liste Vide"
    i = 0
    resultat = 0
    tableauParcouru = False
    itterateur = 0

    for i in range(len(lst)): #Version la plus adaptée
        resultat += lst[i]

    resultat = 0
    for v in lst:
        resultat +=v

    resultat = 0
    while(not tableauParcouru):
       if itterateur < len(lst):
           resultat += lst[itterateur]
       else:
          tableauParcouru = True
       itterateur+=1
    return resultat


def moyenne(lst:list)->float:
    """Calcul la moyenne a partir d'une liste"""
    moyenne = 0
    if(len(lst)>0):
       moyenne = somme(lst) / len(lst)
    return moyenne

def nb_sup(lst:list,e:int)->int:
    """calcul le nombre de nombre superieur a e dans une liste"""
    compteurNombreSuperieur = 0
    # assert len(lst) != 0, "Liste vide"
    for i in range(len(lst)):
        if lst[i] > e:
            compteurNombreSuperieur+=1
    compteurNombreSuperieur = 0
    for v in lst:
        if v > e:
            compteurNombreSuperieur +=1

    return compteurNombreSuperieur

def moy_sup(lst:list,e:int)->float:
    """calcul la moyenne d'une liste de nombre superieur a e"""
    # assert len(lst) != 0, "Liste vide"
    nombre_au_dessus_de_e = []

    for v in lst:
        if v > e :
            nombre_au_dessus_de_e.append(v)
    return somme(nombre_au_dessus_de_e) / len(nombre_au_dessus_de_e)

def val_max(lst:list)->float:
    """ retourne la valeurs maximum de la liste """
    #assert len(lst) != 0, "Liste vide"
    valeurMaximum = lst[0]
    for i,v in enumerate(lst):
        if(valeurMaximum < v):
            valeurMaximum = v
    return valeurMaximum

def ind_max(lst:list) ->int:
    # assert len(lst) != 0, "Liste vide"
    indexMax = 0
    valeurMaximum = lst[0]
    for i,v in enumerate(lst):
        if(valeurMaximum < v):
            valeurMaximum = v
            indexMax = i
    return indexMax

def test_exercice1 ():
    print("TEST SOMME")
#test liste vide
   # print("Test liste vide : ", somme([]))
#test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 11111 : ", somme(S))

    print("TEST MOYENNE")
#test liste Vide
    print("Test liste vide : ", moyenne([]))
#test moyenne 2222
    print("Test moyenne 2222: ", moyenne(S))

    print("TEST Nombre SUP")

    #test liste vide
    print("Test liste vide : ", nb_sup([],10))
    print("Test Valeurs entierement positif resultat = 4",nb_sup([10,30,40,50,60],20))
    print("Test Valeurs entierement negatif resultat = 1",nb_sup([-10,-30,-40,-50,-60],-20))
    print("Test Valeurs mixte resultat = 2",nb_sup([-10,30,-40,50,60],30))

    print("TEST moy_sup")

    print("Moyenne sup test : resultat = 38",moy_sup([50,12,13,45,19],15))


#test_exercice1()
def est_triee(liste:list) -> bool:
    listeEstTriee = True
    i = 1

    while i < len(liste) and listeEstTriee:
        if liste[i-1] > liste[i]:
            listeEstTriee = False
        i+=1
    return listeEstTriee


def position_tri(lst:list,element:int)->int:
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

print(position_tri([1,2,3,4,5,6],5))



