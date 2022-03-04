#Paweł Woźniak
#zaimportowanie biblioteki obsługującej formaty kolorów
import colorsys

#pobranie wartości od użytkownika
r=float(input('Podaj wartość R: '))
g=float(input('Podaj wartość G: '))
b=float(input('Podaj wartość B: '))

#konwersja z RGB na HSV
print(colorsys.rgb_to_hsv(r, g, b))