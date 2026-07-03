# Ziua săptămânii #

* Dezvoltatori: Abdel, Noelia.

Această extensie vă permite să găsiți ziua săptămânii corespunzătoare unei date alese.

Ea adaugă un submeniu în meniul Instrumente al NVDA numit „Ziua săptămânii”, care conține 2 elemente:

* Primul, numit „Caută o zi”, deschide o casetă de dialog compusă din 3 controale:

    * O casetă de listă pentru a alege sau a tasta data;
    * Un buton „OK” pentru a afișa o casetă de mesaj care conține ziua dumneavoastră;
    * Un buton „Anulează” pentru a închide caseta de dialog.

* Al doilea, numit „Setările extensiei dayOfTheWeek”, deschide parametrii extensiei pentru a specifica dacă doriți sau nu să anunțați etichetele câmpurilor de dată, fiind compus din următoarele elemente:

    * Activează accesibilitatea selectorului de dată;
    * Nivelul de anunțare a etichetelor, unde veți avea 3 opțiuni:

        * Lung (aceasta este opțiunea implicită);
        * Scurt (pentru anunțuri scurte);
        * Dezactivat (pentru a dezactiva anunțurile etichetelor).

    * Activează anunțarea doar a valorii câmpului de dată curent, atunci când vă deplasați pe verticală;
    * Un buton „OK” pentru a salva configurația;
    * Un buton „Anulează” pentru a anula și a închide caseta de dialog.

## Note ##

* Puteți închide aceste casete de dialog pur și simplu apăsând tasta Escape;
* Puteți atribui o comandă rapidă pentru a deschide aceste casete de dialog în meniul „Gesturi de introducere” și, mai exact, în categoria „Ziua săptămânii”;
* Dacă utilizați NVDA 2018.2 sau o versiune ulterioară, veți găsi un singur element în meniul de instrumente pentru a căuta ziua, iar setările extensiei vor fi în panoul de setări NVDA.

## Compatibilitate ##

* Această extensie este compatibilă cu versiunile NVDA începând de la 2019.3 și ulterioare.

## Modificări pentru 20240326.0.0

* S-a actualizat compatibilitatea pentru nvda-2024.1.;
* S-a șters linkul de descărcare din readme, linkul de descărcare pentru actualizările viitoare va fi acum disponibil doar din magazinul de extensii.

## Modificări pentru 20231229.0.0 ##

* S-a adăugat o implementare compatibilă cu versiunile anterioare pentru a asigura suportul modului de vorbire la cerere, care va fi disponibil în curând împreună cu versiunea nvda-2024.1.

## Modificări pentru 20231015.0.0 ##

* S-a remediat o eroare detectată la navigarea cu săgeată în sus din selectorul de dată în cele mai recente versiuni de NVDA.

## Modificări pentru 20230728.0.0 ##

* S-au aplicat regulile flake8 și mypy asupra codului;
* S-a modificat versiunea minimă de NVDA suportată la 2019.3 pentru a asigura suportul adnotărilor introduse în Python 3.

## Modificări pentru 20230607.0.0 ##

* S-au adăugat următoarele fluxuri de lucru (workflows):
 * auto-update-translations - pentru a actualiza automat traducerile din sistemul de traducere al NVDA.
 * release-on-tag..yaml: pentru a construi și a publica extensia de îndată ce este trimis un nou tag;
 * manual-release.yaml: pentru a construi și a lansa manual noi versiuni ale extensiei.
* Traduceri actualizate.

## Modificări pentru versiunea 20230508.0.0 și ulterioare ##

* • S-au modificat numărul versiunii, versiunea minimă de NVDA și linkul de descărcare în conformitate cu convențiile/cerințele magazinului.

## Modificări pentru 19.02 ##

* S-a modificat numerotarea versiunilor folosind AA.LL (Anul din 2 cifre, urmat de punct, urmat de luna din 2 cifre);
* S-a adăugat compatibilitatea cu noul format de versiune pentru extensii, apărut începând cu versiunea nvda 2019.1.

## Modificări pentru 6.0 ##

* S-au adăugat setările extensiei în panoul de setări NVDA pentru NVDA 2018.2 și versiuni ulterioare;
* S-a mutat elementul pentru căutarea unei zile în meniul instrumente;
* S-a adăugat compatibilitatea cu versiunile anterioare ale extensiei pentru versiunile NVDA precedente celei 2018.2, care includeau panoul de setări.

## Modificări pentru 5.0 ##

* S-a adăugat compatibilitatea extensiei cu wxPython 4.0 și Python3;
* S-a remediat o eroare legată de căile extensiei care conțin caractere non-ASCII.

## Modificări pentru 4.0 ##

* Extensia este acum capabilă să recunoască toate formatele de dată regionale pe care utilizatorul le poate alege;
* S-a adăugat compatibilitatea cu versiunile anterioare ale extensiei pentru versiunile NVDA precedente celei 2016.4, care includeau modulul gui.guiHelper.

## Modificări pentru 3.1 ##

* Revenire la formatul anterior pentru ziua săptămânii, deoarece acesta permite recunoașterea unui număr mai mare de limbi;
* S-a îmbunătățit accesibilitatea selectorului de dată prin recunoașterea celor 3 câmpuri „Zi”, „Lună” și „An” și a valorilor respective ale acestora;
* S-a adăugat o tehnică pentru integrarea limbii georgiene în vederea recunoașterii zilelor săptămânii;
* S-a adăugat o casetă de dialog de configurare pentru a activa sau a dezactiva accesibilitatea selectorului de dată;
* S-a mutat submeniul extensiei din „Instrumente” în „Preferințe”;
* S-a modificat categoria extensiei în „Ziua săptămânii”.

## Modificări pentru 2.0 ##

* S-a utilizat modulul gui.guiHelper pentru a asigura aspectul corect al casetei de dialog care solicită o dată;
* S-a adăugat licența GPL la extensie;
* Zilele săptămânii au fost traduse, astfel încât extensia să funcționeze corect în diferitele limbi;
* S-a modificat formatul zilei pentru a evita erorile de codare.

## Modificări pentru 1.0 ##

* Versiune inițială.
