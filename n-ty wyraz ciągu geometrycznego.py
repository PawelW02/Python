#Paweł Woźniak
#funkcja wypisująca n-ty wyraz ciągu według wzoru na n-ty wyraz ciągu, zdefiniowany domyślny wyraz pierwszy oraz iloczyn
def ciag(n, a1=1, q=2):
    an = float(a1*q**(n-1))
    print('an = ',an)
#wywołanie funkcji dla 10 wyrazów
ciag(10)