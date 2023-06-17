# Day of the week #

* Auteurs : Abdel, Noelia.
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension vous permet de trouver un jour de la semaine correspondant à
une date choisie.

Il ajoute un sous-menu dans le menu Outils NVDA nommé "Jour de la semaine",
contenant 2 éléments :

* Le premier nommé "Trouver un jour", ouvre une boîte de dialogue composée
  de 3 contrôles :

    * Une zone de liste pour choisir ou tapez votre date ;
    * Un bouton "OK" pour afficher une boîte de messages contenant votre
      jour ;
    * Un bouton "Annuler" pour fermer la boîte de dialogue.

* Le deuxième nommé "Paramètres de l'extension dayOfTheWeek" ouvre les
  paramètres de l'extension pour spécifier si vous souhaitez annoncer les
  étiquettes pour les champs de date ou non, il se compose des éléments
  suivants :

    * Activer l'accessibilité du sélecteur de date ;
    * Niveau des annonces d'étiquettes, vous aurez alors 3 choix :

        * Long (c'est le choix par défaut) ;
        * Court (pour les annonces courtes) ;
        * Désactiver (désactiver les annonces d'étiquettes).

    * Activer les annonces de la valeur actuelle du champ de la date
      uniquement lorsque vous vous déplacez verticalement ;
    * Un bouton "OK" pour sauvegarder votre configuration ;
    * Un bouton "Annuler" pour annuler et fermer la boîte de dialogue.

## Notes ##

* Vous pouvez fermer cette boîte de dialogue en appuyant sur Échap ;
* Vous pouvez assigner un raccourci pour ouvrir la boîte de dialogue dans le
  menu "Gestes de Commandes" et, plus précisément, dans la catégorie "Jour
  de la semaine" ;
* Si vous utilisez NVDA 2018.2 ou une version ultérieure, vous ne trouverez
  qu'un seul élément dans le menu Outil pour rechercher votre jour, les
  paramètres de l'extension se trouvent dans le panneau Paramètres NVDA.

## Compatibilité ##

* Cette extension est compatible avec les versions de NVDA allant de 2014.3
  et au-delà.

## Changements pour la version 20230508.0.0 et au-delà ##

*   Numéro de version modifiée, version minimale NVDA et lien de
  téléchargement en fonction des conventions / exigences de la store.

## Changements pour la version 19.02 ##

* Modification de la numérotation des versions en utilisant YY.MM (L'année
  en 2 chiffres, suivie d'un point, suivie du mois en 2 chiffres);
* Ajout de la compatibilité avec le nouveau format de gestion des versions
  des extensions, apparu depuis nvda 2019.1.

## Changements pour la version 6.0 ##

* ajout des paramètres de l'extension au panneau Paramètres NVDA pour NVDA
  2018.2 et les versions ultérieures;
* Déplacement de l'élément pour rechercher un jour dans le menu Outils;
* Ajout de la rétrocompatibilité de l'extension avec les versions NVDA
  antérieures à la version 2018.2, qui incluait le panneau Paramètres.

## Changements pour la version 5.0 ##

* Ajout de la compatibilité de l'extension avec wxPython 4.0 et Python3 ;
* Correction d'un bug avec les chemins d'extension contenant des caractères
  non-ASCII.

## Changements pour la version 4.0 ##

* L'extension est maintenant en mesure de reconnaître tous les formats de
  date régional que l'utilisateur peut choisir ;
* Ajout de la rétrocompatibilité de l'extension avec les versions NVDA
  antérieures à la version 2016.4, qui incluait le module gui.guiHelper.

## Changements pour la version 3.1 ##

* Retour au format précédent pour le jour de la semaine car il permet de
  reconnaître un plus grand nombre de langues ;
* Amélioré l'accessibilité du sélecteur de date avec la reconnaissance des 3
  champs "Jour", "Mois" et "Année", et leurs valeurs respectives ;
* Ajout d'une technique pour l'intégration de la langue Géorgienne pour la
  reconnaissance des jours de la semaine ;
* Ajout d'une boîte de dialogue de configuration pour activer ou désactiver
  l'accessibilité du sélecteur de date ;
* Déplacé le sous-menu de l'extension de "Outils" à "Préférences" ;
* Changé la catégorie de l'extension à "Jour de la semaine".

## Changements pour la version 2.0 ##

* Utilisé le module gui.guiHelper pour assurer la bonne apparence de la
  boîte de dialogue demandant une date ;
* Ajout de la licence GPL pour l'extension;
* Les jours de la semaine ont été traduits, de sorte que l'extension
  fonctionne correctement dans les différentes langues ;
* Changé le format de jour pour éviter les erreurs d'encodage.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
