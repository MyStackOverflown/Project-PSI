# Syntetyczny Pisarz

Projekt obejmuje pełen proces służący do budowy, uczenia oraz ewaluacji modelu sieci rekurencyjnej LSTM. Model uczy się struktury języka bezpośrednio na poziomie pojedynczych znaków, rekonstruując unikalny styl literacki.

---

## Architektura modelu

* Embedding: 512 wymiarowe ciągłe wektory gęste dla 90 unikalnych znaków.
* LSTM: Pojedyncza warstwa zawierająca 2048 jednostek, zdolna do przetwarzania kontekstu sekwencyjnego.
* Dense: Aktywacja Softmax zwracająca rozkład prawdopodobieństwa dla kolejnego znaku.
* Params: 21 210 202, 100% trenowalnych.

---

## Struktura projektu

```
Project-PSI/
├── data/
│   ├── raw/                 # Surowe pliki tekstowe
│   └── processed/           # Skonsolidowany i oczyszczony tekst
├── models/
│   ├── checkpoints/         # Punkty kontrolne zapisywane po każdej epoce
│   └── final/               # Ostateczny model
├── notebooks/
│   ├── 01_cleaning.ipynb    # Czyszczenie tekstu
│   ├── 02_dataset.ipynb     # Tokenizacja i mapowania
│   ├── 03_model.ipynb       # Definicja i kompilacja architektury
│   ├── 04_training.ipynb    # Pętla treningowa i wykresy zbieżności
│   └── 05_evaluation.ipynb  # Inferencja i próbkowanie tekstu
├── src/                     # Kod źródłowy modułów pomocniczych
└── README.md                # Dokumentacja projektu
```

---

## Przygotowanie Środowiska i Uruchomienie

* Projekt został przystosowany do pracy w chmurze Google Colab przy użyciu akceleracji sprzętowej GPU oraz integracji z Dyskiem Google.
* Skopiuj cały folder Project-PSI do swojego głównego katalogu na Dysku Google, zachowując powyższą strukturę.
* Każdy z notatników w katalogu notebooks/ posiada zaimplementowany na wstępie niezależny fragment kodu automatycznie montujący Dysk Google i ustawiający ścieżkę roboczą.

---

## Testowanie i Inferencja

Ostatni moduł odpowiada za ładowanie wag produkcyjnych z pliku .keras i generowanie próbek tekstu. Wykorzystuje on mechanizm próbkowania autoregresyjnego z parametrem temperatury.
