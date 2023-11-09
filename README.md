
# Algorytm Smitha-Watermana

## WAŻNE INFORMACJE:
Zmienne mają przypisane wartości początkowe:

**`dopasowanie = 1`**

**`niedopasowanie = -1`**

**`przerwa = -1`**

Wartości tych zmiennych można zmienić na początku skryptu.
## SPOSÓB UŻYCIA:

1. **Uruchomienie programu:**
   Otwórz terminal lub wiersz polecenia w swoim systemie operacyjnym i uruchom program, podając nazwę pliku FASTA (lub ścieżkę do pliku) jako argument.

   Przykład użycia:
   ```
   python nazwa_programu.py --input nazwa_pliku.fasta
   ```

2. **Podanie argumentu:**
   Użytkownik musi podać argument **`--input`** wraz z nazwą pliku FASTA, który chce przetworzyć. Na przykład **`nazwa_pliku.fasta`** to przykładowa nazwa pliku FASTA.

   ```
   --input nazwa_pliku.fasta
   ```

3. **Odczyt wyniku:**
   Po zakończeniu działania programu, użytkownik otrzyma w terminalu informacje o sekwencjach, maksymalnym wyniku dopasowania oraz lokalne dopasowania dla obu sekwencji. Dodatkowo, wynik zostanie zapisany do pliku **`nazwa_pliku_wynik.txt`**.

   Przykładowe wyniki w terminalu:
   ```
    SEKWENCJA NUMER 1 - SEKWENCJA 1: ATGGCAAGT
    SEKWENCJA NUMER 2 - SEKWENCJA 2: ATCGGAGG

    MAKSYMALNY WYNIK: 3
    SEKWENCJA 1
    AT-GG
    ** **
    ATCGG
    SEKWENCJA 2
   ```

4. **Otwarcie pliku wynikowego:**
   Użytkownik może otworzyć plik `nazwa_pliku_wynik.txt` w dowolnym edytorze tekstowym, aby zobaczyć szczegółowe wyniki lokalnego dopasowania.

## PRZYKŁADY URUCHOMIENIA:

1. **Przykład 1**:

    Oryginalne sekwencje:
    ```
    PRZYKLAD 1.1: GACTATGGATGATTGGCTTAG
    PRZYKLAD 1.2: GATTGG
    ```
    Oczekiwane wyjście:
    ```
    Maksymalny wynik = 6
    Dopasowanie lokalne:
    GATTGG
    ******
    GATTGG
    ```

    Rzeczywiste wyjście:
    ```
    SEKWENCJA NUMER 1 - PRZYKLAD 1.1: GACTATGGATGATTGGCTTAG
    SEKWENCJA NUMER 2 - PRZYKLAD 1.2: GATTGG

    MAKSYMALNY WYNIK: 6
    PRZYKLAD 1.1
    GATTGG
    ******
    GATTGG
    PRZYKLAD 1.2
    ```
2. **Przykład 2**:

    Oryginalne sekwencje:
    ```
    PRZYKLAD 2.1: TCGGAATT
    PRZYKLAD 2.2: TCGGCATT
    ```
    Oczekiwane wyjście:
    ```
    Maksymalny wynik = 6
    Dopasowanie lokalne:
    TCGGAATT
    ****|***
    TCGGCATT
    ```

    Rzeczywiste wyjście:
    ```
    SEKWENCJA NUMER 1 - PRZYKLAD 2.1: TCGGAATT
    SEKWENCJA NUMER 2 - PRZYKLAD 2.2: TCGGCATT

    MAKSYMALNY WYNIK: 6
    PRZYKLAD 2.1
    TCGGAATT
    ****|***
    TCGGCATT
    PRZYKLAD 2.2
    ```
3. **Przykład 3**:

    Oryginalne sekwencje:
    ```
    PRZYKLAD 3.1: GCAA
    PRZYKLAD 3.2: GCTAA
    ```
    Oczekiwane wyjście:
    ```
    Maksymalny wynik = 3
    Dopasowanie lokalne:
    GC-AA
    ** **
    GCTAA
    ```

    Rzeczywiste wyjście:
    ```
    SEKWENCJA NUMER 1 - PRZYKLAD 3.1: GCAA
    SEKWENCJA NUMER 2 - PRZYKLAD 3.2: GCTAA

    MAKSYMALNY WYNIK: 3
    PRZYKLAD 3.1
    GC-AA
    ** **
    GCTAA
    PRZYKLAD 3.2
    ```


