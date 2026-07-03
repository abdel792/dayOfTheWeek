# Viikonpäivä #

* Kehittäjät: Abdel, Noelia.

Tämän lisäosan avulla voit selvittää valittua päivämäärää vastaavan viikonpäivän.

Se lisää NVDA:n Työkalut-valikkoon alavalikon nimeltä "Viikonpäivä", joka sisältää 2 kohdetta:

* Ensimmäinen nimeltään "Etsi päivä", avaa valintaruudun, joka koostuu 3 säätimestä:

    * Luetteloruutu päivämäärän valitsemiseksi tai kirjoittamiseksi;
    * "OK"-painike, joka näyttää viestiruudun, joka sisältää päiväsi;
    * "Peruuta"-painike valintaruudun sulkemiseksi.

* Toinen nimeltään "Viikonpäivä-lisäosan asetukset" avaa lisäosan parametrit, joissa voit määrittää, haluatko ilmoittaa päivämääräkenttien selitteet vai et. Se koostuu seuraavista osista:

    * Ota käyttöön päivämäärävalitsimen saavutettavuus;
    * Selitteiden ilmoitustaso, jolloin sinulla on 3 vaihtoehtoa:

        * Pitkä (tämä on oletusvaihtoehto);
        * Lyhyt (lyhyitä ilmoituksia varten);
        * Pois päältä (poistaa selitteiden ilmoitukset käytöstä).

    * Ota käyttöön vain nykyisen päivämääräkentän arvon ilmoittaminen pystysuunnassa liikuttaessa;
    * "OK"-painike määritysten tallentamiseksi;
    * "Peruuta"-painike peruuttamiseksi ja valintaruudun sulkemiseksi.

## Huomautukset ##

* Voit sulkea nämä valintaruudut painamalla Esc-näppäintä;
* Voit määrittää pikanäppäimen näiden valintaruutujen avaamiseen "Syötteet"-valikosta ja tarkemmin sanottuna luokasta "Viikonpäivä";
* Jos käytät NVDA-versiota 2018.2 tai uudempaa, löydät työkalut-valikosta vain yhden kohdan päivän etsimistä varten, ja lisäosan asetukset ovat NVDA:n asetuspaneelissa.

## Yhteensopivuus ##

* Tämä lisäosa on yhteensopiva NVDA-versioiden 2019.3 ja sitä uudempien kanssa.

## Muutokset versioon 20240326.0.0

* Päivitetty yhteensopivuus nvda-2024.1-versiolle.;
* Poistettu latauslinkki luettelotiedostosta, tulevien päivitysten latauslinkki on jatkossa saatavilla vain lisäosakaupasta.

## Muutokset versioon 20231229.0.0 ##

* Lisätty taaksepäin yhteensopiva toteutus tukemaan puhetta tarvittaessa -tilaa, joka on pian saatavilla nvda-2024.1-version myötä.

## Muutokset versioon 20231015.0.0 ##

* Korjattu virhe, joka havaittiin navigoitaessa ylänuolella päivämääränvalitsimesta NVDA:n uusimmissa versioissa.

## Muutokset versioon 20230728.0.0 ##

* Sovellettu flake8- ja mypy-sääntöjä koodiin;
* Muutettu pienin tuettu NVDA-versio versioon 2019.3 Python 3:ssa esiteltyjen annotaatioiden tukemiseksi.

## Muutokset versioon 20230607.0.0 ##

* Lisätty seuraavat työvaiheet:
 * auto-update-translations - kääntämään käännökset automaattisesti NVDA:n käännösjärjestelmästä.
 * release-on-tag..yaml: lisäosan kääntämiseksi ja julkaisemiseksi heti, kun uusi tagi on lähetetty;
 * manual-release.yaml: lisäosan uusien versioiden kääntämiseksi ja julkaisemiseksi manuaalisesti.
* Päivitetyt käännökset.

## Muutokset versioon 20230508.0.0 ja uudempiin ##

* • Muutettu versionumero, NVDA:n vähimmäisversio ja latauslinkki kaupan käytäntöjen/vaatimusten mukaisesti.

## Muutokset versioon 19.02 ##

* Muutettu versionumerointi muotoon VV.KK (Vuosi 2 numerolla, jota seuraa piste, jota seuraa kuukausi 2 numerolla);
* Lisätty yhteensopivuus uuden lisäosien versiointimuodon kanssa, joka on ilmestynyt nvda 2019.1 -versiosta lähtien.

## Muutokset versioon 6.0 ##

* Lisätty lisäosan asetukset NVDA:n asetuspaneeliin NVDA 2018.2:lle ja uudemmille;
* Siirretty päivän etsimisen kohde työkalut-valikkoon;
* Lisätty lisäosan taaksepäin yhteensopivuus NVDA-versioiden kanssa, jotka edelsivät versiota 2018.2, johon asetuspaneeli sisältyi.

## Muutokset versioon 5.0 ##

* Lisätty lisäosan yhteensopivuus wxPython 4.0:n ja Python3:n kanssa;
* Korjattu virhe lisäosan poluissa, jotka sisältävät muita kuin ASCII-merkkejä.

## Muutokset versioon 4.0 ##

* Lisäosa pystyy nyt tunnistamaan kaikki alueelliset päivämäärämuodot, jotka käyttäjä voi valita;
* Lisätty lisäosan taaksepäin yhteensopivuus NVDA-versioiden kanssa, jotka edelsivät versiota 2016.4, johon gui.guiHelper-moduuli sisältyi.

## Muutokset versioon 3.1 ##

* Palattu edelliseen viikonpäivämuotoon, koska se mahdollistaa useampien kielten tunnistamisen;
* Parannettu päivämäärävalitsimen saavutettavuutta tunnistamalla 3 kenttää 'Päivä', 'Kuukausi' ja 'Vuosi' sekä niiden vastaavat arvot;
* Lisätty tekniikka Georgian kielen integroimiseksi viikonpäivien tunnistamiseen;
* Lisätty asetusten valintaruutu päivämäärävalitsimen saavutettavuuden käyttöönottamiseksi tai käytöstä poistamiseksi;
* Siirretty lisäosan alavalikko "Työkalut"-valikosta "Asetukset"-valikkoon;
* Muutettu lisäosan luokaksi "Viikonpäivä".

## Muutokset versioon 2.0 ##

* Käytetty gui.guiHelper-moduulia varmistamaan päivämäärää pyytävän valintaruudun oikea ulkoasu;
* Lisätty GPL-lisenssi lisäosaan;
* Viikonpäivät on käännetty, jotta lisäosa toimii oikein eri kielillä;
* Muutettu päivän muotoa koodausvirheiden välttämiseksi.

## Muutokset versioon 1.0 ##

* Alkuperäinen versio.
