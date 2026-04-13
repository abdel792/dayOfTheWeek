# Deň v týždni #

* Autori: Abdel, Noelia.

Doplnok umožňuje zistiť, ktorý deň pripadá na zadaný dátum.

V menu NVDA > nástroje pribudne ponuka Deň v týždni. V tejto ponuke sú
dostupné dve položky:

* Položka Hľadať deň otvorí dialóg, v ktorom sú tri prvky:

    * Zoznam, v ktorom môžete vybrať alebo zadať dátum;
    * Tlačidlo OK na zobrazenie dňa;
    * Tlačidlo Zrušiť na zatvorenie dialógu.

* Druhá položka s názvom Nastavenia deň v týždni obsahuje tieto možnosti:

    * Povoliť sprístupnenie prvku na výber dátumu;
    * Úroveň oznamovania prvkov, kde máte tri možnosti:

        * Dlhé (predvolená možnosť);
        * Krátke;
        * Vypnuté (na vypnutie oznamovania popiskov).

    * Počas nastavovania dátumu upozorniť na dnešný deň;
    * Tlačidlo OK na uloženie nastavení;
    * Tlačidlo zrušiť na zatvorenie dialógu.

## Poznámky ##

* Dialógi je možné zatvoriť tlačidlom escape;
* Skratky na vyvolanie dialógov doplnku je možné nastaviť v menu nvda >
  možnosti > Klávesové skratky, vo vetve Deň v týždni.
* Od verzie NVDA 2018.2 je v menu nástroje v podmenu doplnku len jedna
  položka. Nastavenia sú v strome s nastaveniami NVDA.

## Kompatibilita ##

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

## Verzia 19.02 ##

* Upravené číslovanie verzie. Používame tvar YY.MM (dve číslice pre rok a
  dve pre mesiac);
* Pridaná podpora pre nové zadávanie verzií doplnkov predstavené v NVDA
  2019.1.

## Verzia 6.0 ##

* Nastavenia pridané do stromu nastavení pre NVDA od verzie 2018.2;
* Položka vyhľadať deň presunutá do menu nástroje;
* Pridaná spätná kompatibilita so staršími verziami NVDA pred 2018.2;

## Verzia 5.0 ##

* Pridaná kompatibilita s rozhraním wxPython 4.0 a Python3;
* Opravené problémy, ktoré nastávali, ak sa doplnok pokúsil uložiť
  nastavenia a cesta obsahovala znaky mimo ascii rozsahu.

## Verzia 4.0 ##

* Doplnok rozpoznáva všetky regionálne dátumy;
* Pridaná spätná kompatibilita s NVDA do verzie 2016.4, ktoré obsahovali
  modul gui.guiHelper.

## Verzia 3.1 ##

* Vraciame sa k predošlému formátu doplnku, ktorý podporoval viacero
  jazykov;
* Upravená prístupnosť prvku na výber dátumu, kde je možné vyrbať deň,
  mesiac a rok;
* Doplnok dokáže oznamovať dni v Gruzínčine;
* Pridaná možnosť nastaviť prístupnosť prvku na výber dátumu;
* Nastavenia doplnku presunuté z menu nástroje do menu možnosti;
* Zmenená kategória v dialógu klávesové skratky.

## Verzia 2.0 ##

* Upravený vzhľad dialógov použitím gui.guiHelper;
* Pridaná GPL licencia;
* Preloľžené dni, takže doplnok je možné používať vo viacerých jazykoch;
* Odstránené problémy s kódovaním.

## Verzia 1.0 ##

* Prvé vydanie.

[[!tag dev stable]]
