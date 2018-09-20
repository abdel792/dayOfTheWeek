# Viikonpäivä #

*	 Tekijät: Abdel, Noelia.
*	 Lataa [vakaa versio][1]
*	 Lataa [kehitysversio][2]

Tällä lisäosalla on mahdollista selvittää valittua päivämäärää vastaava
viikonpäivä.

NVDA:n Asetukset-valikkoon lisätään Viikonpäivä-alavalikko, jossa on kaksi
kohdetta:


*	Ensimmäinen, "Etsi päivä", avaa valintaikkunan, jossa on kolme säädintä:
	*	Listaruutu päivämäärän valitsemiseen tai kirjoittamiseen;
	*	"OK"-painike, jota painettaessa valitsemasi päivämäärä näytetään ilmoitusruudussa;
	*	"Peruuta"-painike, jolla valintaikkuna suljetaan.
*	Toinen, "Viikonpäivä-lisäosan asetukset", avaa lisäosan asetusvalintaikkunan, josta voit määrittää, ilmoitetaanko päivämääräkenttien selitteet, ja siinä on seuraavat osat:
	*	Ota käyttöön päivämäärävalitsimen saavutettavuus;
	*	Selitteiden ilmoitustaso, josta on valittavissa kolme vaihtoehtoa:
		*	Pitkä (tämä on valittu oletuksena);
		*	Lyhyt (lyhyet ilmoitukset);
		*	Ei käytössä (poistaa selitteiden ilmoittamisen käytöstä).
	*	Ilmoita nykyisen päivämääräkentän arvo vain siirryttäessä nuolilla ylös ja alas;
	*	"OK"-painike asetusten tallentamiseen;
	*	"Peruuta"-painike muutosten perumiseen ja valintaikkunan sulkemiseen.

## Huomautuksia ##

*	 Valintaikkunat voidaan sulkea painamalla Esc-näppäintä;
*	 Valintaikkunoiden avaamista varten on mahdollista määrittää
   näppäinkomento Syötekomennot-valintaikkunan Viikonpäivä-kategoriasta;
*	 Työkalut-valikossa on nyt vain yksi vaihtoehto päivän etsimiseen, mikäli
   käytössä on NVDA 2018.2 tai uudempi. Lisäosan asetukset löytyvät NVDA:n
   asetuspaneelista.

## Muutokset versiossa 6.0 ##

*	 Lisäosan asetukset lisätty NVDA:n asetuspaneeliin versiossa 2018.2 ja
   uudemmissa;
*	 Siirretty päivän etsimiseen tarkoitettu vaihtoehto Työkalut-valikkoon;
*	 Lisätty taaksepäin yhteensopivuus NVDA 2018.2:ta edeltäneille versioille.

## Muutokset versiossa 5.0 ##

*	 Lisätty wxPython 4.0:n ja Python 3:n yhteensopivuus;
*	 Korjattu bugi, jota esiintyi, kun lisäosan hakemistopoluissa oli muita
   kuin ASCII-merkkejä.

## Muutokset versiossa 4.0 ##

*	 Lisäosa tunnistaa nyt kaikki käyttäjän valittavissa olevat alueelliset
   päivämäärämuodot;
*	 Lisätty taaksepäin yhteensopivuus gui.guiHelper-moduulin sisältävää NVDA
   2016.4:ää vanhemmille versioille.

## Muutokset versiossa 3.1 ##

*	 Palattu viikonpäivän vanhaan muotoon, koska se mahdollistaa useamman
   kielen tunnistamisen;
*	 Paranneltu päivämäärävalitsimen saavutettavuutta "Päivä"-, "Kuukausi"- ja
   "Vuosi"-kenttien sekä niiden arvojen tunnistamisessa;
*	 Lisätty tekniikka georgian kielen integroimiseen viikonpäivien
   tunnistamista varten;
*	 Lisätty asetusvalintaikkuna päivämäärävalitsimen saavutettavuuden
   käyttöön ottamiseen tai käytöstä poistamiseen;
*	 Lisäosan alavalikko siirretty "Työkalut"-valikosta "Asetukset"-valikkoon;
*	 Lisäosan kategoriaksi muutettu "Viikonpäivä".

## Muutokset versiossa 2.0 ##

*	 Päivämääränkyselyvalintaikkunan asianmukaisen ulkoasun varmistamiseen
   käytetään gui.guiHelper-moduulia;
*	 Lisätty GPL-lisenssi;
*	 Viikonpäivät on käännetty, jotta lisäosa toimii oikein eri kielillä;
*	 Päivän muotoa muutettu koodausvirheiden välttämiseksi.

## Muutokset versiossa 1.0 ##

*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
