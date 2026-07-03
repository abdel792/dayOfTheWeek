# Deň v týždni #

* Vývojári: Abdel, Noelia.

Tento doplnok vám umožňuje nájsť deň v týždni zodpovedajúci zvolenému dátumu.

Pridáva podponuku do ponuky Nástroje NVDA s názvom „Deň v týždni“, ktorá obsahuje 2 položky:

* Prvá s názvom „Hľadať deň“, otvorí dialógové okno pozostávajúce z 3 ovládacích prvkov:

    * Zoznam na výber alebo zadanie dátumu;
    * Tlačidlo „OK“ na zobrazenie okna so správou obsahujúcou váš deň;
    * Tlačidlo „Zrušiť“ na zatvorenie dialógového okna.

* Druhá s názvom „Nastavenia doplnku dayOfTheWeek“ otvorí parametre doplnku, kde môžete určiť, či chcete oznamovať menovky polí dátumu alebo nie. Skladá sa z nasledujúcich prvkov:

    * Povoliť prístupnosť výberu dátumu;
    * Úroveň oznamovania menoviek, pričom budete mať na výber 3 možnosti:

        * Dlhé (toto je predvolená možnosť);
        * Krátke (pre krátke oznámenia);
        * Vypnuté (na zakázanie oznamovania menoviek).

    * Povoliť oznamovanie iba aktuálnej hodnoty poľa dátumu pri vertikálnom pohybe;
    * Tlačidlo „OK“ na uloženie vašej konfigurácie;
    * Tlačidlo „Zrušiť“ na zrušenie a zatvorenie dialógového okna.

## Poznámky ##

* Tieto dialógové okná môžete zatvoriť jednoduchým stlačením klávesu Escape;
* Skratku na otvorenie týchto dialógových okien môžete priradiť v ponuke „Vstupné gestá“ a presnejšie v kategórii „Deň v týždni“;
* Ak používate NVDA 2018.2 alebo novšiu verziu, v ponuke nástrojov nájdete iba jednu položku na vyhľadávanie dňa a nastavenia doplnku budú v paneli nastavení NVDA.

## Kompatibilita ##

* Tento doplnok je kompatibilný s verziami NVDA od 2019.3 a vyššími.

## Zmeny vo verzii 20240326.0.0

* Aktualizovaná kompatibilita pre nvda-2024.1.;
* Odstránený odkaz na stiahnutie zo súboru readme, odkaz na stiahnutie pre budúce aktualizácie bude teraz dostupný iba v obchode s doplnkami.

## Zmeny vo verzii 20231229.0.0 ##

* Pridaná spätne kompatibilná implementácia na podporu režimu reči na požiadanie, ktorý bude čoskoro dostupný s nvda-2024.1.

## Zmeny vo verzii 20231015.0.0 ##

* Opravená chyba zistená pri navigácii šípkou nahor z výberu dátumu v najnovších verziách NVDA.

## Zmeny vo verzii 20230728.0.0 ##

* Na kód boli aplikované pravidlá flake8 a mypy;
* Minimálna podporovaná verzia NVDA bola zmenená na 2019.3 na podporu anotácií zavedených v Pythone 3.

## Zmeny vo verzii 20230607.0.0 ##

* Pridané nasledujúce pracovné postupy (workflows):
 * auto-update-translations – na automatickú aktualizáciu prekladov zo systému prekladu NVDA.
 * release-on-tag..yaml: na zostavenie a publikovanie doplnku hneď po odoslaní nového tagu;
 * manual-release.yaml: na manuálne zostavenie a vydanie nových verzií doplnku.
* Aktualizované preklady.

## Zmeny vo verzii 20230508.0.0 a vyšších ##

* • Zmenené číslo verzie, minimálna verzia NVDA a odkaz na stiahnutie v súlade s konvenciami/požiadavkami obchodu.

## Zmeny vo verzii 19.02 ##

* Zmenené číslovanie verzií pomocou RR.MM (rok dvoma číslicami, nasleduje bodka, nasleduje mesiac dvoma číslicami);
* Pridaná kompatibilita s novým formátom verzií doplnkov, ktorý sa objavil od verzie nvda 2019.1.

## Zmeny vo verzii 6.0 ##

* Pridané nastavenia doplnku do panelu nastavení NVDA pre NVDA 2018.2 a vyššie;
* Položka na vyhľadávanie dňa bola presunutá do ponuky nástrojov;
* Pridaná spätná kompatibilita doplnku s verziami NVDA predchádzajúcimi verzii 2018.2, ktoré obsahovali panel nastavení.

## Zmeny vo verzii 5.0 ##

* Pridaná kompatibilita doplnku s wxPython 4.0 a Python3;
* Opravená chyba s cestami doplnku, ktoré obsahujú iné ako ASCII znaky.

## Zmeny vo verzii 4.0 ##

* Doplnok je teraz schopný rozpoznať všetky regionálne formáty dátumu, ktoré si používateľ môže vybrať;
* Pridaná spätná kompatibilita doplnku s verziami NVDA predchádzajúcimi verzii 2016.4, ktoré obsahovali modul gui.guiHelper.

## Zmeny vo verzii 3.1 ##

* Návrat k predchádzajúcemu formátu dňa v týždni, pretože umožňuje rozpoznanie väčšieho počtu jazykov;
* Vylepšená prístupnosť výberu dátumu s rozpoznávaním 3 polí „Deň“, „Mesiac“ a „Rok“ a ich príslušných hodnôt;
* Pridaná technika na integráciu gruzínskeho jazyka na rozpoznávanie dní v týždni;
* Pridané konfiguračné dialógové okno na povolenie alebo zakázanie prístupnosti výberu dátumu;
* Podponuka doplnku bola presunutá z „Nástroje“ do „Možnosti“;
* Kategória doplnku bola zmenená na „Deň v týždni“.

## Zmeny vo verzii 2.0 ##

* Použitý modul gui.guiHelper na zabezpečenie správneho vzhľadu dialógového okna požadujúceho dátum;
* Do doplnku bola pridaná licencia GPL;
* Dni v týždni boli preložené, aby doplnok správne fungoval v rôznych jazykoch;
* Zmenený formát dňa, aby sa predišlo chybám v kódovaní.

## Zmeny vo verzii 1.0 ##

* Počiatočná verzia.
