#Paweł Woźniak
#funkcja usuwająca powtórki w liście
def powt(lista):
    #utworzenie nowej listy będącej poprawioną wersją poprzedniej
    lista2=list(set(lista))
    #wypisanie nowej listy
    print(lista2)
#wywołanie funkcji z przykładowymi wartościami
powt([1,1,1,2,3,3,4,4,5])