#utworzenie i wypisanie listy z zastosowaniem funkcji range
lista = list(range(3, 100, 3))
print(lista)

#usunięcie co 3 elementu zaczynając od 5.
del lista[4::3]
print(lista )

#obliczenie i wypisanie średniej
sr=(sum(lista))/len(lista)
print(sr)