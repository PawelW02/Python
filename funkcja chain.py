#zaimportowanie funkcji chain
from itertools import chain 

#utworzenie listy zawierającej inne listy
lista=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

#utworzenie i wypisanie nowej listy z obniżeniem zagnieżdżenia
l2=list(chain.from_iterable(lista))
print(l2)