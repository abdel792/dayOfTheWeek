# Day of the week (Ugedag) #

* Forfattere: Abdel, Noelia.
* download [stabil version][1]
* download [udviklingsversion][2]

Med dette tilføjelsesprogram kan du finde den ugedag, som svarer til en
valgt dato.

Denne pakke tilføjer en undermenu i NVDA-menuen under Værktøjer ved navn
"Ugedag", der indeholder 2 elementer:

* Den første med navnet "Find en dag" åbner en dialog bestående af 3
  kontroller:

    * En listeboks, hvor du kan vælge eller indtaste din dato;
    * En OK-knap, som vil vise en meddelelsesboks med din ugedag;
    * En Annuller-knap, som lukker dialogen.

* Den anden med navnet "Indstillinger for tilføjelsesprogrammet Ugedag"
  åbner parametrene for tilføjelsen for at angive, om du vil have etiketter
  til datafelter oplyst eller ej. Den består af følgende indstillinger:

    * Gør datovælgeren tilgængelig;
    * Annonceringsniveau for etiketter har tre valg:

        * Lang (det er standardvalg);
        * Kort (for korte meddelelser);
        * Fra (Deaktiverer annoncering af etiketter).

    * Annoncér kun det aktuelle datofelt, når der flyttes &lodret;
    * En OK-knap der gemmer dine indstillinger;
    * En Annuller-knap, som lukker dialogen.

## Noter ##

* Du kan lukke disse dialoger bare ved at trykke på Escape.
* Du kan tilknytte en genvejstast til at åbne dialogen under
  Inputbevægelser, nærmere bestemt under kategorien "Ugedag";
* Hvis du bruger NVDA 2018.2 eller nyere, finder du kun et punkt i
  værktøjsmenuen for at søge efter dage, og tilføjelsesindstillingerne er i
  NVDA-indstillingspanelet.

## Kompatibilitet ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.3.

## Ændringer for 19.02 ##

* Ændret versionsnummerering til åå.MM (År i 2 cifre efterfulgt af et
  punktum, efterfulgt af måneden i 2 cifre);
* Tilføjede kompatibilitet med det nye versionsformat af der fra nu af
  benyttes i tilføjelser, der blev aktuelt siden NVDA 2019.1.

## Ændringer i 6.0 ##

* tilføjede tilføjelsesindstillingerne til NVDA indstillingspanelet for NVDA
  2018.2 og nyere;
* Flyttet punktet til at søge en dag til værktøjsmenuen;
* Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA versioner,
  der går forud for 2018.2, som omfatteder indstillingspanelet.

## Ændringer i 5.0 ##

* Tilføjet kompatibilitet af tilføjelsesprogrammet med wxPython 4.0 og
  Python3;
* Rettede en fejl med stier tilhørende tilføjelsespakken der indholder
  non-ASCII-tegn.

## Ændringer i4.0  ##

* Tilføjelsesprogrammet er nu i stand til at genkende alle de regionale
  datoformater, som brugeren kan vælge;
* Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA versioner,
  der gik forud for 2016.4, som omfattede gui.guiHelper modul.

## Ændringer i 3.1 ##

* Tilbage til det tidligere format for Ugedag, fordi det giver mulighed for
  at genkende et større antal sprog;
* Forbedret tilgængelighed af dato selector med anerkendelsen af de 3 felter
  'Dag', 'Måned' og 'År', og deres respektive værdier;
* Tilføjet en teknik til integrering af det georgiske sprog for anerkendelse
  af dagene i ugen;
* Tilføjet en konfigurationsdialog for at aktivere eller deaktivere
  tilgængeligheden af datovælgeren;
* Flyttede tilføjelsespakkens undermenu fra "Værktøjer" til "Indstillinger";
* Ændret tilføjelsespakkens kategori til "Ugedag".

## Ændringer i 2.0 ##

* Brugt modulet gui.guiHelper for at sikre den korrekte udseende i
  dialogboksen der beder om en dato;
* Tilføjet GPL-licensen til tilføjelsen;
* Ugedag er blevet oversat, således at tilføjelsen virker korrekt på de
  forskellige sprog;
* Ændret dagsformat for at undgå kodningsfejl.

## Ændringer i 1.0 ##

* Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
