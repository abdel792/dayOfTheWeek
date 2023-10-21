# Day of the week #

* Autori: Abdel, Noelia.
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest supliment vă permite să găsiți o zi din săptămână care corespunde cu o
dată aleasă.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * Un buton „Anulare” pentru a închide dialogul.

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

## Note ##

* You can close these dialogs just by pressing Escape;
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category;
* Dacă folosiți NVDA 2018.2 sau mai nou, veți găsi un singur element în
  meniul instrumente pentru căutarea zilei dumneavoastră, setările
  suplimentului vor fi în panoul de setări al NVDA.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* � Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Modificări în versiunea 6.0 ##

* S-au adăugat setările suplimentului în de setări al NVDA pentru NVDA
  2018.2 și mai nou;
* Elementul pentru căutarea unei zile s-a mutat în meniul instrumente;
* A fost adăugată înapoi compatibilitatea suplimentului cu versiunile NVDA
  care au precedat versiunea 2018.2, care a inclus panoul de setări.

## Modificări în versiunea 5.0 ##

* S-a adăugat compatibilitatea suplimentului cu wxPython 4.0 și Python3.
* S-a rezolvat o problemă privind adresele suplimentului care conținea
  caractere non-ASCII

## Modificări în versiunea 4.0 ##

* Suplimentul poate recunoaște toate formatele datelor regionale p care le
  poate alege un utilizator;
* A fost adăugată înapoi compatibilitatea suplimentului cu versiunile NVDA
  care au precedat versiunea 2016.4, care a inclus modulul gui.guiHelper.

## Modificări în versiunea 3.1 ##

* S-a revenit la vechiul format al zilei săptămânii, deoarece permite
  recunoașterea unui număr mare de limbi;
* A fost îmbunătățită accesibilitatea selectorului de dată cu recunoașterea
  a trei câmpuri 'zi, 'lună' și 'an', dar și respectivele valori ale
  acestora;
* A fost adăugată o tehnică pentru integrarea limbii georgiene pentru
  recunoașterea zilelor săptămânii;
* A fost adăugat un dialog de configurare pentru activarea sau dezactivarea
  accesibilității selectorului de dată;
* Sub-meniul suplimentului a fost mutat din instrumente în preferințe.
* A fost schimbată categoria suplimentului în "Day of the week".

## Modificări în versiunea 2.0 ##

* A fost folosit modulul gui.guiHelper pentru a asigura aspectul corect al
  dialogului care cere o dată;
* A fost adăugată licența GPL pentru supliment;
* Zilele săptămânii au fost traduse, astfel încât suplimentul să funcționeze
  corect în diferite limbi;
* Formatul zilei a fost modificat pentru a evita erorile de codificare.

## Modificări în versiunea 1.0 ##

* Versiunea inițială.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
