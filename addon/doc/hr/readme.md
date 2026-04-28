# Dan u tjednu (Day of the week)

- Autori: Abdels, Noelia.

S ovim dodatkom je moguće naći dan u tjednu za određeni datum.

U NVDA izborniku „Alati” dodaje podizbornik „Dan u tjednu”, koji sadrži
dvije stavke:

- The first one named "Search a day", opens a dialog composed of 3 controls:

  - Popisni okvir s mogućnošću biranja ili upisivanja datuma;
  - Gumb „U redu” za prikaz poruke koja sadrži tvoj dan;
  - Gumb „Odustani” za zatvaranje dijaloškog okvira.

- The second one named "dayOfTheWeek add-on settings" opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:

  - Uključi pristupačnost za odabir datuma;

  - Razina najave oznaka, za koju postoje tri opcije:

    - Dugo (ovo je standardni izbor);
    - Kratko (za kratke izgovore);
    - Isključeno (deaktivira izgovaranje oznaka).

  - Uključi izgovaranje datuma trenutačnog polja samo pri okomitom
    kretanju;

  - Gumb „U redu” za spremanje konfiguracije;

  - Gumb „Odustani” za prekid i zatvaranje dijaloškog okvira.

## Napomene

- Ove dijaloške okvire je moguće zatvoriti jednostavnim pritiskom tipke
  Escape;
- Moguće je odrediti tipovnički prečac za otvaranje dijaloškog okvira u
  izborniku „Ulazne geste” i još preciznije, u kategoriji „Dan u tjednu”;
- If you use NVDA 2018.2 or higher, you'll find only one item in the tool menu for searching your day, the add-on settings will be in the NVDA settings panel.

## Kompatibilnost

- Ovaj je dodatak kompatibilan s NVDA verzijom 2019.3 i novijim verzijama.

## Promjene u 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Promjene u 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Promjene u 20231015.0.0

- Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Promjene u 20230728.0.0

- Programskom kodu su dodana flake8 i mypy pravila;
- Namjanja podržana NVDA verzija je promijenjena na 2019.3 kako bi se
  podržale zabilješke koje su uvedene u Python 3.

## Promjene u 20230508.0.0 i novijim verzijama

- Promijenjen je broj verzije, minimalna NVDA verzija i poveznica za
  preuzimanje prema konvencijama/zahtjevima trgovine.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Promjene u 19.02

- Promijenjeno je numeriranje verzija koristeći YY.MM (Dvije znamenke za
  godinu, slijedi točka, a zatim dvije znamenke za mjesec);

## Promjene u 6.0

- postavke dodatka su dodane u ploču NVDA postavki za NVDA verziju 2018.2 i
  noviju;
- Stavka za traženje dana je promještena u izbornik „Alati”;

## Promjene u 5.0

- Dodana je kompatibilnost sa wxPython 4.0 i Python 3;
- Ispravljena greška u dijelovima dodatka koji sadrže znakove koji nisu
  ASCII.
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Promjene u 4.0

- Dodatak sada može prepoznati sve regionalne formate datuma koje korisnik
  može odabrati;
- Dodatak je sada kompatibilan sa NVDA verzijama starijima od 2016.4, koje
  su uključivale modul gui.guiHelper.

## Promjene u 3.1

- Povratak na prethodni format dana u tjednu, jer to omogućava prepoznavanje
  većeg broja jezika;
- Poboljšana pristupačnost za odabir datuma s prepoznavanjem triju polja:
  „Dan”, „Mjesec” i „Godina”, te pripadajućih vrijednosti;

## Promjene u 2.0

- Korišten je gui.guiHelper kako bi se pojavio ispravan dijaloški okvir za
  odabir datuma;
- Dodana GPL licenca u dodatak;
- Dani u tjednu su prevedeni, tako da dodatak sada radi ispravno na
  različitim jezicima;
- Promijenjen je format za dan, kako bi se izbjegle greške u kodiranju.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Promjene u 1.0

- Prva verzija.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
