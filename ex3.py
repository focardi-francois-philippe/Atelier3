
def separer(lst:list)->list:
    """ 
    fonction permettant de separer des nombres en fonctions de leurs types

    Args:
        lst (list): liste definit

    Returns:
        list: la liste triée
    """
    lsep = []
    nombre_element_negatif = 0
    
    for index,value in enumerate(lst):
        if(value<0):
            lsep.insert(0,value)
            nombre_element_negatif+=1
        elif(value>0):
            lsep.append(value)
        else:
            lsep.insert(nombre_element_negatif,0)
            
    
    return lsep

print(separer([1,-1,2,-2,3,-3,-4,4,-5,6,0,0,0,0,-10,-15,-12,12,13,19]))
    
            
        
        
        
        
    
    