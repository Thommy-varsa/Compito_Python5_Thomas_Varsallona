print("Benvenuto nel mio programma di conversazione")
print()
risposta=input("Ti piace andare in bicicletta? Rispondi si o no:")
if risposta=="si" :
    print("Molto bene! Ti terrai in forma.")
    risposta2 = input("Ti piace anche il basket?")
    if risposta2=="si":
        print("Allora sei un atleta!")
    else:
        print("Uno sport è meglio di niente!")
else:
    print("Forse ti piace qualche altro sport.")