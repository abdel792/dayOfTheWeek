# Dan u tjednu (Day of the week) #

* Autori: Abdels, Noelia.

S ovim dodatkom je moguće naći dan u tjednu za određeni datum.

U NVDA izborniku „Alati” dodaje podizbornik „Dan u tjednu”, koji sadrži
dvije stavke:

* Prva stavka se zove „Traži dan”. Otvara dijaloški okvir s tri kontrole:

    * Popisni okvir s mogućnošću biranja ili upisivanja datuma;
    * Gumb „U redu” za prikaz poruke koja sadrži tvoj dan;
    * Gumb „Odustani” za zatvaranje dijaloškog okvira.

* Druga stavka se zove „Postavke dodatka Dan u tjednu”. Otvara parametre
  dodatka za određivanje izgovaranja ili neizgovaranja oznaka za polja
  datuma. Sastoji se od sljedećih elemenata:

    * Uključi pristupačnost za odabir datuma;
    * Razina najave oznaka, za koju postoje tri opcije:

        * Dugo (ovo je standardni izbor);
        * Kratko (za kratke izgovore);
        * Isključeno (deaktivira izgovaranje oznaka).

    * Uključi izgovaranje datuma trenutačnog polja samo pri okomitom
      kretanju;
    * Gumb „U redu” za spremanje konfiguracije;
    * Gumb „Odustani” za prekid i zatvaranje dijaloškog okvira.

## Napomene ##

* Ove dijaloške okvire je moguće zatvoriti jednostavnim pritiskom tipke
  Escape;
* Moguće je odrediti tipovnički prečac za otvaranje dijaloškog okvira u
  izborniku „Ulazne geste” i još preciznije, u kategoriji „Dan u tjednu”;
* Ako se koristi NVDA verzija 2018.2 ili novija, u izborniku će se prikazati
  samo jedna stavka za traženje dana. Postavke dodatka se nalaze u ploči
  NVDA postavki.

## Kompatibilnost ##

* Ovaj je dodatak kompatibilan s NVDA verzijom 2019.3 i novijim verzijama.

## Promjene u 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Promjene u 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Promjene u 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Promjene u 20230728.0.0 ##

* Programskom kodu su dodana flake8 i mypy pravila;
* Namjanja podržana NVDA verzija je promijenjena na 2019.3 kako bi se
  podržale zabilješke koje su uvedene u Python 3.

## Promjene u 20230508.0.0 i novijim verzijama ##

* Promijenjen je broj verzije, minimalna NVDA verzija i poveznica za
  preuzimanje prema konvencijama/zahtjevima trgovine.

## Promjene u 19.02 ##

* Promijenjeno je numeriranje verzija koristeći YY.MM (Dvije znamenke za
  godinu, slijedi točka, a zatim dvije znamenke za mjesec);
* Dodana je kompatibilnost s novim formatom za određivanje verzije, pojavila
  se u nvda 2019.1.

## Promjene u 6.0 ##

* postavke dodatka su dodane u ploču NVDA postavki za NVDA verziju 2018.2 i
  noviju;
* Stavka za traženje dana je promještena u izbornik „Alati”;
* Dodatak je sada kompatibilan sa NVDA verzijama starijima od 2018.2, koje
  su uključivale ploču s postavkama.

## Promjene u 5.0 ##

* Dodana je kompatibilnost sa wxPython 4.0 i Python 3;
* Ispravljena greška u dijelovima dodatka koji sadrže znakove koji nisu
  ASCII.

## Promjene u 4.0 ##

* Dodatak sada može prepoznati sve regionalne formate datuma koje korisnik
  može odabrati;
* Dodatak je sada kompatibilan sa NVDA verzijama starijima od 2016.4, koje
  su uključivale modul gui.guiHelper.

## Promjene u 3.1 ##

* Povratak na prethodni format dana u tjednu, jer to omogućava prepoznavanje
  većeg broja jezika;
* Poboljšana pristupačnost za odabir datuma s prepoznavanjem triju polja:
  „Dan”, „Mjesec” i „Godina”, te pripadajućih vrijednosti;
* Dodana tehnika za integriranje gruzijskog jezika za prepoznavanje dana u
  tjednu;
* Dodan podizbornik za omogućavanje ili onemogućavanje pristupačnosti polja
  za odabir datuma;
* Premješten podizbornik dodatka iz „Alati” u „Postavke”;
* Premještena kategorija dodatka u „Dan u tjednu”.

## Promjene u 2.0 ##

* Korišten je gui.guiHelper kako bi se pojavio ispravan dijaloški okvir za
  odabir datuma;
* Dodana GPL licenca u dodatak;
* Dani u tjednu su prevedeni, tako da dodatak sada radi ispravno na
  različitim jezicima;
* Promijenjen je format za dan, kako bi se izbjegle greške u kodiranju.

## Promjene u 1.0 ##

* Prva verzija.

[[!tag dev stable]]
