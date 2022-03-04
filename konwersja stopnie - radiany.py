#Paweł Woźniak
import math
#pytanie w którą stronę ma zajść konwersja i pobranie kąta od użytkownika
a=int(input('stopnie -> radiany = 1   radiany -> stopnie = 2    '))
b=float(input('podaj wartosc kata: '))
# zamiana stopni na radiany 
if a == 1:
    c=float((b/180)*math.pi)
    print(c)
#zamiana radianów na stopnie
if a==2:
    c=float((b*180)/math.pi)
    print(c)