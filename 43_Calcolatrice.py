print("1 addizione - 2 sottrazione - 3 moltiplicazione - 4 divisione")
operazione = int(input("inserire operazione richiesta: "))
if operazione == 1:
    n1 = float(input("inserire numero: "))
    n2 = float(input("inserire numero: "))
    print("il risultato è:",n1+ n2)
if operazione == 2:
    n1 = float(input("inserire numero: "))
    n2 = float(input("inserire numero: "))
    print("il risultato è:",n1 - n2)
if operazione == 3:
    n1 = float(input("inserire numero: "))
    n2 = float(input("inserire numero: "))
    print("il risultato è:",n1 * n2)
if operazione == 4:
    n1 = float(input("inserire numero: "))
    n2 = float(input("inserire numero: "))
    print("il risultato è:",n1 / n2)