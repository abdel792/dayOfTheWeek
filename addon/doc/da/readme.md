# Day of the week (Ugedag) #

*	 Forfattere: Abdel, Noelia.
*	 download [stabil version][1]
*	 download [udviklingsversion][2]

Med dette tilføjelsesprogram kan du finde den ugedag, som svarer til en
valgt dato.

Det tilføjer en undermenu i NVDA-menuen under indstillinger ved navn
"Ugedag", der indeholder 2 elementer:


*	Den første ved navn "Find en dag" åbner en dialog med tre kontrolelementer:
	*	En listboks der lader dig vælge eller indtaste en dato;
	*	En "ok" knap der viser din dato;
	*	Knappen "afbryd" der lader dig lukke dialogen.
*	Den anden ved navn "Indstillinger for tilføjelsesprogrammet Ugedag" åbner en dialog, hvor du kan beslutte om du ønsker at få etiketter for datofelter oplyst eller ej. Dialogen består af følgende:
	*	Gør datovælgeren tilgængelig;
	*	Annonceringsniveau for etiketter, hvor du har tre muligheder:
		*	Lang: Dette er standardindstillingen;
		*	Kort: For korte meddelelser;
		*	Fra: Slår annoncering af etiketter fra.
	*	Kun annoncering af datofeltet, når der flyttes lodret;
	*	Og knappen "ok" for at gemme din konfiguration;
	*	Knappen "afbryd" for at lukke dialogen og annullere dine ændringer.

## Noter ##

*	 Du kan lukke disse dialoger bare ved at trykke på Escape;
*	 Du kan tilknytte en genvejstast til at åbne dialogen under
   Inputbevægelser, nærmere bestemt under kategorien "Ugedag";
*	 Hvis du bruger NVDA 2018.2 eller nyere, finder du kun et punkt i
   værktøjsmenuen for at søge efter dage, og tilføjelsesindstillingerne er i
   NVDA-indstillingspanelet.

## Ændringer i 6.0 ##

*	 tilføjede tilføjelsesindstillingerne til NVDA indstillingspanelet for
   NVDA 2018.2 og nyere;
*	 Flyttet punktet til at søge en dag til værktøjsmenuen;
*	 Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA
   versioner, der går forud for 2018.2, som omfatteder indstillingspanelet.

## Ændringer i 5.0 ##

*	 Tilføjet kompatibilitet af tilføjelsesprogrammet med wxPython 4.0 og
   Python3;
*	 Rettede en fejl med stier tilhørende tilføjelsespakken der indholder
   non-ASCII-tegn.

## Ændringer i4.0  ##

*	 Tilføjelsesprogrammet er nu i stand til at genkende alle de regionale
   datoformater, som brugeren kan vælge;
*	 Tilføjet bagudkompatibilitet for tilføjelsesprogrammet med NVDA
   versioner, der gik forud for 2016.4, som omfattede gui.guiHelper modul.

## Ændringer i 3.1 ##

*	 Tilbage til det tidligere format for Ugedag, fordi det giver mulighed for
   at genkende et større antal sprog;
*	 Forbedret tilgængelighed af dato selector med anerkendelsen af de 3
   felter 'Dag', 'Måned' og 'År', og deres respektive værdier;
*	 Tilføjet en teknik til integrering af det georgiske sprog for
   anerkendelse af dagene i ugen;
*	 Tilføjet en konfigurationsdialog for at aktivere eller deaktivere
   tilgængeligheden af datovælgeren;
*	 Flyttede tilføjelsespakkens undermenu fra "Værktøjer" til
   "Indstillinger";
*	 Ændret tilføjelsespakkens kategori til "Ugedag".

## Ændringer i 2.0 ##

*	 Brugt modulet gui.guiHelper for at sikre den korrekte udseende i
   dialogboksen der beder om en dato;
*	 Tilføjet GPL-licensen til tilføjelsen;
*	 Ugedag er blevet oversat, således at tilføjelsen virker korrekt på de
   forskellige sprog;
*	 Ændret dagsformat for at undgå kodningsfejl.

## Ændringer i 1.0 ##

*	 Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
