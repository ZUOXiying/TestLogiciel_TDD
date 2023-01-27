"""Test Logiciel Functions"""
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

def geometrique_plus(n_suite,list_geo):
    """si la suite est géométrique et renvoiela liste des n éléments suivant"""
    if not si_geometrique(list_geo):
        return False
    if n_suite < 0:
        return False
    if n_suite == 0:
        return [True,[]]
    numbre = len(list_geo)
    q_list = list_geo[1]/list_geo[0]
    list_geo_plus = [list_geo[numbre-1] * q_list]
    for i in range(1,n_suite):
        list_geo_plus.append(list_geo_plus[i-1]*q_list)
    return [True,list_geo_plus]

def arithmetique_plus(n_suite,list_ari):
    """si la suite est arithmetique et renvoiela liste des n éléments suivant"""
    if not si_arithmetique(list_ari):
        return False
    if n_suite < 0:
        return False
    if n_suite == 0:
        return [True,[]]
    numbre = len(list_ari)
    q_list = list_ari[1]-list_ari[0]
    list_ari_plus = [list_ari[numbre-1] + q_list]
    for i in range(1,n_suite):
        list_ari_plus.append(list_ari_plus[i-1]+q_list)
    return [True,list_ari_plus]

def unit_valid(list_sudoku):
    """Déterminer si les données de la grille 3*3 sont en conflit"""
    for i in range(1,8,3):
        for j in range(1,8,3):
            unit,unit_vals = [],[]
            for x_coordinate in range(i-1,i+2):
                for y_coordinate in range(j-1,j+2):
                    unit.append(list_sudoku[x_coordinate][y_coordinate])
            for temp in filter(lambda x_coordinate: x_coordinate != ".", unit):
                unit_vals.append(int(temp))
            if sum(unit_vals) == sum(set(unit_vals)):
                continue
            if sum(unit_vals) != sum(set(unit_vals)):
                return False
    return True

def colonne_valid(list_sudoku):
    """Déterminer si chaque colonne de données est en conflit"""
    for i in range(9):
        unit,unit_vals = [],[]
        for j in range(9):
            unit.append(list_sudoku[j][i])
        for temp in filter(lambda x: x != ".", unit):
            unit_vals.append(int(temp))
        if sum(unit_vals) == sum(set(unit_vals)):
            continue
        if sum(unit_vals) != sum(set(unit_vals)):
            return False
    return True

def ligne_valid(list_sudoku):
    """Déterminer si chaque ligne de données est en conflit"""
    for i in range(9):
        unit,unit_vals = [],[]
        unit = list_sudoku[i]
        for temp in filter(lambda x: x != ".", unit):
            unit_vals.append(int(temp))
        if sum(unit_vals) == sum(set(unit_vals)):
            continue
        if sum(unit_vals) != sum(set(unit_vals)):
            return False
    return True

def sudoku_valid(list_sudoku):
    """Déterminer si Sudoku est valide"""
    return unit_valid(list_sudoku)&colonne_valid(list_sudoku)&ligne_valid(list_sudoku)
