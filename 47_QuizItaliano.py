print("Ciao! Facciamo un quiz.")
risposta = int(input("In che anno è nato Alessandro Manzoni? "))
if risposta > 1785:
    print("Uhm… è nato prima dell’anno",risposta)
    risposta2 = input("Vuoi studiare di più? Rispondi sì o no")
    if risposta2== "sì":
        print("Ottimo.")
    else:
        print("Ti conviene farlo ugualmente.")
elif risposta < 1785 :
    print("Uhm… è nato dopo l'anno",risposta)
else:
    print("Bene. Hai inserito l’anno corretto.")
    
    print("Passiamo alla prossima domanda")
    risposta3 = input("chi sono i due protagonisti dei Promessi Sposi? ")
    risposta3 = risposta3.lower()
        
    if risposta3 == "renzo e lucia": 
        print("risposta corretta")    
        if risposta3 == "renzo":
            print("è giusto renzo ma manca la ragazza...")
        if risposta3 == "lucia":
            print("è giusto ma manca il ragazzo...") 
        else:
            print("nessuno dei 2 è corretto...")
    