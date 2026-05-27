# Raport z realizacji projektu

## Wykorzystanie metod głębokiego uczenia do analizy i syntezy stylu literackiego

### Mateusz Żydek, Jan Pawelec

---

## 1. Cel projektu i założenia teoretyczne

Celem projektu było zaprojektowanie, implementacja oraz pełne wytrenowanie od zera znakowego modelu językowego (Char-level Language Model) opartego na architekturze sieci rekurencyjnej LSTM. Zgodnie z analizą wymagań, system miał za zadanie imitować unikalny styl literacki George'a R.R. Martina na podstawie jego sagi fantasy. 

W przeciwieństwie do podejść wykorzystujących gotowe, duże modele językowe (LLM) poddawane fine-tuningowi, model ten nie posiada wstępnej wiedzy o słowach, gramatyce czy interpunkcji, uczy się korelacji i prawdopodobieństwa wystąpienia kolejnej litery lub znaku na podstawie sekwencji poprzednich.

Trudność zadania polega na tym, że sieć musi samodzielnie opanować składnię, ortografię oraz specyficzne cechy stylu autora, takie jak archaizmy, konstrukcje dialogowe, specyficzną budowę świata przedstawionego, strukturę opisu postaci, a także jedzenia.

---

## 2. Przetwarzanie danych wejściowych

Proces przetwarzania danych został podzielony na odizolowane moduły zapewniające powtarzalność procesu:

* Konsolidacja datasetu: Tomy sagi w formie tekstowej zostały scalone i oczyszczone z metadanych, reklam i spisów treści, a następnie ujednolicono je do kodowania UTF-8 i zapisano wynik.
* Analiza statystyczna i tokenizacja: Łączny rozmiar tekstu wyniósł 9 637 016 znaków, rozmiar słownika wyniósł 90 unikalnych znaków, dodatkowo zbudowano dwukierunkowe mapowania indeksów (char2idx) oraz (idx2char) w celu zamiany tekstu na reprezentacje numeryczne.
* Konstrukcja strumienia danych: Wygenerowano sekwencje treningowe, których długość ustawiono na 100 znaków, a dane pakowano w paczki o rozmiarze 64 ze stałym buforem mieszania 10000.

---

## 3. Architektura Sieci Neuronowej

Model został zaimplementowany przy użyciu interfejsu funkcjonalnego Keras:

* Input Layer: Przyjmuje tensory o kształcie (64, None), umożliwiając podawanie sekwencji o zmiennej długości.
* Embedding Layer: Mapuje 90 unikalnych znaków na 512-wymiarowe ciągłe wektory gęste, łącznie 46080 parametrów.
* LSTM Layer: Kluczowy element architektury składający się z 2048 jednostek LSTM. Tak duża pojemność warstwy pozwala na zapamiętywanie długoterminowych zależności w tekście, łącznie 20 979 712 parametrów.
* Dense Layer: Warstwa gęsta z aktywacją typu Softmax, rzutująca przestrzeń ukrytą z powrotem na 90 klas prawdopodobieństwa kolejnego znaku, łącznie 184410 parametrów.

Podsumowanie parametrów:
* Wszystkie parametry: 21210202.
* Parametry trenowalne: 21210202.
* Parametry nietrenowalne: 0.

---

## 4. Proces treningowy i analiza zbieżności

Trening modelu przeprowadzono na przestrzeni 10 epok przy użyciu optymalizatora Adam oraz funkcji straty Sparse Categorical Crossentropy. Stan sieci był zabezpieczany po każdej epoce za pomocą mechanizmu punktów kontrolnych zapisywanych do Dysku Google.

Zarejestrowane logi zbieżności funkcji straty prezentują się następująco:

* Epoka 1/10: Czas: 476s | loss: 1.5470
* Epoka 2/10: Czas: 483s | loss: 1.2113
* Epoka 3/10: Czas: 483s | loss: 1.1490
* Epoka 4/10: Czas: 484s | loss: 1.1107
* Epoka 5/10: Czas: 483s | loss: 1.0811
* Epoka 6/10: Czas: 482s | loss: 1.0559
* Epoka 7/10: Czas: 482s | loss: 1.0352
* Epoka 8/10: Czas: 484s | loss: 1.0171
* Epoka 9/10: Czas: 484s | loss: 1.0023
* Epoka 10/10: Czas: 483s | loss: 0.9904

Wnioski z przebiegu treningu:

Stabilny spadek wartości błędu z poziomu 1.5470 do wartości końcowej 0.9904 potwierdza prawidłowy dobór parametrów uczenia oraz zbieżność modelu. Sieć przeszła przez fazy nauki, a ostateczny model zapisano do pliku.

---

## 5. Wyniki jakościowe i ewaluacja

Analiza wygenerowanych przez model próbek dostarczyła kluczowe dowody sukcesu projektu. Przy niskich i umiarkowanych temperaturach próbkowania model generuje w pełni poprawne gramatycznie i ortograficznie wyrazy w języku angielskim.

Co najważniejsze, model zaczął poprawnie odtwarzać unikalne, strukturalne fragmenty książek Martina. Poniżej znajduje się wygenerowany fragment:

```
Robert Baratheon and his sons and serving wenches and the sons of the Lord of Light, before the Dornishmen had been sent to the Wall and the streets and the stormlands they had been sent to the stables and the rest of the Seven Kingdoms. The sons of the sea was still a boy of eight, a squire to Ser Kevan Lannister,
-{SER HOBBER REDWYNE, Lord of the Dreadfort,
-{SER GERALD GOODBROOK}, a boy of twelve,
-ROLAND CRAKEHALL, Lord of the Eyrie,
-his uncle, SER AXELL FLORENT, former sellswords,
```

Interpretacja wyniku:

* Model bezbłędnie kojarzy nazwy własne i pojęcia ze świata sagi (Robert Baratheon, Lord of the Light, Dornishmen, The Wall, Seven Kingdoms).
* Architektura LSTM o pojemności 2048 jednostek zdołała odwzorować rzadko występujący w tekście spis postaci.
* Pomimo licznych nawiązań do nazw oraz pojęć ze świata sagi model nie jest w stanie wygenerować spójnego narracyjnie oraz fabularnie fragmentu.

---

## 6. Podsumowanie i wnioski końcowe

Projekt zakończył się technicznie pełnym sukcesem. Znakowy model LSTM udowodnił swoje działanie w niszowych zadaniach syntezy stylu literackiego. Ze względu na dużą zasobożerność operacji rekurencyjnych, wdrożenie bezinterfejsowe oparte na chmurze Google Colab i montowaniu wolumenów Google Drive zapewniło kompromis pomiędzy wydajnością, mobilnością i powtarzalnością wyników.
