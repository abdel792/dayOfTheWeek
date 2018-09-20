# Dan u tjednu #

*	 Autori: Abdels, Noelia.
*	 preuzmi [stable version][1]
*	 preuzmi [development version][2]

Ovaj dodatak omogućuje vam da pronađete dan u tjednu koji odgovara odabranom
datumu.

It adds a submenu in the NVDA Preferences menu named "Day of the week",
containing 2 items:


*	Prva stavka "Search a day", otvara dijaloški okvir koji se sastoji od 3 kontrole:
*	*	Popis za odabir ili unos datuma;
*	*	Gumb "u redu" koji prikazuje poruku s odabranim danom;
*	*	Gumb "Otkaži" koji zatvara dijaloški okvir;
*	Druga stavka "Postavke dodatka DayOfTheWeek" otvara parametre dodatka gdje možete odrediti želite li ili ne želite polja za unos vrijednosti datuma, sastoji se od sljedećih elemenata:
*	*	Omogući pristupačnost polja za odabir datuma;
*	*	Način izvještavanja o vrijednostima, ovdje ćete imati 3 mogućnosti izbora:
*	*	*	 Dugi (podrazumijevani izbor);
*	*	*	 Kratki (za kratko izvještavanje);
*	*	*	Isključeno (onemogućuje izgovaranje vrijednosti).
*	*	Omogući izgovaranje samo polja s trenutnim datumom tijekom kretanja vertikalno;
*	*	Gumb "U redu" koji sprema konfiguraciju;
*	*	 Gumb "Otkaži" koji otkazuje i zatvara dijaloški okvir.

## Napomene ##

*	 You can close these dialogs just by pressing Escape;
*	 You can assign a shortcut to open these dialogs in "Input gestures" menu
   and, more precisely, in the "Day of the week" category;
*	 If you use NVDA 2018.2 or higher, you'll find only one item in the tool
   menu for searching your day, the add-on settings will be in the NVDA
   settings panel.

## Changes for 6.0 ##

*	 added the addon settings to the NVDA settings panel for NVDA 2018.2 and
   higher;
*	 Moved the item for searching a day to the tools menu;
*	 Added the backward compatibility of the add-on with the NVDA versions
   that preceded 2018.2, which included the settings panel.

## Changes for 5.0 ##

*	 Dodana kompatibilnost dodatka sa wxPython 4.0 i Python 3;
*	 Ispravljena greška u dijelovima dodatka koji sadrže znakove koji nisu
   ASCi.

## Changes for 4.0 ##

*	 Dodatak sada može prepoznati sve regionalne formate datuma koje korisnik
   može odabrati;
*	 Dodatak je sada kompatibilan sa starijim inačicama NVDA, koje su
   uključivale gui.guiHelper

## Changes for 3.1 ##

*	 Povratak na prethodni format dana u tjednu, jer to omogućava
   prepoznavanje većeg broja jezika;
*	 Poboljšana pristupačnost polja za odabir datuma sa prepoznavanjem 3
   polja: 'Dan', 'Mjesec i 'Godina', te pripadajućih vrijednosti;
*	 Dodana tehnika za integriranje gruzijskog jezika za prepoznavanje dana u
   tjednu;
*	 Dodan podizbornik za omogućavanje ili onemogućavanje pristupačnosti polja
   za odabir datuma;
*	 Premješten podizbornik dodatka iz "Alati" u "Postavke";
*	 Premještena kategorija dodatka u "Dan u tjednu".

## Izmjene u inačici 2.0 ##

*	 Korišten je gui.guiHelper kako bi se pojavio ispravan dijaloški okvir za
   odabir datuma
*	 Dodana GPL licenca u dodatak
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Changed the day format to avoid encoding errors.

## Promjene u 1.0 ##

*	 Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
