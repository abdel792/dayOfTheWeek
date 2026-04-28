# Day of the week

- Autori: Abdel, Noelia.

Acest supliment vă permite să găsiți o zi din săptămână care corespunde cu o
dată aleasă.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

- The first one named "Search a day", opens a dialog composed of 3 controls:

  - A listbox to choose or type your date;
  - An "OK" button to display a messageBox containing your day;
  - Un buton „Anulare” pentru a închide dialogul.

- The second one named "dayOfTheWeek add-on settings" opens the parameters
  of the add-on to specify whether you want to report labels for date fields
  or not, it is composed of the following elements:

  - Enable accessibility of the date selector;

  - Level of the announces of labels, you will then have 3 choices:

    - Long (it's the default choice);
    - Short (for short announcements);
    - Off (to disable labels announcements).

  - Enable announcement of the current date field value only, when moving
    vertically;

  - An "OK" button to save your configuration;

  - A "Cancel" button to cancel and close the dialog.

## Note

- You can close these dialogs just by pressing Escape;
- You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category;
- Dacă folosiți NVDA 2018.2 sau mai nou, veți găsi un singur element în
  meniul instrumente pentru căutarea zilei dumneavoastră, setările
  suplimentului vor fi în panoul de setări al NVDA.

## Compatibility

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

## Changes for version 20230508.0.0 and beyond

- Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);

## Changes for 19.02

- S-au adăugat setările suplimentului în de setări al NVDA pentru NVDA
  2018.2 și mai nou;
- Elementul pentru căutarea unei zile s-a mutat în meniul instrumente;

## Modificări în versiunea 5.0

- S-a adăugat compatibilitatea suplimentului cu wxPython 4.0 și Python3.
- S-a rezolvat o problemă privind adresele suplimentului care conținea
  caractere non-ASCII
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Modificări în versiunea 4.0

- Suplimentul poate recunoaște toate formatele datelor regionale p care le
  poate alege un utilizator;
- A fost adăugată înapoi compatibilitatea suplimentului cu versiunile NVDA
  care au precedat versiunea 2016.4, care a inclus modulul gui.guiHelper.

## Modificări în versiunea 3.1

- S-a revenit la vechiul format al zilei săptămânii, deoarece permite
  recunoașterea unui număr mare de limbi;
- A fost îmbunătățită accesibilitatea selectorului de dată cu recunoașterea
  a trei câmpuri 'zi, 'lună' și 'an', dar și respectivele valori ale
  acestora;

## Modificări în versiunea 2.0

- A fost folosit modulul gui.guiHelper pentru a asigura aspectul corect al
  dialogului care cere o dată;
- A fost adăugată licența GPL pentru supliment;
- Zilele săptămânii au fost traduse, astfel încât suplimentul să funcționeze
  corect în diferite limbi;
- Formatul zilei a fost modificat pentru a evita erorile de codificare.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Modificări în versiunea 1.0

- Versiunea inițială.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
