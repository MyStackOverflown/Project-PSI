# Wykorzystanie metod głębokiego uczenia do analizy i syntezy stylu literackiego

## Mateusz Żydek, Jan Pawelec

---

## Kamienie milowe do realizacji projektu

### 1. Określenie tematu i analiza wymagań
Jasny, krótki opis określający wymagania i zakres, który będzie podstawą dalszych prac i oceny.

### 2. Zebranie oraz przygotowanie danych
Gotowy do treningu dataset, dokumentacja kroków preprocessingu oraz przygotowanie środowiska do pracy.

### 3. Wybór i implementacja modelu AI
Wybór architektury, implementacja, sampling, ewentualna implementacja checkpointów.

### 4. Ocena wyników modelu i optymalizacja
Uzyskanie mierzalnej oceny jakości generowanego tekstu oraz opracowanie mierzalnej optymalizacji eksperymentalnej.

### 5. Wdrożenie modelu i demonstracja aplikacji
Opracowanie wersji demonstracyjnej, przygotowanie dokumentacji oraz opracowanie raportu.

---

## Wymagania i zakres projektu

### Cel projektu
Celem projektu jest zaprojektowanie i implementacja modelu opartego na metodach głębokiego uczenia, zdolnego do generowania tekstu naśladującego styl literacki wybranego autora na podstawie jego wcześniejszych dzieł.

Model powinien uchwycić cechy stylu, takie jak:
- słownictwo,
- składnia,
- długość i struktura zdań,
- powtarzalne wzorce stylistyczne.

### Zakres projektu
Projekt obejmuje:
- przygotowanie datasetu tekstowego,
- preprocessing danych,
- wybór i implementację modelu generatywnego,
- trening modelu na przygotowanym korpusie,
- generowanie próbek tekstu w stylu autora,
- ewaluację jakości generacji,
- przygotowanie demonstracji.

---

## Dane wejściowe

### Specyfikacja danych wejściowych
- Teksty literackie wybranego autora/autorów  
- Format: tekst  
- Język: polski / angielski  

### Wymagania dla danych
- brak metadanych,
- jednolity encoding,
- odpowiednia długość.

---

## Podejście techniczne

### Możliwe podejścia techniczne
- Fine-tuning większego modelu,
- Fine-tuning LoRA / PEFT,
- model znakowy LSTM / GRU,
- Transformer trenowany od zera.

---

## Metryki i ocena

### Możliwe metryki automatyczne
- perplexity,
- długość i struktura zdań,
- różnorodność słownictwa.

### Ocena jakościowa
- subiektywna ocena podobieństwa,
- porównanie z tekstami referencyjnymi,
- test Turinga w małej skali.

---

## Ograniczenia projektu

### Problemy i ograniczenia
- ograniczone zasoby obliczeniowe,
- dataset ograniczony zasobami,
- obiektywna ocena stylu literackiego.

---

## Rezultat końcowy

### Finalne, wymierne rezultaty:
- wytrenowany model generujący tekst,
- notebook / program umożliwiający generację,
- raport / prezentacja opisująca dane, model, wyniki oraz wnioski.
