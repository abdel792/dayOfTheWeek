# Jour de la semaine

* Auteurs : Abdel, Noelia.

Cette extension vous permet de trouver le jour de la semaine correspondant à une date choisie.

Elle ajoute un sous-menu dans le menu Outils de NVDA nommé « Jour de la semaine », contenant 2 éléments :

* Le premier, nommé « Rechercher un jour », ouvre une boîte de dialogue composée de 3 contrôles :

    * Une zone de liste pour choisir ou saisir votre date ;
    * Un bouton « OK » pour afficher une boîte de message contenant le jour correspondant ;
    * Un bouton « Annuler » pour fermer la boîte de dialogue.

* Le second, nommé « Paramètres de l'extension Jour de la semaine », ouvre les paramètres de l'extension afin de préciser si vous souhaitez annoncer les étiquettes des champs de date ou non. Il est composé des éléments suivants :

    * Activer l'accessibilité du sélecteur de date ;
    * Niveau d'annonce des étiquettes, avec les 3 choix suivants :

        * Long (choix par défaut) ;
        * Court (pour des annonces abrégées) ;
        * Désactivé (pour désactiver l'annonce des étiquettes).

    * Activer l'annonce de la valeur du champ de date courant uniquement, lors des déplacements verticaux ;
    * Un bouton « OK » pour enregistrer votre configuration ;
    * Un bouton « Annuler » pour annuler et fermer la boîte de dialogue.

## Remarques

* Vous pouvez fermer ces boîtes de dialogue simplement en appuyant sur Échap ;
* Vous pouvez attribuer un raccourci pour ouvrir ces boîtes de dialogue dans le menu « Gestes de commandes » et, plus précisément, dans la catégorie « Jour de la semaine » ;
* Si vous utilisez NVDA 2018.2 ou une version ultérieure, vous ne trouverez qu'un seul élément dans le menu Outils pour rechercher un jour ; les paramètres de l'extension seront disponibles dans le panneau des paramètres de NVDA.

## Compatibilité

* Cette extension est compatible avec les versions de NVDA à partir de la version 2019.3.

## Changements de la version 20240326.0.0

* Compatibilité mise à jour pour NVDA 2024.1 ;
* Suppression du lien de téléchargement dans le README ; le lien de téléchargement des futures mises à jour sera désormais disponible uniquement depuis la boutique des extensions.

## Changements de la version 20231229.0.0

* Ajout d'une implémentation rétrocompatible pour prendre en charge le mode Parler à la demande, qui sera prochainement disponible avec NVDA 2024.1.

## Changements de la version 20231015.0.0

* Correction d'un bogue détecté lors de la navigation avec la flèche haut depuis le sélecteur de date dans les dernières versions de NVDA.

## Changements de la version 20230728.0.0

* Application des règles flake8 et mypy au code ;
* Modification de la version minimale prise en charge de NVDA vers la version 2019.3 afin de prendre en charge les annotations introduites dans Python 3.

## Changements de la version 20230607.0.0

* Ajout des workflows suivants :
 * auto-update-translations - pour mettre automatiquement à jour les traductions depuis le système de traduction de NVDA.
 * release-on-tag.yaml : pour construire et publier l'extension dès qu'une nouvelle étiquette est créée ;
 * manual-release.yaml : pour construire et publier manuellement de nouvelles versions de l'extension.
* Mise à jour des traductions.

## Changements à partir de la version 20230508.0.0

* • Modification du numéro de version, de la version minimale de NVDA et du lien de téléchargement conformément aux conventions et exigences de la boutique.

## Changements de la version 19.02

* Modification de la numérotation des versions au format AA.MM (l'année sur 2 chiffres, suivie d'un point, puis le mois sur 2 chiffres) ;
* Ajout de la compatibilité avec le nouveau format de version des extensions, apparu depuis NVDA 2019.1.

## Changements de la version 6.0

* Ajout des paramètres de l'extension au panneau des paramètres de NVDA pour NVDA 2018.2 et les versions ultérieures ;
* Déplacement de l'élément de recherche d'un jour vers le menu Outils ;
* Ajout de la rétrocompatibilité de l'extension avec les versions de NVDA antérieures à la version 2018.2, qui n'intégraient pas encore le panneau des paramètres.

## Changements de la version 5.0

* Ajout de la compatibilité de l'extension avec wxPython 4.0 et Python 3 ;
* Correction d'un bogue concernant les chemins d'accès de l'extension contenant des caractères non ASCII.

## Changements de la version 4.0

* L'extension est désormais capable de reconnaître tous les formats régionaux de date que l'utilisateur peut choisir ;
* Ajout de la rétrocompatibilité de l'extension avec les versions de NVDA antérieures à la version 2016.4, qui intégraient le module gui.guiHelper.

## Changements de la version 3.1

* Retour au format précédent pour le jour de la semaine, car il permet de reconnaître un plus grand nombre de langues ;
* Amélioration de l'accessibilité du sélecteur de date grâce à la reconnaissance des 3 champs « Jour », « Mois » et « Année », ainsi que de leurs valeurs respectives ;
* Ajout d'une technique d'intégration de la langue géorgienne pour la reconnaissance des jours de la semaine ;
* Ajout d'une boîte de dialogue de configuration permettant d'activer ou de désactiver l'accessibilité du sélecteur de date ;
* Déplacement du sous-menu de l'extension de « Outils » vers « Préférences » ;
* Modification de la catégorie de l'extension en « Jour de la semaine ».

## Changements de la version 2.0

* Utilisation du module gui.guiHelper afin de garantir la présentation correcte de la boîte de dialogue demandant une date ;
* Ajout de la licence GPL à l'extension ;
* Traduction des jours de la semaine afin que l'extension fonctionne correctement dans les différentes langues ;
* Modification du format du jour afin d'éviter les erreurs d'encodage.

## Changements de la version 1.0

* Version initiale.
