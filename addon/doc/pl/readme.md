# Day of the week #

* Autorzy: Abdel, Noelia.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ten dodatek pomaga znaleźć dzień tygodnia odpowiadający wybranej dacie.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * A "Cancel" button to close the dialog.

* The second one named "dayOfTheWeek add-on settings" opens the parameters
  of the add-on to specify whether you want to report labels for date fields
  or not, it is composed of the following elements:

    * Enable accessibility of the date selector;
    * Level of the announces of labels, you will then have 3 choices:

        * Long (it's the default choice);
        * Short (for short announcements);
        * Off (to disable labels announcements).

    * Enable announcement of the current date field value only, when moving
      vertically;
    * An "OK" button to save your configuration;
    * A "Cancel" button to cancel and close the dialog.

## Uwagi ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* Od NVDA 2018.2, w meni dodatku znajduje się tylko jednen
  element. Ustawienia dodatku zostały dołączone do panelu ustawień NVDA.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Zmiany w wersji 6.0 ##

* Od wersji NVDA 2018.2, meni ustawień dodatku znajduje się w panelu
  ustawień NVDA;
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

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
