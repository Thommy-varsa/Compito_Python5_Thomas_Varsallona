numero=int(input("inserisci un numero:"))
if numero%5==0 and numero%3==0:
    print("il numero è divisibile sia per 3 che per 5")
elif numero%3==0:
    print("il numero è divisibile solo per 3")
elif  numero%5==0:
    print("il numero è divisibile per 5")
else:
    print("il numero non è divisibile ne per 3 ne per 5")