import math

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

#obliczenie delty 
delta = (b*b)-(4*a*c)

#sprawdzenie czy równanie jest kwadratowe
if a != 0:
    
    #wyznaczenie pierwiastków w przypadku delty >0
    if delta > 0:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)    
        
        print ("x1 = ", x1)    
        print ("x2 = ", x2) 
        
    else:
        
        #wyznaczenie x, gdy delta=0
        if delta ==0:
            x=-b/(2*a)
            print ("x = ", x)


        #przypadek ujemnej delty    
        else:
            print ("brak miejsc zerowych")
else:
    print("Równanie nie jest kwadratowe!")