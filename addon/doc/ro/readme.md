# Day of the week #

*	 Autori: Abdel, Noelia.
*	 Descărcați [versiunea stabilă][1]
*	 Descărcați [versiunea în dezvoltare][2]

Acest supliment vă permite să găsiți o zi din săptămână care corespunde cu o
dată aleasă.

El adaugă un element în NVDA, meniul preferințe, numit „Day of the week”,
care conține două elemente:


*	Primul se numește "caută o zi", deschide un dialog compus din 3 controale:
	*	O listă pentru alegerea sau tastarea datei;
	*	Un buton "OK" pentru afișarea unui mesaj care conține ziua;
	*	Un buton de anulare pentru închiderea dialogului.
*	Al doilea se numește "Setări dayOfTheWeek", deschide parametrii suplimentului pentru a specifica dacă vreți să raportați sau nu etichetele pentru câmpurile de dată, este compus din următoarele elemente:
	*	Activează accesibilitatea selectorului de dată;
	*	Nivelul de anunțări ale etichetelor, veți avea 3 alegeri:
		*	Lung (e alegerea implicită);
		*	Scurt (pentru anunțurile scurte);
		*	Dezactivat (pentru dezactivarea anunțurilor etichetelor).
	*	Activează doar anunțarea valorii câmpului de dată curent la deplasarea pe vertical;
	*	Un buton "OK" pentru salvarea configurației;
	*	Un buton de anulare pentru anularea modificărilor efectuate și închiderea dialogului.

## Note ##

*	 Puteți închide aceste dialoguri apăsând tasta Escape;
*	 Puteți aloca o comandă rapidă pentru a deschide dialogul în meniul
   „Gesturi de intrare” și, mai precis, în categoria /„Day of the Week/”;
*	 Dacă folosiți NVDA 2018.2 sau mai nou, veți găsi un singur element în
   meniul instrumente pentru căutarea zilei dumneavoastră, setările
   suplimentului vor fi în panoul de setări al NVDA.

## Modificări în versiunea 6.0 ##

*	 S-au adăugat setările suplimentului în de setări al NVDA pentru NVDA
   2018.2 și mai nou;
*	 Elementul pentru căutarea unei zile s-a mutat în meniul instrumente;
*	 A fost adăugată înapoi compatibilitatea suplimentului cu versiunile NVDA
   care au precedat versiunea 2018.2, care a inclus panoul de setări.

## Modificări în versiunea 5.0 ##

*	 S-a adăugat compatibilitatea suplimentului cu wxPython 4.0 și Python3.
*	 S-a rezolvat o problemă privind adresele suplimentului care conținea
   caractere non-ASCII

## Modificări în versiunea 4.0 ##

*	 Suplimentul poate recunoaște toate formatele datelor regionale p care le
   poate alege un utilizator;
*	 A fost adăugată înapoi compatibilitatea suplimentului cu versiunile NVDA
   care au precedat versiunea 2016.4, care a inclus modulul gui.guiHelper.

## Modificări în versiunea 3.1 ##

*	 S-a revenit la vechiul format al zilei săptămânii, deoarece permite
   recunoașterea unui număr mare de limbi;
*	 A fost îmbunătățită accesibilitatea selectorului de dată cu recunoașterea
   a trei câmpuri 'zi, 'lună' și 'an', dar și respectivele valori ale
   acestora;
*	 A fost adăugată o tehnică pentru integrarea limbii georgiene pentru
   recunoașterea zilelor săptămânii;
*	 A fost adăugat un dialog de configurare pentru activarea sau dezactivarea
   accesibilității selectorului de dată;
*	 Sub-meniul suplimentului a fost mutat din instrumente în preferințe.
*	 A fost schimbată categoria suplimentului în "Day of the week".

## Modificări în versiunea 2.0 ##

*	 A fost folosit modulul gui.guiHelper pentru a asigura aspectul corect al
   dialogului care cere o dată;
*	 A fost adăugată licența GPL pentru supliment;
*	 Zilele săptămânii au fost traduse, astfel încât suplimentul să
   funcționeze corect în diferite limbi;
*	 Formatul zilei a fost modificat pentru a evita erorile de codificare.

## Modificări în versiunea 1.0 ##

*	 Versiunea inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
