#lista
samogloski=("a","e","i","o","u","y","ą","ę","ó")

spr=input("Podaj literę: ")

#sprawdzenie czy podany znak jest literą
if spr.isalpha():
    
    #sprawdzenie czy podana litera należy do listy samogłosek
    if spr in samogloski:
        print("Samogloska")
    else:
        print("Spolgloska")
else:
    print("Podano liczbę lub znak")