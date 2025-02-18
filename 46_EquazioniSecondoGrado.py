import math
def calcola_equazione():
    # Inserimento dei coefficienti
    a = float(input("Inserisci il coefficiente a: "))
    b = float(input("Inserisci il coefficiente b: "))
    c = float(input("Inserisci il coefficiente c: "))
    # Caso equazione di primo grado
    if a == 0:
        if b != 0:
            x = -c / b
            print(f"Equazione di primo grado: x = {x:.2f}")
        else:
            print("Nessuna soluzione se c ≠ 0, infinite soluzioni se c = 0.")
        return
    # Calcolo del delta per l'equazione di secondo grado
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Due soluzioni distinte: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Unica soluzione: x = {x:.2f}")
    else:
        parte_reale = -b / (2 * a)
        parte_immaginaria = math.sqrt(-delta) / (2 * a)
        print(f"Soluzioni complesse: x1 = {parte_reale:.2f} + {parte_immaginaria:.2f}i, x2 = {parte_reale:.2f} - {parte_immaginaria:.2f}i")
calcola_equazione()