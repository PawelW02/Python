#Paweł Woźniak
#przykładowa lista
lista=[1,2,3,4,9,33,55]

#zsumowanie elementów listy
print('suma', sum(lista))

#mnożenie elementów listy
#zdefiniowanie i ustalenie wartości zmiennej s
s=1

#pętla nadpisująca wartość s mnożąc przez kolejne elementy listy
for i in range(len(lista)):
    s = lista[i] * s

#wypisanie ostatniej wartości s
print('iloczyn: ', s)