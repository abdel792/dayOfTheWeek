# Viikonpäivä #

*	 Tekijät: Abdel, Noelia.
*	 Lataa [vakaa versio][1]
*	 Lataa [kehitysversio][2]

Tällä lisäosalla on mahdollista selvittää valittua päivämäärää vastaava
viikonpäivä.

NVDA-valikon Työkalut-alavalikon alle lisätään Viikonpäivä-vaihtoehto, josta
avautuu valintaikkuna, jossa on kolme säädintä:

*	 Listaruutu, josta voit valita tai johon voit kirjoittaa haluamasi
   päivämäärän.
*	 OK-painike, jota painettaessa tulee näkyviin valitsemasi päivän näyttävä
   ilmoitusruutu.
*	 Peruuta-painike, joka sulkee valintaikkunan.

## Huomautuksia ##
*	 Voit sulkea valintaikkunan myös painamalla Esc-näppäintä.
*	 Voit liittää valintaikkunan avaamista varten näppäinkomennon NVDA:n
   Asetukset-valikon Syötekomennot-kohdasta ja valitsemalla avautuvasta
   valintaikkunasta Työkalut-kategorian.

## Muutokset versiossa 2.0 ##

*	 Päivämääränkyselyvalintaikkunan asianmukaisen ulkoasun varmistamiseen
   käytetään gui.guiHelper-moduulia;
*	 Lisätty GPL-lisenssi;
*	 Viikonpäivät on käännetty, jotta lisäosa toimii oikein eri kielillä;
*	 Koodausvirheiden välttämiseksi päivämääriä varten käytetään %w-muotoa
   %a:n asemesta.

## Muutokset versiossa 1.0 ##

*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
