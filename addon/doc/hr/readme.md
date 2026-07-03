# Dan u tjednu #

* Razvijatelji: Abdel, Noelia.

Ovaj dodatak omogućuje vam pronalaženje dana u tjednu koji odgovara odabranom datumu.

Dodaje podizbornik u NVDA izbornik Alati pod nazivom "Dan u tjednu", koji sadrži 2 stavke:

* Prva pod nazivom "Traži dan", otvara dijaloški okvir koji se sastoji od 3 kontrole:

    * Okvir s popisom za odabir ili upisivanje vašeg datuma;
    * Gumb "U redu" za prikaz okvira s porukom koja sadrži vaš dan;
    * Gumb "Odustani" za zatvaranje dijaloškog okvira.

* Druga pod nazivom "Postavke dodatka dayOfTheWeek" otvara parametre dodatka kako biste odredili želite li prijaviti oznake za polja datuma ili ne, a sastoji se od sljedećih elemenata:

    * Omogući pristupačnost birača datuma;
    * Razina najave oznaka, tada ćete imati 3 izbora:

        * Dugo (to je zadani izbor);
        * Kratko (za kratke najave);
        * Isključeno (za onemogućavanje najave oznaka).

    * Omogući najavu samo trenutne vrijednosti polja datuma, prilikom okomitog pomicanja;
    * Gumb "U redu" za spremanje vaše konfiguracije;
    * Gumb "Odustani" za odustajanje i zatvaranje dijaloškog okvira.

## Napomene ##

* Ove dijaloške okvire možete zatvoriti jednostavnim pritiskom na tipku Escape;
* Možete dodijeliti prečac za otvaranje ovih dijaloških okvira u izborniku "Ulazne geste" i, točnije, u kategoriji "Dan u tjednu";
* Ako koristite NVDA 2018.2 ili noviju verziju, pronaći ćete samo jednu stavku u izborniku alata za pretraživanje vašeg dana, postavke dodatka bit će na ploči s postavkama NVDA.

## Kompatibilnost ##

* Ovaj dodatak je kompatibilan s verzijama NVDA u rasponu od 2019.3 i novijim.

## Promjene za 20240326.0.0

* Ažurirana kompatibilnost za nvda-2024.1.;
* Izbrisana poveznica za preuzimanje iz datoteke readme, poveznica za preuzimanje za buduća ažuriranja sada će biti dostupna samo u trgovini dodataka.

## Promjene za 20231229.0.0 ##

* Dodana unazadna kompatibilna implementacija za podršku načina govora na zahtjev, koji će uskoro biti dostupan s nvda-2024.1.

## Promjene za 20231015.0.0 ##

* Ispravljena pogreška otkrivena prilikom navigacije strelicom prema gore iz birača datuma u najnovijim verzijama NVDA.

## Promjene za 20230728.0.0 ##

* Primijenjena pravila flake8 i mypy na kôd;
* Promijenjena minimalna podržana verzija NVDA na 2019.3 radi podrške za anotacije uvedene u Pythonu 3.

## Promjene za 20230607.0.0 ##

* Dodani sljedeći tijekovi rada:
 * auto-update-translations - za automatsko ažuriranje prijevoda iz NVDA sustava za prevođenje.
 * release-on-tag..yaml: za izgradnju i objavljivanje dodatka čim se pošalje nova oznaka;
 * manual-release.yaml: za ručnu izgradnju i objavljivanje novih verzija dodatka.
* Ažurirani prijevodi.

## Promjene za verziju 20230508.0.0 i novije ##

* • Promijenjen broj verzije, minimalna verzija NVDA i poveznica za preuzimanje u skladu s konvencijama/zahtjevima trgovine.

## Promjene za 19.02 ##

* Promijenjeno numeriranje verzija pomoću GG.MM (Godina u 2 znamenke, nakon koje slijedi točka, nakon koje slijedi mjesec u 2 znamenke);
* Dodana kompatibilnost s novim formatom označavanja verzija dodataka, koji se pojavio od verzije nvda 2019.1.

## Promjene za 6.0 ##

* Dodane postavke dodatka na ploču s postavkama NVDA za NVDA 2018.2 i novije;
* Premještena stavka za traženje dana u izbornik alata;
* Dodana unazadna kompatibilnost dodatka s verzijama NVDA koje su prethodile verziji 2018.2, a koje su uključivale ploču s postavkama.

## Promjene za 5.0 ##

* Dodana kompatibilnost dodatka s wxPythonom 4.0 i Pythonom 3;
* Ispravljena pogreška s putanjama dodatka koje sadrže znakove koji nisu ASCII.

## Promjene za 4.0 ##

* Dodatak sada može prepoznati sve regionalne formate datuma koje korisnik može odabrati;
* Dodana unazadna kompatibilnost dodatka s verzijama NVDA koje su prethodile verziji 2016.4, a koje su uključivale modul gui.guiHelper.

## Promjene za 3.1 ##

* Povratak na prethodni format za dan u tjednu jer omogućuje prepoznavanje većeg broja jezika;
* Poboljšana pristupačnost birača datuma s prepoznavanjem 3 polja 'Dan', 'Mjesec' i 'Godina' te njihovih odgovarajućih vrijednosti;
* Dodana tehnika za integraciju gruzijskog jezika za prepoznavanje dana u tjednu;
* Dodan konfiguracijski dijaloški okvir za omogućavanje ili onemogućavanje pristupačnosti birača datuma;
* Premješten podizbornik dodatka iz "Alati" u "Preferences";
* Promijenjena kategorija dodatka u "Dan u tjednu".

## Promjene za 2.0 ##

* Korišten modul gui.guiHelper kako bi se osigurao ispravan izgled dijaloškog okvira koji traži datum;
* Dodana GPL licenca dodatku;
* Dani u tjednu su prevedeni kako bi dodatak ispravno radio na različitim jezicima;
* Promijenjen format dana kako bi se izbjegle pogreške u kodiranju.

## Promjene za 1.0 ##

* Početna verzija.
