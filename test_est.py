from ex2 import est_triee

def test_est_triee() -> bool:
    """
    Fonction de test si une liste est triée

    Returns:
        bool: True si tous les tests sont validés. False sinon
    """
    LISTE_VIDE = []

    LISTE_PAS_TRIEE1 = [5,3,1,2,9,8]
    LISTE_PAS_TRIEE2 = [1,2,-15,-2,9,-8]
    LISTE_PAS_TRIEE3 = [-1,-2,19,-19,-9,8]

    LISTE_TRIEE1 = [1,2,3,4,5]
    LISTE_TRIEE2 = [10,200,3565,42535,598387]
    LISTE_TRIEE3 = [-19,-6,77,77,77,77,88]

    fonction_valide = True

    # Triée #
    print("Resultat attendu : True")
    print("Test 1 : {}, obtenu : {}".format(LISTE_TRIEE1,est_triee(LISTE_TRIEE1)))
    print("Test 2 : {}, obtenu : {}".format(LISTE_TRIEE2,est_triee(LISTE_TRIEE2)))
    print("Test 3 : {}, obtenu : {}".format(LISTE_TRIEE3,est_triee(LISTE_TRIEE3)))

    if not est_triee(LISTE_TRIEE1) or not est_triee(LISTE_TRIEE2) or not est_triee(LISTE_TRIEE3):
        fonction_valide = False

    # Non Triée#
    print("\n\nResultat attendu : False")
    print("Test 1 : {}, obtenu : {}".format(LISTE_PAS_TRIEE1,est_triee(LISTE_PAS_TRIEE1)))
    print("Test 2 : {}, obtenu : {}".format(LISTE_PAS_TRIEE2,est_triee(LISTE_PAS_TRIEE2)))
    print("Test 3 : {}, obtenu : {}".format(LISTE_PAS_TRIEE2,est_triee(LISTE_PAS_TRIEE2)))

    if est_triee(LISTE_PAS_TRIEE3) or est_triee(LISTE_PAS_TRIEE2) or est_triee(LISTE_PAS_TRIEE3):
        fonction_valide = False

    # None ou Vide #
    print("Resultat attendu : False")
    print("Test : {}, obtenu : {}".format(LISTE_VIDE,est_triee(LISTE_VIDE)))

    if est_triee(LISTE_VIDE):
        fonction_valide = False

    return fonction_valide

print(test_est_triee())