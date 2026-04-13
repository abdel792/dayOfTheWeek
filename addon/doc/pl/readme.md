# Day of the week #

* Autorzy: Abdel, Noelia.

Ten dodatek pomaga znaleźć dzień tygodnia odpowiadający wybranej dacie.

Dodaje podmenu w menu Narzędzia NVDA o nazwie "Dzień tygodnia", zawierające
2 pozycje:

* Pierwszy o nazwie "Wyszukaj dzień", otwiera okno dialogowe złożone z 3
  kontrolek:

    * Pole listy do wyboru lub wpisania daty;
    * Przycisk "OK" do wyświetlania messageBox zawierającego Twój dzień;
    * Przycisk "Anuluj", aby zamknąć okno dialogowe.

* Drugi o nazwie "dayOfTheWeek add-on settings" otwiera parametry dodatku,
  aby określić, czy chcesz raportować etykiety dla pól daty, czy nie, składa
  się z następujących elementów:

    * Włącz dostępność selektora daty;
    * Poziom ogłoszeń etykiet, będziesz miał wtedy 3 opcje:

        * Długi (jest to domyślny wybór);
        * Krótki (dla krótkich ogłoszeń);
        * Wyłączone (aby wyłączyć anonsy etykiet).

    * Włącz ogłaszanie bieżącej wartości pola daty tylko podczas przesuwania
      w pionie;
    * Przycisk "OK", aby zapisać konfigurację;
    * Przycisk "Anuluj", aby anulować i zamknąć okno dialogowe.

## Uwagi ##

* Możesz zamknąć te okna dialogowe, naciskając Escape;
* Możesz przypisać skrót do otwierania tych okien dialogowych w menu "Gesty
  wprowadzania", a dokładniej w kategorii "Dzień tygodnia";
* Od NVDA 2018.2, w meni dodatku znajduje się tylko jednen
  element. Ustawienia dodatku zostały dołączone do panelu ustawień NVDA.

## Zgodność ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Zmiany na 19.02 ##

* Zmieniono numerację wersji przy użyciu YY. MM (Rok w 2 cyfrach, po którym
  następuje kropka, a następnie miesiąc w 2 cyfrach);
* Dodano kompatybilność z nowym formatem wersjonowania dodatku, pojawił się
  od nvda 2019.1.

## Zmiany w wersji 6.0 ##

* dodano ustawienia dodatku do panelu ustawień NVDA dla NVDA 2018.2 i
  nowszych;
* Element służący do wyszukiwania został przeniesiony do meni Narzędzia;
* Dodano zgodność wsteczną z wersjami NVDA starszymi niż 2018.2, co dotyczy
  np. panelu ustawień.

## Zmiany w wersji 5.0 ##

* Dodano zgodność z wxPython 4.0 i Python3;
* Poprawiono błąd dotyczący ścieżek dodatku, które zawierają znaki spoza
  łacińskiego alfabetu.

## Zmiany w wersji 4.0 ##

* Dodatek rozpoznaje już każdy regionalny format daty, który użytkownik może
  wybrać;
* Dodano zgodność wsteczną z wersjami NVDA starszymi niż 2016.4, które
  zawierały the gui.guiHelper module.

## Zmiany w wersji 3.1 ##

* Powróciliśmy do poprzedniego formatu the day of the week, ponieważ
  rozpoznaje on więcej języków;
* Poprawiono dostępność wybieracza daty pod względem rozpoznawania trzech
  pól 'Dzień', 'Miesiąc' i 'Rok', oraz odpowiadających im wartości;
* Dodano metodę integracji języka Gruzińskiego w zakresie rozpoznawania dni
  tygodnia;
* Dodano okno dialogowe ustawień służące do włączania lub wyłączania
  dostępności selektora daty;
* Przeniesiono podmenu dodatku z "Narzędzi" do "Ustawień";
* Kategoria dodatku została zmieniona na "Day of the week".

## Zmiany w wersji 2.0 ##

* Użyto the gui.guiHelper module aby upewnić się, że okno dialogowe do
  wpisywania daty wygląda właściwie;
* Dodano licencję GPL;
* Przetłumaczono dni tygodnia, aby dodatek działał poprawnie w różnych
  językach;
* Zmieniono format dnia, aby uniknąć błędów w kodowaniu.

## Zmiany w wersji 1.0 ##

* Pierwsza wersja.

[[!tag dev stable]]
