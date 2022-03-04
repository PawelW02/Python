#Pawel Wozniak

#slownik zawierajacy potrzebne liczby
liczby={'zero':0, 'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'piec':5, 'szesc':6, 'siedem':7, 'osiem':8, 'dziewiec':9,
        'dziesiec':10, 'jedenascie':11, 'dwanascie':12, 'trzynascie':13, 'czternascie':14, 'pietnascie':15, 'szesnascie':16, 'siedemnascie':17, 'osiemnascie':18, 'dziewietnascie':19,
        'dwadziescia':20, 'trzydziesci':30, 'czterdziesci':40, 'piecdziesiat':50}
#funkcja przeliczajaca wartosci slowne uzywajac slownika
def przelicz(n=""):
    l=n.split()
    s=0
    for x in l:
       if x in liczby:
           s+=liczby[x]
    return s
#pobranie liczby slownie i wypisanie jej wartosci liczbowej
t=input("Podaj liczbe slownie z zakresu 1-59: ")
print ("Wartość:", przelicz(t))