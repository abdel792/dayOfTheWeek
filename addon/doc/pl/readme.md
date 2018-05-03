# Day of the week #

*	 Autorzy: Abdel, Noelia.
*	 Pobierz [wersja stabilna][1]
*	 Pobierz [wersja rozwojowa][2]

Ten dodatek pomaga znaleźć dzień tygodnia odpowiadający wybranej dacie.

wtyczka dodaje do okna ustawień NVDA nowe podmenu o nazwie "Day of the
week", które zawiera 2 elementy:


*	Pierwszy element "Wyszukaj dzień", otwiera okno dialogowe, które zawiera 3 kontrolki:
	*	Listę do wybierania lub wpisywania daty;
	*	przycisk "OK" powodujący wyświetlenie pola wiadomości zawierającego dzień;
	*	i przycisk "Zrezygnuj," który zamyka okno dialogowe.
*	Drugi element nazwany "Ustawienia dayOfTheWeek" otwiera okno, w którym można zdecydować, czy oznaczenia w polach daty mają być wymawiane, czy nie. Okno to składa się z następujących elementów:
	*	Włącz dostępność selektora daty;
	*	Poziom oznajmiania oznaczania, gdzie do wyboru są 3 stopnie:
		*	Długi (jest wybrany domyślnie);
		*	Krótki (dla krótkich oznajmień);
		*	Wyłączony (Wyłącza oznajmianie oznaczeń).
	*	Włącz oznajmianie wartości aktualnego pola daty tylko przy poruszaniu się w pionie;
	*	 przycisk "OK" aby zapisać konfigurację;
	*	 Przycisk "Zrezygnuj" aby anulować i zamknąć okno dialogowe.


## Uwagi ##

*	 Można zamknąć te okna naciskając Escape.
*	 Można przypisać skrót klawiszowy służący do otwierania tych okien
   dialogowych w menu "Zdarzeniach Wejścia" a dokładniej w kategorii "Day of
   the week".

## Zmiany w wersji 5.0 ##

*	 Dodano zgodność z wxPython 4.0 i Python3;
*	 Poprawiono błąd dotyczący ścieżek dodatku, które zawierają znaki spoza
   łacińskiego alfabetu.

## Zmiany w wersji 4.0 ##

*	 Dodatek rozpoznaje już każdy regionalny format daty, który użytkownik
   może wybrać;
*	 Dodano zgodność wsteczną z wersjami NVDA starszymi niż 2016.4, które
   zawierały the gui.guiHelper module.

## Zmiany w wersji 3.1 ##

*	 Powróciliśmy do poprzedniego formatu the day of the week, ponieważ
   rozpoznaje on więcej języków;
*	 Poprawiono dostępność wybieracza daty pod względem rozpoznawania 3 pól
   'Dzień', 'Miesiąc' i 'Rok', oraz odpowiadających im wartości;
*	 Dodano metodę integracji języka Gruzińskiego w zakresie rozpoznawania dni
   tygodnia;
*	 Dodano okno dialogowe ustawień służące do włączania lub wyłączania
   dostępności selektora daty;
*	 Przeniesiono podmenu dodatku z "Narzędzi" do "Ustawień";
*	 Kategoria dodatku została zmieniona na "Day of the week".

## Zmiany w wersji 2.0 ##

*	 Użyto the gui.guiHelper module aby upewnić się, że okno dialogowe do
   wpisywania daty wygląda właściwie;
*	 Dodano licencję GPL;
*	 Przetłumaczono dni tygodnia, aby dodatek działał poprawnie w różnych
   językach;
*	 Zmieniono format dnia, aby uniknąć błędów w kodowaniu.

## Zmiany w wersji 1.0 ##

*	 Pierwsza wersja.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
