"""Test Logiciel TDD"""
def si_geometrique(list_geo):
    """si c’est une suite géométrique"""
    numbre = len(list_geo)
    if numbre == 1:
        return False
    try:
        q_list = list_geo[1]/list_geo[0]
        for i in range(1,numbre):
            temp = list_geo[i]/list_geo[i-1]
            if temp != q_list:
                return False
        return True
    except ZeroDivisionError:
        return False

def si_arithmetique(list_ari):
    """si c’est une suite arithmétique"""
    numbre = len(list_ari)
    if numbre == 1:
        return False
    d_list = list_ari[1]-list_ari[0]
    for i in range(1,numbre):
        temp = list_ari[i]-list_ari[i-1]
        if temp != d_list:
            return False
    return True
