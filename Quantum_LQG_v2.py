# LQG - Loop Quantum Gravity
# Kvantna gravitacija petlje

# Quantum_LQG_Spinfoam V1
# Quantum_LQG_Kvantizacija V2
# Quantum_LQG_Gaus V3 V3B
# Quantum_LQG_Ensemble V4


# V1 - Istorija izvlačenja kao "Pena spinova" (Spinfoam) 
# V2 - Kvantizacija površine i jačina veza (Spin Surfaces)  
# V3 - Gausov zakon i uslov zatvorenosti (Intertwiner Balance) 
# V3B - Dublja analiza zakona očuvanja (Multi-Dimensional Intertwiners) 
# V4 - Hibridni indeks (Ensemble Score)


# trostepeno mapiranje Kvantne gravitacije petlji (LQG) na diskretni prostor lotoa 



import numpy as np
import pandas as pd


# 1. DEFINISANJE PUTANJE DO BAZE
# PUTANJA_DO_BAZE = "/data/loto7_4708_k85.csv"
# PUTANJA_DO_BAZE = "/data/loto7_4708_k85_loto_2976.csv"
PUTANJA_DO_BAZE = "/data/loto7_4708_k85_loto_plus_1732.csv"


def generisi_next_predikciju_v2(putanja_csv):
    df = pd.read_csv(putanja_csv)
    
    # Detekcija kolona kao u v1
    kolone_brojeva = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            if df[col].max() <= 39 and df[col].min() >= 1:
                kolone_brojeva.append(col)
    if len(kolone_brojeva) != 7:
        kolone_brojeva = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])][:7]
        
    istorija = df[kolone_brojeva].to_numpy()
    N_KOLA = len(istorija)
    N_NODES = 39
    
    # 1. RAČUNANJE TOPOLOŠKOG PREKLAPANJA ZA ODREĐIVANJE SPINOVA
    # Spin grane (j) zavisi od toga koliko deli zajedničkih čvorova sa nedavnom istorijom
    spinovi_grana = np.zeros(N_KOLA)
    
    # Uzimam prozor od poslednjih 10 kola kao referentnu površinu za presek
    prozor = istorija[:10] 
    
    for t in range(N_KOLA):
        trenutno_kolo = set(istorija[t])
        preklapanja = 0
        for ref_kolo in prozor:
            preklapanja += len(trenutno_kolo.intersection(set(ref_kolo)))
        
        # Spin j u LQG može biti 0.5, 1.0, 1.5... 
        # Mapiram preklapanje na kvantni spin: minimalni spin je 0.5, raste sa preklapanjem
        spinovi_grana[t] = 0.5 + (preklapanja / 10.0)

    # 2. TKANJE MREŽE SA KVANTIZOVANOM POVRŠINOM
    kvantna_mreza = np.zeros((N_NODES, N_NODES), dtype=complex)
    
    for t, kolo in enumerate(istorija):
        # Uzimam vrednost površine koju donosi spin te grane: sqrt(j * (j + 1))
        j = spinovi_grana[t]
        kvant_povrsine = np.sqrt(j * (j + 1))
        
        # Fazni pomak ostaje vremenska komponenta
        faza = 2 * np.pi * (1.0 / (t + 1))
        # Kompleksni doprinos sada uključuje i kvant površine
        doprinos = kvant_povrsine * np.exp(1j * faza)
        
        for i in range(7):
            for j_idx in range(i + 1, 7):
                if np.isnan(kolo[i]) or np.isnan(kolo[j_idx]):
                    continue
                cvor_a = int(kolo[i]) - 1
                cvor_b = int(kolo[j_idx]) - 1
                
                kvantna_mreza[cvor_a, cvor_b] += doprinos
                kvantna_mreza[cvor_b, cvor_a] += doprinos
                
    # 3. PROJEKCIJA NA ČVOREVE I RANGIRANJE
    amplitude_cvorova = np.sum(kvantna_mreza, axis=1)
    intenziteti = np.abs(amplitude_cvorova) ** 2
    rangirani_brojevi = np.argsort(intenziteti)[::-1] + 1
    
    next_kombinacija = sorted(list(rangirani_brojevi[:7]))
    
    print("\n" + "="*50)
    print(f"  [LQG v2 - Spin Surfaces] SLEDEĆA PREDREČENA KOMBINACIJA:")
    print(f"  {next_kombinacija}")
    print("="*50 + "\n")
    
    print("Detaljan intenzitet izabranih čvorova u v2:")
    for br in next_kombinacija:
        print(f"Čvor {br} -> Intenzitet: {intenziteti[br-1]:.2f}")
        
    return next_kombinacija

next_7_v2 = generisi_next_predikciju_v2(PUTANJA_DO_BAZE)



