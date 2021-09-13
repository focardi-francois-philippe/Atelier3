def est_present(lst: list, e: int) -> bool:
    present = False
    if(len(lst) == 0):
        present = False
    for element in lst:
        if(element == e):
            present = True
    return present


def test_present(present: callable):
    if not present([], 10):
        print("SUCCES : test liste vide")
    else:
        print("ECHEC : test liste vide")
    print("TEST DEBUT")
    if present([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1):
        print("SUCCES TEST DEBUT")
    else:
        print("ECHEC TEST DEBUT")
    print("TEST FIN")
    if present([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10):
        print("SUCCES TEST FIN")
    else:
        print("ECHEC TEST FIN")
    print("TEST MILIEU")
    if present([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5):
        print("SUCCES TEST MILIEU")
    else:
        print("ECHEC TEST MILIEU")
    if not present([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11):
        print("SUCCES TEST absent")
    else:
        print("ECHEC TEST absent")

# VERSION 1


def present1(lst, e):
    for i in range(0, len(lst), 1):
        if (lst[i] == e):
            return(True)
        else:
            return (False)
    return (False)

def present2 (lst, e) :
    b=True
    for i in range (0, len(lst), 1) :
        if (lst[i] == e) :
            b=True
        else :
            b=False
    return (b)


def present3 (lst, e) :
    b=True
    for i in range (0, len(lst), 1) :
        return (lst[i] == e)




test_present(present3)