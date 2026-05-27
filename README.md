# Syntetyczny Pisarz

Projekt obejmuje pełen proces służący do budowy, uczenia oraz ewaluacji modelu sieci rekurencyjnej LSTM. Model uczy się struktury języka bezpośrednio na poziomie pojedynczych znaków. Pozwala to na automatyczne odtworzenie stylu, składni, interpunkcji oraz unikalnych cech dowolnego autora na podstawie dostarczonego korpusu tekstowego.

---

## Architektura modelu

Model został zaimplementowany przy użyciu interfejsu funkcjonalnego Keras. Pipeline umożliwia elastyczne dostosowanie parametrów sieci w zależności od zbioru danych:

* Embedding Layer: Mapuje unikalne znaki wykryte w tekście na ciągłe wektory gęste.
* LSTM Layer: Odpowiada za przetwarzanie i zapamiętywanie zależności następujących po sobie w tekście.
* Dense Layer: Aktywacja Softmax zwracająca rozkład prawdopodobieństwa dla kolejnego znaku.

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

Ostatni moduł odpowiada za ładowanie wag z pliku .keras i generowanie próbek tekstu, na podstawie zadanego mu kontekstu. Wykorzystuje on mechanizm próbkowania autoregresyjnego z parametrem temperatury:

* Niska temperatura: Model wybiera najbardziej prawdopodobne znaki, co skutkuje tekstem o wysokiej poprawności gramatycznej i ortograficznej. Sieć silnie odtwarza powtarzalne struktury tekstowe, najczęstsze zwroty oraz specyficzne formatowanie tekstu źródłowego.
* Wysoka temperatura: Zwiększa losowość i różnorodność doboru słownictwa, co sprzyja większej unikalności generowanych zdań, ale przy zbyt wysokich wartościach rośnie ryzyko powstawania błędów i sztucznych słów, co wynika ze znakowej natury sieci.
* Charakterystyka architektury: Model doskonale mapuje styl zdań, interpunkcję oraz unikalny klimat tekstu. Ze względu na brak globalnego mechanizmu uwagi, wygenerowany tekst po danej liczbie znaków traci spójność, co jest cechą znakowych modeli rekurenycjnych.