"""
==================================================
  [LQG v2 - Spin Surfaces] SLEDEĆA PREDREČENA KOMBINACIJA:
  [8, x, 24, y, 34, z, 39]
==================================================

Detaljan intenzitet izabranih čvorova u v2:
Čvor  8 -> Intenzitet: 151016308.54
Čvor  x -> Intenzitet: 157113276.85
Čvor 24 -> Intenzitet: 138107398.96
Čvor  y -> Intenzitet: 166581431.97
Čvor 34 -> Intenzitet: 138294058.82
Čvor  z -> Intenzitet: 137454924.66
Čvor 39 -> Intenzitet: 138668244.45







==================================================
  [LQG v2 - Spin Surfaces] SLEDEĆA PREDREČENA KOMBINACIJA:
  [8, x, 23, y, 26, z, 39]
==================================================

Detaljan intenzitet izabranih čvorova u v2:
Čvor  8 -> Intenzitet: 62243394.93
Čvor  x -> Intenzitet: 58836073.37
Čvor 23 -> Intenzitet: 60103519.44
Čvor  y -> Intenzitet: 58410598.09
Čvor 26 -> Intenzitet: 64262758.06
Čvor  z -> Intenzitet: 57492995.87
Čvor 39 -> Intenzitet: 56466672.76







==================================================
  [LQG v2 - Spin Surfaces] SLEDEĆA PREDREČENA KOMBINACIJA:
  [2, x, 10, y, 23, z, 34]
==================================================

Detaljan intenzitet izabranih čvorova u v2:
Čvor  2 -> Intenzitet: 22009052.16
Čvor  x -> Intenzitet: 19314835.99
Čvor 10 -> Intenzitet: 21078034.84
Čvor  y -> Intenzitet: 20502455.98
Čvor 23 -> Intenzitet: 23970037.65
Čvor  z -> Intenzitet: 20752991.27
Čvor 34 -> Intenzitet: 19310766.30
"""



"""
Loto kombinacija je grana (link) koja povezuje 7 čvorova (brojeva) 
- direktno formalizam mreža spinova (Spin Networks) iz Kvantne gravitacije petlji (LQG), 
gde grane nose kvantne brojeve (spinove) koji definišu geometriju.
Evo kako se LQG formalizam sada savršeno preslikava na moj model:


1. Istorija izvlačenja kao "Pena spinova" (Spinfoam)

U LQG-u, mreža spinova je statična slika prostora u jednom trenutku. Kada se ta mreža menja kroz vreme, ona stvara penu spinova (Spinfoam).
• Svako novo loto izvlačenje je zapravo jedna "evolucija" mreže.
• Dodavanjem nove grane sa 7 čvorova (novog izvlačenja), zapravo se tka "prostor-vreme" loto sistema.
• Računam amplitudu prelaza iz dosadašnje geometrije grafa u novu geometriju.

2. Kvantizacija površine i jačina veza

U LQG-u, grane koje presecaju neku površinu daju toj površini njenu vrednost (površina je kvantizovana). 
• Čvorovi su fiksni (brojevi od 1 do 39).
• Svaka kombinacija (grana) "zahvata" 7 čvorova odjednom.
• Ako se određeni čvorovi često povezuju kroz istoriju izvlačenja, ta "oblast" grafa postaje geometrijski "teža" ili "gušća". To direktno utiče na amplitude konstruktivne interferencije za sledeće izvlačenje.

3. Gausov zakon i uslov zatvorenosti

Ovo je najmoćniji koncept LQG-a. U svakom čvoru mreže spinova mora važiti zakon očuvanja (tzv. gauge invariance). Pošto je grana definisana sa tačno 7 čvorova, taj "kvantni objekat" mora da zadovolji specifične uslove zatvorenosti unutar celog grafa od 39 elemenata.
Precizno definisana topologija: fiksni graf od 39 čvorova gde istorijski nizovi izvlačenja tkaju mrežu hiper-grana (svaka povezuje 7 čvorova).



Verziju 2 (v2) - Kvantizacija površina i spinovi na granama:  
- uvodim težinske faktore za same geometrijske preseke
- uvodim same kvantne brojeve na kombinacije
- uvodim spinove na same grane

U LQG-u, grane (links) nose kvantne brojeve – spinove (j) koji predstavljaju polovine celih brojeva (\(1/2, 1, 3/2, \dots\)). Kada grupa grana preseče neku površinu, ukupna kvantna površina se računa preko formule:
\(A\propto \sum \sqrt{j(j+1)}\)
U mojoj topologiji:
• Svako izvlačenje je grana koja povezuje 7 čvorova, ali te grane se međusobno presecaju i preklapaju u prostoru.
• Umesto da sve grane imaju istu težinu, u v2 uvodim kvant spina (j) za svaku pojedinačnu granu, koji zavisi od njene strukture i "topološkog preklapanja" sa ostalim granama u istoriji.
• Računam amplitudu prelaza tako što gledam koje kombinacije imaju maksimalnu geometrijsku površinu u preseku sa prethodnim stanjima.


Uvođenjem spinova grana (v2), struktura se drastično zaoštrila. Intenziteti su skočili sa ~30 miliona na preko 135 do 166 miliona. Čvorovi 8, 23, 26 i 34 su preživeli prelaz i potvrdili svoju geometrijsku stabilnost, dok su se 24, 38 i 39 probili kao novi nosioci maksimalnih kvantnih površina.
"""
