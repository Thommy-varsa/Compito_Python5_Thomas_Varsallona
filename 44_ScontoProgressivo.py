def calcola_importo_finale(num_articoli, prezzi):
    totale = sum(prezzi)  # Calcola il prezzo totale
    
    if num_articoli < 10:
        # Sconto del 5% se ogni articolo costa almeno 10€, altrimenti 2%
        sconto = 0.05 if all(prezzo >= 10 for prezzo in prezzi) else 0.02
    elif num_articoli == 10:
        # Sconto del 10% sul totale
        sconto = 0.10
    else:  # num_articoli > 10
        if totale > 100:
            sconto = 0.50  # Sconto del 50%
        elif totale < 100:
            sconto = 0.30  # Sconto del 30%
        else:
            sconto = 0.35  # Sconto del 35%
    
    importo_finale = totale * (1 - sconto)
    return round(importo_finale, 2)
# Esempio di utilizzo
totale_da_pagare = calcola_importo_finale(12, [15, 20, 8, 12, 5, 7, 18, 30, 12, 10, 6, 9])
print(f"Importo finale da pagare: {totale_da_pagare}€")