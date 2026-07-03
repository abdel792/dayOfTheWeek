# Ugedag #

* Udviklere: Abdel, Noelia.

Denne tilføjelse giver dig mulighed for at finde ugedagen svarende til en valgt dato.

Den tilføjer en undermenu i NVDA-menuen Værktøjer med navnet "Ugedag", som indeholder 2 punkter:

* Det første kaldet "Søg efter en dag", åbner en dialogboks bestående af 3 kontrolelementer:

    * En listeboks til at vælge eller skrive din dato;
    * En "OK"-knap til at vise en meddelelsesboks, der indeholder din dag;
    * En "Annuller"-knap til at lukke dialogboksen.

* Det andet kaldet "Indstillinger for tilføjelsen Ugedag" åbner parametrene for tilføjelsen for at angive, om du vil rapportere mærkater for datofelter eller ej, den består af følgende elementer:

    * Aktiver tilgængelighed for datovælgeren;
    * Niveau for oplæsning af mærkater, hvor du derefter vil have 3 valgmuligheder:

        * Lang (det er standardvalget);
        * Kort (for korte meddelelser);
        * Fra (for at deaktivere oplæsning af mærkater).

    * Aktiver kun oplæsning af den aktuelle værdi i datofeltet, når du flytter dig lodret;
    * En "OK"-knap til at gemme din konfiguration;
    * En "Annuller"-knap til at annullere og lukke dialogboksen.

## Bemærkninger ##

* Du kan lukke disse dialogbokse blot ved at trykke på Escape;
* Du kan tildele en genvej til at åbne disse dialogbokse i menuen "Input-bevægelser" og, mere præcist, i kategorien "Ugedag";
* Hvis du bruger NVDA 2018.2 eller nyere, finder du kun ét punkt i værktøjsmenuen til at søge efter din dag, tilføjelsens indstillinger vil være i NVDA's indstillingspanel.

## Kompatibilitet ##

* Denne tilføjelse er kompatibel med versioner af NVDA fra 2019.3 og opefter.

## Ændringer for 20240326.0.0

* Opdateret kompatibilitet for nvda-2024.1.;
* Slettet downloadlink fra readme, downloadlinket til fremtidige opdateringer vil nu kun være tilgængeligt fra tilføjelsesbutikken.

## Ændringer for 20231229.0.0 ##

* Tilføjet en bagudkompatibel implementering til at understøtte tale-ved-efterspørgsel-tilstand, som snart vil være tilgængelig med nvda-2024.1.

## Ændringer for 20231015.0.0 ##

* Rettet en fejl registreret ved navigering med pil op fra datovælgeren i de nyeste versioner af NVDA.

## Ændringer for 20230728.0.0 ##

* Anvendt flake8- og mypy-regler på koden;
* Ændret den mindst understøttede NVDA-version til 2019.3 for at understøtte annoteringer introduceret i Python 3.

## Ændringer for 20230607.0.0 ##

* Tilføjet følgende arbejdsgange:
 * auto-update-translations - til automatisk at opdatere oversættelser fra NVDA's oversættelsessystem.
 * release-on-tag..yaml: til at bygge og udgive tilføjelsen, så snart et nyt tag pushes;
 * manual-release.yaml: til at bygge og udgive nye versioner af tilføjelsen manuelt.
* Opdaterede oversættelser.

## Ændringer for version 20230508.0.0 og opefter ##

* • Ændret versionsnummer, minimum NVDA-version og downloadlink i henhold til butikkens konventioner/krav.

## Ændringer for 19.02 ##

* Ændret versionsnummerering ved hjælp af ÅÅ.MM (Året med 2 cifre, efterfulgt af et punktum, efterfulgt af måneden med 2 cifre);
* Tilføjet kompatibilitet med det nye versionsformat for tilføjelser, der dukkede op siden nvda 2019.1.

## Ændringer for 6.0 ##

* Tilføjet tilføjelsens indstillinger til NVDA's indstillingspanel for NVDA 2018.2 og nyere;
* Flyttet punktet til at søge efter en dag til værktøjsmenuen;
* Tilføjet bagudkompatibilitet for tilføjelsen med de NVDA-versioner, der gik forud for 2018.2, som inkluderede indstillingspanelet.

## Ændringer for 5.0 ##

* Tilføjet kompatibilitet for tilføjelsen med wxPython 4.0 og Python3;
* Rettet en fejl med tilføjelsesstier, der indeholder ikke-ASCII-tegn.

## Ændringer for 4.0 ##

* Tilføjelsen er nu i stand til at genkende alle de regionale datoformater, som brugeren kan vælge;
* Tilføjet bagudkompatibilitet for tilføjelsen med de NVDA-versioner, der gik forud for 2016.4, som inkluderede modulet gui.guiHelper.

## Ændringer for 3.1 ##

* Tilbage til det foregående format for ugedagen, fordi det gør det muligt at genkende et større antal sprog;
* Forbedret tilgængeligheden af datovælgeren med genkendelse af de 3 felter 'Dag', 'Måned' og 'År' og deres respektive værdier;
* Tilføjet en teknik til integration af det georgiske sprog til genkendelse af ugedagene;
* Tilføjet en konfigurationsdialogboks til at aktivere eller deaktivere tilgængeligheden af datovælgeren;
* Flyttet tilføjelsens undermenu fra "Værktøjer" til "Præferencer";
* Ændret tilføjelsens kategori til "Ugedag".

## Ændringer for 2.0 ##

* Brugt modulet gui.guiHelper for at sikre det korrekte udseende af dialogboksen, der beder om en dato;
* Tilføjet GPL-licensen til tilføjelsen;
* Ugedage er blevet oversat, så tilføjelsen fungerer korrekt på de forskellige sprog;
* Ændret dagens format for at undgå kodningsfejl.

## Ændringer for 1.0 ##

* Første version.
