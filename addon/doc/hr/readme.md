# Dan u tjednu #

* Autori: Abdels, Noelia.
* preuzmi [stable version][1]
* preuzmi [development version][2]

Ovaj dodatak omogućuje vam da pronađete dan u tjednu koji odgovara odabranom
datumu.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * "Otkaži" gumb za zatvaranje dijaloškog okvira.

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

## Napomene ##

* You can close these dialogs just by pressing Escape;
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category;
* If you use NVDA 2018.2 or higher, you'll find only one item in the tool
  menu for searching your day, the add-on settings will be in the NVDA
  settings panel.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Changes for 6.0 ##

* added the addon settings to the NVDA settings panel for NVDA 2018.2 and
  higher;
* Moved the item for searching a day to the tools menu;
* Added the backward compatibility of the add-on with the NVDA versions that
  preceded 2018.2, which included the settings panel.

## Changes for 5.0 ##

* Dodana kompatibilnost dodatka sa wxPython 4.0 i Python 3;
* Ispravljena greška u dijelovima dodatka koji sadrže znakove koji nisu
  ASCi.

## Changes for 4.0 ##

* Dodatak sada može prepoznati sve regionalne formate datuma koje korisnik
  može odabrati;
* Dodatak je sada kompatibilan sa starijim inačicama NVDA, koje su
  uključivale gui.guiHelper

## Changes for 3.1 ##

* Povratak na prethodni format dana u tjednu, jer to omogućava prepoznavanje
  većeg broja jezika;
* Poboljšana pristupačnost polja za odabir datuma sa prepoznavanjem 3 polja:
  'Dan', 'Mjesec i 'Godina', te pripadajućih vrijednosti;
* Dodana tehnika za integriranje gruzijskog jezika za prepoznavanje dana u
  tjednu;
* Dodan podizbornik za omogućavanje ili onemogućavanje pristupačnosti polja
  za odabir datuma;
* Premješten podizbornik dodatka iz "Alati" u "Postavke";
* Premještena kategorija dodatka u "Dan u tjednu".

## Izmjene u inačici 2.0 ##

* Korišten je gui.guiHelper kako bi se pojavio ispravan dijaloški okvir za
  odabir datuma
* Dodana GPL licenca u dodatak
* Days of the week have been translated, so that the add-on works properly
  in the different languages;
* Changed the day format to avoid encoding errors.

## Promjene u 1.0 ##

* Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
