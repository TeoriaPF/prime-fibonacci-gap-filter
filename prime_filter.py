import numpy as np

def gjenero_primet(n_max):
    """Gjeneron nje liste me n_max numra prime."""
    primet = []
    numri = 2
    while len(primet) < n_max:
        eshte_prim = True
        for p in primet:
            if p * p > numri:
                break
            if numri % p == 0:
                eshte_prim = False
                break
        if eshte_prim:
            primet.append(numri)
        numri += 1
    return primet

def filtri_parashikues_fibonacci(prim_aktual, diferenca_e_fundit):
    """Algoritmi i parashikimit bazuar ne filtrin Prime-Fibonacci."""
    diferenca_mesatare = np.log(prim_aktual)
    
    if diferenca_e_fundit == 2:
        diferenca_baze = 4 if diferenca_mesatare < 8 else 6
    elif diferenca_e_fundit == 8:
        diferenca_baze = 6  # Bllokimi i Fibonaccit
    elif diferenca_e_fundit == 34:
        diferenca_baze = 6 if diferenca_mesatare > 12 else 2  # Efekti kthyes
    else:
        diferenca_baze = 6 if diferenca_mesatare > 7 else 4

    faktorizimi = max(1.0, diferenca_mesatare / 3.0)
    parashikimi = int(round(diferenca_baze * faktorizimi))
    
    if parashikimi % 2 != 0:
        parashikimi += 1
    if parashikimi == diferenca_e_fundit:
        parashikimi += 2
        
    return parashikimi

# Ekzekutimi i testit mbi 10,000 numra
primet = gjenero_primet(10001)
gabimet = []
saktesi_absolute = 0

for i in range(1, len(primet) - 1):
    p_akt = primet[i]
    p_pasardhes_real = primet[i+1]
    dif_fundit = primet[i] - primet[i-1]
    
    # Llogaritja e parashikimit
    dif_parashikuar = filtri_parashikues_fibonacci(p_akt, dif_fundit)
    p_parashikuar = p_akt + dif_parashikuar
    
    # Llogaritja e gabimit
    gabimi = abs(p_parashikuar - p_pasardhes_real)
    gabimet.append(gabimi)
    
    if gabimi == 0:
        saktesi_absolute += 1

# Afishimi i rezultateve ne ekran
print("=== STATISTIKAT E MODELIT TË RI ===")
print(f"Gabimi mesatar absolut: {np.mean(gabimet):.2f} numra")
print(f"Raste me saktësi 100% (Gabimi = 0): {saktesi_absolute} nga {len(gabimet)}")
print(f"Përqindja e rasteve shumë afër (Gabimi <= 4): {(sum(1 for g in gabimet if g <= 4) / len(gabimet)) * 100:.2f}%")
