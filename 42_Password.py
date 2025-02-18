risposta1 = input("inserisci la password: ")
if risposta1=="PincoPallino2022!":
    print("Password corretta")
else:
    risposta1 = input('password errata, reinserisci la password: ')
    if risposta1=="PincoPallino2022!":
        print("Password corretta")
    else:
        print("password errata, tentativi terminati")