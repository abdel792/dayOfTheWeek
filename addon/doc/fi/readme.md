# Viikonpäivä #

* Tekijät: Abdel, Noelia.
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tällä lisäosalla on mahdollista selvittää valittua päivämäärää vastaava
viikonpäivä.

NVDA:n Työkalut-valikkoon lisätään Viikonpäivä-alavalikko, jossa on kaksi
kohdetta:

* Ensimmäinen, "Hae päivä", avaa valintaikkunan, jossa on kolme säädintä:

    * Listaruutu, josta voi valita tai johon voi kirjoittaa päivämäärän;
    * OK-painike, jota painettaessa tulee näkyviin valitun päivän näyttävä
      ilmoitusruutu;
    * Peruuta-painike, joka sulkee valintaikkunan.

* Toinen, "dayOfTheWeek-lisäosan asetukset", avaa lisäosan asetukset, joilla
  voi määrittää, ilmoitetaanko päivämääräkenttien selitteet vai
  ei. Valintaikkunassa on seuraavat osat:

    * Ota käyttöön päivämäärävalitsimen saavutettavuus;
    * Seliteilmoitusten taso, jossa on kolme vaihtoehtoa:

        * Pitkä (oletusarvoisesti valittuna);
        * Lyhyt (lyhyet ilmoitukset);
        * Ei käytössä (poistaa seliteilmoitukset käytöstä).

    * Ota käyttöön nykyisen päivämääräkentän arvon ilmoittaminen vain
      pystysuunnassa liikuttaessa;
    * OK-painike, jota painettaessa asetukset tallennetaan;
    * Peruuta-painike, joka peruuttaa ja sulkee valintaikkunan.

## Huomautuksia ##

* Valintaikkunat voidaan sulkea painamalla Esc-näppäintä;
* Valintaikkunoiden avaamista varten on mahdollista määrittää näppäinkomento
  Syötekomennot-valintaikkunan Viikonpäivä-kategoriasta;
* Mikäli käytössä on NVDA 2018.2 tai uudempi, Työkalut-valikossa on nyt vain
  yksi vaihtoehto päivän etsimiseen. Lisäosan asetukset löytyvät NVDA:n
  asetuspaneelista.

## Yhteensopivuus ##

* NVDA:n versiot 2014.3-2019.1 ovat yhteensopivia tämän lisäosan kanssa.

## Muutokset versiossa 19.02 ##

* Versionumerointi muutettu muotoon vv.kk (vuosi kahdella numerolla, piste
  ja kuukausi kahdella numerolla);
* Lisätty yhteensopivuus lisäosien uudelle versionumeroinnille, joka
  otettiin käyttöön NVDA 2019.1:ssä.

## Muutokset versiossa 6.0 ##

* Lisäosan asetukset lisätty NVDA:n asetuspaneeliin versiossa 2018.2 ja
  uudemmissa;
* Siirretty päivän etsimiseen tarkoitettu vaihtoehto Työkalut-valikkoon;
* Lisätty taaksepäin yhteensopivuus NVDA 2018.2:ta edeltäneille versioille.

## Muutokset versiossa 5.0 ##

* Lisätty wxPython 4.0:n ja Python 3:n yhteensopivuus;
* Korjattu bugi, jota esiintyi, kun lisäosan hakemistopoluissa oli muita
  kuin ASCII-merkkejä.

## Muutokset versiossa 4.0 ##

* Lisäosa tunnistaa nyt kaikki käyttäjän valittavissa olevat alueelliset
  päivämäärämuodot;
* Lisätty taaksepäin yhteensopivuus gui.guiHelper-moduulin sisältävää NVDA
  2016.4:ää vanhemmille versioille.

## Muutokset versiossa 3.1 ##

* Palattu viikonpäivän vanhaan muotoon, koska se mahdollistaa useamman
  kielen tunnistamisen;
* Paranneltu päivämäärävalitsimen saavutettavuutta "Päivä"-, "Kuukausi"- ja
  "Vuosi"-kenttien sekä niiden arvojen tunnistamisessa;
* Lisätty tekniikka georgian kielen integroimiseen viikonpäivien
  tunnistamista varten;
* Lisätty asetusvalintaikkuna päivämäärävalitsimen saavutettavuuden käyttöön
  ottamiseen tai käytöstä poistamiseen;
* Lisäosan alavalikko siirretty "Työkalut"-valikosta "Asetukset"-valikkoon;
* Lisäosan kategoriaksi muutettu "Viikonpäivä".

## Muutokset versiossa 2.0 ##

* Päivämääränkyselyvalintaikkunan asianmukaisen ulkoasun varmistamiseen
  käytetään gui.guiHelper-moduulia;
* Lisätty GPL-lisenssi;
* Viikonpäivät on käännetty, jotta lisäosa toimii oikein eri kielillä;
* Päivän muotoa muutettu koodausvirheiden välttämiseksi.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
