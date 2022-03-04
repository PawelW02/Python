lista=[(2, 8),(5, 5),(9, 3),(1, 0),(3, 2),(6, 4),(1, 9),(10, 3),(2, 3),(1, 7)]
def trzeci(elem):
    return elem[2]
#utworzenie nowej listy, która jest uporządkowaną wersją poprzedniej
#posortowanie według 2 elementu listy
#l2=sorted(lista, key=lambda x: x[1])
l2=sorted(lista, key=trzeci)

#wypisanie posortowanej listy
print(l2)