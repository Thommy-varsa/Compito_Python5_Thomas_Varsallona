prezzo = float(input("inserisci prezzo automobile: "))
if 10000<=prezzo<=20000:
    sconto=prezzo*0.05
    #print(sconto)
    prezzo = prezzo-sconto
    contanti = input("vuoi pagare in contanti? Rispondi si o no ")
    if contanti=="si":
        prezzo=prezzo-200
print("devi pagare",prezzo)