#Paweł Woźniak
#funkcja znajdująca NWD rozkładając liczby na części pierwsze
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a
#przykładowe wywołanie funkcji
print(nwd(55,50))