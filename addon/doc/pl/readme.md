# Dzień tygodnia #

* Autorzy: Abdel, Noelia.

Ten dodatek umożliwia znalezienie dnia tygodnia odpowiadającego wybranej dacie.

Dodaje on podmenu w menu Narzędzia NVDA o nazwie „Dzień tygodnia”, zawierające 2 elementy:

* Pierwszy o nazwie „Szukaj dnia”, otwiera okno dialogowe składające się z 3 elementów sterujących:

    * Listę rozwijaną do wyboru lub wpisania daty;
    * Przycisk „OK”, aby wyświetlić komunikat zawierający Twój dzień;
    * Przycisk „Anuluj”, aby zamknąć okno dialogowe.

* Drugi o nazwie „Ustawienia dodatku dayOfTheWeek” otwiera parametry dodatku, umożliwiając określenie, czy chcesz zgłaszać etykiety pól daty, czy nie. Składa się z następujących elementów:

    * Włącz dostępność selektora daty;
    * Poziom ogłaszania etykiet, do wyboru są 3 opcje:

        * Długie (opcja domyślna);
        * Krótkie (dla krótkich komunikatów);
        * Wyłączone (aby wyłączyć ogłaszanie etykiet).

    * Włącz ogłaszanie tylko bieżącej wartości pola daty podczas przemieszczania się w pionie;
    * Przycisk „OK”, aby zapisać konfigurację;
    * Przycisk „Anuluj”, aby anulować i zamknąć okno dialogowe.

## Uwagi ##

* Możesz zamknąć te okna dialogowe, naciskając klawisz Escape;
* Możesz przypisać skrót do otwierania tych okien dialogowych w menu „Zdarzenia wejściowe”, a dokładniej w kategorii „Dzień tygodnia”;
* Jeśli używasz NVDA 2018.2 lub nowszego, w menu narzędzi znajdziesz tylko jeden element do wyszukiwania dnia, a ustawienia dodatku będą znajdować się w panelu ustawień NVDA.

## Kompatybilność ##

* Ten dodatek jest kompatybilny z wersjami NVDA od 2019.3 i nowszymi.

## Zmiany w wersji 20240326.0.0

* Zaktualizowano kompatybilność z wersją nvda-2024.1.;
* Usunięto link do pobierania z pliku readme, link do pobierania przyszłych aktualizacji będzie teraz dostępny wyłącznie w sklepie z dodatkami.

## Zmiany w wersji 20231229.0.0 ##

* Dodano wstecznie kompatybilną implementację wspierającą tryb mowy na żądanie, który wkrótce będzie dostępny w nvda-2024.1.

## Zmiany w wersji 20231015.0.0 ##

* Naprawiono błąd wykryty podczas nawigacji strzałką w górę z selektora daty w najnowszych wersjach NVDA.

## Zmiany w wersji 20230728.0.0 ##

* Zastosowano reguły flake8 i mypy do kodu;
* Zmieniono minimalną obsługiwaną wersję NVDA na 2019.3, aby wspierać adnotacje wprowadzone w Pythonie 3.

## Zmiany w wersji 20230607.0.0 ##

* Dodano następujące przepływy pracy (workflows):
 * auto-update-translations - do automatycznej aktualizacji tłumaczeń z systemu tłumaczeń NVDA.
 * release-on-tag..yaml: do budowania i publikowania dodatku natychmiast po przesłaniu nowego tagu;
 * manual-release.yaml: do ręcznego budowania i wydawania nowych wersji dodatku.
* Zaktualizowano tłumaczenia.

## Zmiany w wersji 20230508.0.0 i nowszych ##

* • Zmieniono numer wersji, minimalną wersję NVDA oraz link do pobierania zgodnie z konwencjami/wymogami sklepu.

## Zmiany w wersji 19.02 ##

* Zmieniono numerację wersji na format RR.MM (rok zapisany dwoma cyframi, po którym następuje kropka, a następnie miesiąc zapisany dwoma cyframi);
* Dodano kompatybilność z nowym formatem wersji dodatków, który pojawił się od wersji nvda 2019.1.

## Zmiany w wersji 6.0 ##

* Dodano ustawienia dodatku do panelu ustawień NVDA dla wersji NVDA 2018.2 i nowszych;
* Przeniesiono element wyszukiwania dnia do menu narzędzi;
* Dodano wsteczną kompatybilność dodatku z wersjami NVDA poprzedzającymi 2018.2, które zawierały panel ustawień.

## Zmiany w wersji 5.0 ##

* Dodano kompatybilność dodatku z wxPython 4.0 i Python3;
* Naprawiono błąd związany ze ścieżkami dodatku zawierającymi znaki spoza zestawu ASCII.

## Zmiany w wersji 4.0 ##

* Dodatek jest teraz w stanie rozpoznać wszystkie regionalne formaty daty, które użytkownik może wybrać;
* Dodano wsteczną kompatybilność dodatku z wersjami NVDA poprzedzającymi 2016.4, które zawierały moduł gui.guiHelper.

## Zmiany w wersji 3.1 ##

* Powrócono do poprzedniego formatu dnia tygodnia, ponieważ pozwala on na rozpoznawanie większej liczby języków;
* Poprawiono dostępność selektora daty dzięki rozpoznawaniu 3 pól: „Dzień”, „Miesiąc” i „Rok” oraz ich odpowiednich wartości;
* Dodano technikę integracji języka gruzińskiego do rozpoznawania dni tygodnia;
* Dodano okno dialogowe konfiguracji umożliwiające włączenie lub wyłączenie dostępności selektora daty;
* Przeniesiono podmenu dodatku z „Narzędzia” do „Opcje”;
* Zmieniono kategorię dodatku na „Dzień tygodnia”.

## Zmiany w wersji 2.0 ##

* Użyto modułu gui.guiHelper w celu zapewnienia prawidłowego wyglądu okna dialogowego z pytaniem o datę;
* Dodano licencję GPL do dodatku;
* Dni tygodnia zostały przetłumaczone, dzięki czemu dodatek działa poprawnie w różnych językach;
* Zmieniono format dnia, aby uniknąć błędów kodowania.

## Zmiany w wersji 1.0 ##

* Wersja początkowa.
