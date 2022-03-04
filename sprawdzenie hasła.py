import re
haslo=input('haslo: ')

#Przypisanie warunków do zmiennych
a=re.search("[a-z]", haslo)
b=re.search("[A-Z]", haslo)
c=re.search("[0-9]", haslo)
d=re.search("[$#@]", haslo)
e=len(haslo)

#sprawdzenie czy wszystkie warunki są spełnione
if(a and b and c and d and e<=16 and e>=6):
    print("Haslo spelnia wymagania")
else:
    print("Haslo nie spelnia wymagan")