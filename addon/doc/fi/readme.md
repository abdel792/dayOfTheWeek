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

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## Muutokset versiossa 1.0 ##

*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
