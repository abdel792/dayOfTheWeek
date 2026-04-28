# Day of the week (Ugedag)

- Forfattere: Abdel, Noelia.

Med dette tilføjelsesprogram kan du finde den ugedag, som svarer til en
valgt dato.

Denne pakke tilføjer en undermenu i NVDA-menuen under Værktøjer ved navn
"Ugedag", der indeholder 2 elementer:

- Den første med navnet "Find en dag" åbner en dialog bestående af 3
  kontroller:

  - En listeboks, hvor du kan vælge eller indtaste din dato;
  - En OK-knap, som vil vise en meddelelsesboks med din ugedag;
  - En Annuller-knap, som lukker dialogen.

- The second one named "dayOfTheWeek add-on settings" opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:

  - Gør datovælgeren tilgængelig;

  - Annonceringsniveau for etiketter har tre valg:

    - Lang (det er standardvalg);
    - Kort (for korte meddelelser);
    - Fra (Deaktiverer annoncering af etiketter).

  - Annoncér kun det aktuelle datofelt, når der flyttes &lodret;

  - En OK-knap der gemmer dine indstillinger;

  - En Annuller-knap, som lukker dialogen.

## Noter

- Du kan lukke disse dialoger bare ved at trykke på Escape.
- Du kan tilknytte en genvejstast til at åbne dialogen under
  Inputbevægelser, nærmere bestemt under kategorien "Ugedag";
- Hvis du bruger NVDA 2018.2 eller nyere, finder du kun et punkt i
  værktøjsmenuen for at søge efter dage, og tilføjelsesindstillingerne er i
  NVDA-indstillingspanelet.

## Kompatibilitet

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

## Ændringer for 19.02

- Ændret versionsnummerering til åå.MM (År i 2 cifre efterfulgt af et
  punktum, efterfulgt af måneden i 2 cifre);

## Ændringer i 6.0

- tilføjede tilføjelsesindstillingerne til NVDA indstillingspanelet for NVDA
  2018.2 og nyere;
- Flyttet punktet til at søge en dag til værktøjsmenuen;

## Ændringer i 5.0

- Tilføjet kompatibilitet af tilføjelsesprogrammet med wxPython 4.0 og
  Python3;
- Rettede en fejl med stier tilhørende tilføjelsespakken der indholder
  non-ASCII-tegn.
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Ændringer i4.0

- Tilføjelsesprogrammet er nu i stand til at genkende alle de regionale
  datoformater, som brugeren kan vælge;
- Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA versioner,
  der gik forud for 2016.4, som omfattede gui.guiHelper modul.

## Ændringer i 3.1

- Tilbage til det tidligere format for Ugedag, fordi det giver mulighed for
  at genkende et større antal sprog;
- Forbedret tilgængelighed af dato selector med anerkendelsen af de 3 felter
  'Dag', 'Måned' og 'År', og deres respektive værdier;

## Ændringer i 2.0

- Brugt modulet gui.guiHelper for at sikre den korrekte udseende i
  dialogboksen der beder om en dato;
- Tilføjet GPL-licensen til tilføjelsen;
- Ugedag er blevet oversat, således at tilføjelsen virker korrekt på de
  forskellige sprog;
- Ændret dagsformat for at undgå kodningsfejl.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Ændringer i 1.0

- Første version.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
