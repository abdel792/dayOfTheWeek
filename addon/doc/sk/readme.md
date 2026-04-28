# Deň v týždni

- Autori: Abdel, Noelia.

Doplnok umožňuje zistiť, ktorý deň pripadá na zadaný dátum.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing 2 items:

- Položka Hľadať deň otvorí dialóg, v ktorom sú tri prvky:

  - Zoznam, v ktorom môžete vybrať alebo zadať dátum;
  - Tlačidlo OK na zobrazenie dňa;
  - Tlačidlo Zrušiť na zatvorenie dialógu.

- Druhá položka s názvom Nastavenia deň v týždni obsahuje tieto možnosti:

  - Povoliť sprístupnenie prvku na výber dátumu;

  - Úroveň oznamovania prvkov, kde máte tri možnosti:

    - Dlhé (predvolená možnosť);
    - Krátke;
    - Vypnuté (na vypnutie oznamovania popiskov).

  - Počas nastavovania dátumu upozorniť na dnešný deň;

  - Tlačidlo OK na uloženie nastavení;

  - Tlačidlo zrušiť na zatvorenie dialógu.

## Poznámky

- Dialógi je možné zatvoriť tlačidlom escape;
- Skratky na vyvolanie dialógov doplnku je možné nastaviť v menu nvda >
  možnosti > Klávesové skratky, vo vetve Deň v týždni.
- If you use NVDA 2018.2 or higher, you'll find only one item in the tool menu for searching your day, the add-on settings will be in the NVDA settings panel.

## Kompatibilita

- This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0

- Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0

- Applied the flake8 and mypy rules to the code;
- Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond

- Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Verzia 19.02

- • Changed version number, minimum NVDA version and download link according to store conventions/requirements.

## Verzia 6.0

- Nastavenia pridané do stromu nastavení pre NVDA od verzie 2018.2;
- Položka vyhľadať deň presunutá do menu nástroje;

## Verzia 5.0

- Pridaná kompatibilita s rozhraním wxPython 4.0 a Python3;
- Opravené problémy, ktoré nastávali, ak sa doplnok pokúsil uložiť
  nastavenia a cesta obsahovala znaky mimo ascii rozsahu.
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Verzia 4.0

- Doplnok rozpoznáva všetky regionálne dátumy;
- Pridaná spätná kompatibilita s NVDA do verzie 2016.4, ktoré obsahovali
  modul gui.guiHelper.

## Verzia 3.1

- Vraciame sa k predošlému formátu doplnku, ktorý podporoval viacero
  jazykov;
- Upravená prístupnosť prvku na výber dátumu, kde je možné vyrbať deň,
  mesiac a rok;

## Verzia 2.0

- Upravený vzhľad dialógov použitím gui.guiHelper;
- Pridaná GPL licencia;
- Preloľžené dni, takže doplnok je možné používať vo viacerých jazykoch;
- Odstránené problémy s kódovaním.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Verzia 1.0

- Prvé vydanie.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
