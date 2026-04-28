# Viikonpäivä

- Tekijät: Abdel, Noelia.

Tällä lisäosalla on mahdollista selvittää valittua päivämäärää vastaava
viikonpäivä.

NVDA:n Työkalut-valikkoon lisätään Viikonpäivä-alavalikko, jossa on kaksi
kohdetta:

- Ensimmäinen, "Hae päivä", avaa valintaikkunan, jossa on kolme säädintä:

  - Listaruutu, josta voi valita tai johon voi kirjoittaa päivämäärän;
  - OK-painike, jota painettaessa tulee näkyviin valitun päivän näyttävä
    ilmoitusruutu;
  - Peruuta-painike, joka sulkee valintaikkunan.

- The second one named "dayOfTheWeek add-on settings" opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:

  - Ota käyttöön päivämäärävalitsimen saavutettavuus;

  - Seliteilmoitusten taso, jossa on kolme vaihtoehtoa:

    - Pitkä (oletusarvoisesti valittuna);
    - Lyhyt (lyhyet ilmoitukset);
    - Ei käytössä (poistaa seliteilmoitukset käytöstä).

  - Ota käyttöön nykyisen päivämääräkentän arvon ilmoittaminen vain
    pystysuunnassa liikuttaessa;

  - OK-painike, jota painettaessa asetukset tallennetaan;

  - Peruuta-painike, joka peruuttaa ja sulkee valintaikkunan.

## Huomautuksia

- Valintaikkunat voidaan sulkea painamalla Esc-näppäintä;
- Valintaikkunoiden avaamista varten on mahdollista määrittää näppäinkomento
  Näppäinkomennot-valintaikkunan Viikonpäivä-kategoriasta;
- If you use NVDA 2018.2 or higher, you'll find only one item in the tool menu for searching your day, the add-on settings will be in the NVDA settings panel.

## Yhteensopivuus

- Tämä lisäosa on yhteensopiva NVDA 2019.3:n ja sitä uudempien versioiden
  kanssa.

## Muutokset versiossa 20240326.0.0

- Päivitetty yhteensopivuus NVDA 2024.1:lle.
- Deleted download link from readme, the download link for future updates will now only be available from the add-on store.

## Muutokset versiossa 20231229.0.0

- Lisätty taaksepäin yhteensopiva toteutus pyydettäessä-puhetilalle, joka on
  pian saatavilla NVDA 2024.1:ssä.

## Muutokset versiossa 20231015.0.0

- Korjattu bugi, joka ilmeni liikuttaessa ylänuolinäppäimellä
  päivämääränvalitsimessa NVDA:n uusimpia versioita käytettäessä.

## Muutokset versiossa 20230728.0.0

- Sovellettu koodiin flake8- ja mypy-sääntöjä.
- Muutettu NVDA:n tuetuksi vähimmäisversioksi 2019.3 Python 3:ssa
  esiteltyjen merkintöjen tukemiseksi.

## Muutokset versiossa 20230508.0.0 ja sitä uudemmissa

- Versionumero, NVDA-version vähimmäisvaatimus ja latauslinkki muutettu
  lisäosakaupan käytäntöjen/vaatimusten mukaisiksi.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Muutokset versiossa 19.02

- Versionumerointi muutettu muotoon vv.kk (vuosi kahdella numerolla, piste
  ja kuukausi kahdella numerolla);

## Muutokset versiossa 6.0

- Lisäosan asetukset lisätty NVDA:n asetuspaneeliin versiossa 2018.2 ja
  uudemmissa;
- Siirretty päivän etsimiseen tarkoitettu vaihtoehto Työkalut-valikkoon;

## Muutokset versiossa 5.0

- Lisätty wxPython 4.0:n ja Python 3:n yhteensopivuus;
- Korjattu bugi, jota esiintyi, kun lisäosan hakemistopoluissa oli muita
  kuin ASCII-merkkejä.
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Muutokset versiossa 4.0

- Lisäosa tunnistaa nyt kaikki käyttäjän valittavissa olevat alueelliset
  päivämäärämuodot;
- Lisätty taaksepäin yhteensopivuus gui.guiHelper-moduulin sisältävää NVDA
  2016.4:ää vanhemmille versioille.

## Muutokset versiossa 3.1

- Palattu viikonpäivän vanhaan muotoon, koska se mahdollistaa useamman
  kielen tunnistamisen;
- Paranneltu päivämäärävalitsimen saavutettavuutta "Päivä"-, "Kuukausi"- ja
  "Vuosi"-kenttien sekä niiden arvojen tunnistamisessa;

## Muutokset versiossa 2.0

- Päivämääränkyselyvalintaikkunan asianmukaisen ulkoasun varmistamiseen
  käytetään gui.guiHelper-moduulia;
- Lisätty GPL-lisenssi;
- Viikonpäivät on käännetty, jotta lisäosa toimii oikein eri kielillä;
- Päivän muotoa muutettu koodausvirheiden välttämiseksi.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Muutokset versiossa 1.0

- Ensimmäinen versio.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
