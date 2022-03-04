a=int(input("Podaj liczbę całkowitą: "))

#sprawdzenie czy podana liczba dzieli się bez reszty
b=a%2


#if (b==0):
#    print("Liczba parzysta")
#else:
#    print("Liczba nieparzysta")

while (b==1):
    print("Liczba nieparzysta")
    break
while (b==0):
    print("Liczba parzysta")
    break