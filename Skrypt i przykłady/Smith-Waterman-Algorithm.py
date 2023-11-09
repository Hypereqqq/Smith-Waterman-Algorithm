### ZMIENNE
dopasowanie = 1
niedopasowanie = -1
przerwa = -1
###

import argparse

def wczytaj_fasta(nazwa_pliku):
    with open(nazwa_pliku, 'r') as file:
        linie = file.readlines()
    sekwencje = {}
    nazwa = None
    for linia in linie:
        linia = linia.strip()
        if linia.startswith(">"):
            nazwa = linia[1:]
            sekwencje[nazwa] = ""
        else:
            sekwencje[nazwa] += linia
    return sekwencje

def smith_waterman(sek1, sek2, dopasowanie, niedopasowanie, przerwa):
    # Inicjalizacja macierzy
    macierz = [[0 for _ in range(len(sek2)+1)] for _ in range(len(sek1)+1)]

    # Wypełnianie macierzy
    max_wynik = 0
    max_i = max_j = 0

    for i in range(1, len(sek1)+1):
        for j in range(1, len(sek2)+1):
            if sek1[i-1] == sek2[j-1]:
                skos = macierz[i-1][j-1] + dopasowanie
            else:
                skos = macierz[i-1][j-1] + niedopasowanie

            lewo = macierz[i][j-1] + przerwa
            gora = macierz[i-1][j] + przerwa

            macierz[i][j] = max(0, skos, lewo, gora)

            if macierz[i][j] > max_wynik:
                max_wynik = macierz[i][j]
                max_i = i
                max_j = j

    # Odtworzenie lokalnego dopasowania
    dop1 = ''
    dop2 = ''

    i = max_i
    j = max_j

    while macierz[i][j] > 0:
        if sek1[i-1] == sek2[j-1]:
            dop1 = sek1[i-1] + dop1
            dop2 = sek2[j-1] + dop2
            i -= 1
            j -= 1
        elif macierz[i][j] == macierz[i-1][j-1] + niedopasowanie:
            dop1 = sek1[i-1] + dop1
            dop2 = sek2[j-1] + dop2
            i -= 1
            j -= 1
        elif macierz[i][j] == macierz[i-1][j] + przerwa:
            dop1 = sek1[i-1] + dop1
            dop2 = '-' + dop2
            i -= 1
        else:
            dop1 = '-' + dop1
            dop2 = sek2[j-1] + dop2
            j -= 1

    return max_wynik, dop1, dop2

wsad = argparse.ArgumentParser(description='ALGORYTM SMITHA-WATERMANA')
wsad.add_argument('--input', required=True, help='NAZWA PLIKU FASTA')
argumenty = wsad.parse_args()

nazwa_pliku = argumenty.input
sekwencje = wczytaj_fasta(nazwa_pliku)

if len(sekwencje) < 2:
    print("W PLIKU MUSZĄ BYĆ PRZYNAJMNIEJ 2 SEKWENCJE.")
    exit()

nazwa_sekwencji1, sek1 = list(sekwencje.items())[0]
nazwa_sekwencji2, sek2 = list(sekwencje.items())[1]

wynik, dopasowanie1, dopasowanie2 = smith_waterman(sek1, sek2, dopasowanie, niedopasowanie, przerwa)

symbole = ""

for i in range(len(dopasowanie1)):
    if dopasowanie1[i] == dopasowanie2[i]:
        symbole += "*"
    else:
        symbole += " "

nazwa_pliku_wynik = nazwa_pliku[:-6] + "_wynik.txt"
with open(nazwa_pliku_wynik, 'w') as output_file:
    output_file.write(f"SEKWENCJA NUMER 1 - {nazwa_sekwencji1}: {sek1}\n")
    output_file.write(f"SEKWENCJA NUMER 2 - {nazwa_sekwencji2}: {sek2}\n\n")
    output_file.write(f"MAKSYMALNY WYNIK: {wynik}\n")
    output_file.write(f"{nazwa_sekwencji1}\n")
    output_file.write(f"{dopasowanie1}\n")
    output_file.write(f"{symbole}\n")
    output_file.write(f"{dopasowanie2}\n")
    output_file.write(f"{nazwa_sekwencji2}\n")

print(f"SEKWENCJA NUMER 1 - {nazwa_sekwencji1}: {sek1}")
print(f"SEKWENCJA NUMER 2 - {nazwa_sekwencji2}: {sek2}\n")
print(f"MAKSYMALNY WYNIK: {wynik}")
print(f"{nazwa_sekwencji1}")
print(f"{dopasowanie1}")
print(f"{symbole}")
print(f"{dopasowanie2}")
print(f"{nazwa_sekwencji2}\n")

print(f"WYNIK ZAPISANO DO: {nazwa_pliku_wynik}")
