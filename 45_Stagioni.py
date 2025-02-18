def determina_stagione(giorno, mese):
    if mese < 1 or mese > 6 or giorno < 1 or giorno > 31:
        return "Data non valida"
    
    if (mese == 3 and giorno >= 20) or mese in (4, 5) or (mese == 6 and giorno < 21):
        return "Primavera"
    elif (mese == 6 and giorno >= 21) or mese in (1, 2) or (mese == 3 and giorno < 20):
        return "Inverno"
    else:
        return "Data non valida"
# Input utente
giorno = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese (1-6): "))
# Stampa della stagione corrispondente
print("La stagione corrispondente è:", determina_stagione(giorno, mese))