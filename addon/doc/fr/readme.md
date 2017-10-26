# Day of the week #

*	 Auteurs : Abdel, Noelia.
*	 Télécharger [version stable][1]
*	 Télécharger [version de développement][2]

Ce module complémentaire vous permet de trouver un jour de la semaine
correspondant à une date choisie.

Il ajoute un sous-menu dans le menu Préférences NVDA nommé "Jour de la
semaine", contenant 2 éléments :


*	Le premier nommé "Trouver un jour", ouvre une boîte de dialogue composée de 3 contrôles :
	*	Une zone de liste pour choisir ou tapez votre date ;
	*	Un bouton "OK" pour afficher une boîte de messages contenant votre jour ;
	*	Un bouton "Annuler" pour fermer la boîte de dialogue.
*	Le deuxième nommé "Paramètres du module complémentaire dayOfTheWeek" ouvre les paramètres du module complémentaire pour spécifier si vous souhaitez annoncer les étiquettes pour les champs de date ou non, il se compose des éléments suivants :
	*	Activer l'accessibilité du sélecteur de date ;
	*	Niveau des annonces d'étiquettes, vous aurez alors 3 choix :
		*	Long (c'est le choix par défaut) ;
		*	Court (pour les annonces courts) ;
		*	Désactiver (désactiver les annonces d'étiquettes).
	*	Activer les annonces de la valeur actuelle du champ de la date uniquement lorsque vous vous déplacez verticalement ;
	*	Un bouton "OK" pour sauvegarder votre configuration ;
	*	Un bouton "Annuler" pour annuler et fermer la boîte de dialogue.


## Notes ##

*	 Vous pouvez fermer cette boîte de dialogue en appuyant sur Échap.
*	 Vous pouvez assigner un raccourci pour ouvrir la boîte de dialogue dans
   le menu "Gestes de Commandes" et, plus précisément, dans la catégorie
   "Jour de la semaine".

## Changements pour la version 4.0 ##

*	 Le module complémentaire est maintenant en mesure de reconnaître tous les
   formats de date régional que l'utilisateur peut choisir ;
*	 Ajout de la rétrocompatibilité du module avec les versions NVDA
   antérieures à la version 2016.4, qui incluait le module gui.guiHelper.

## Changements pour la version 3.1 ##

*	 Retour au format précédent pour le jour de la semaine car il permet de
   reconnaître un plus grand nombre de langues ;
*	 Amélioré l'accessibilité du sélecteur de date avec la reconnaissance des
   3 champs "Jour", "Mois" et "Année", et leurs valeurs respectives ;
*	 Ajout d'une technique pour l'intégration de la langue Géorgienne pour la
   reconnaissance des jours de la semaine ;
*	 Ajout d'une boîte de dialogue de configuration pour activer ou désactiver
   l'accessibilité du sélecteur de date ;
*	 Déplacé le sous-menu du module complémentaire de "Outils" à "Préférences"
   ;
*	 Changé la catégorie du module complémentaire à "Jour de la semaine".

## Changements pour la version 2.0 ##

*	 Utilisé le module gui.guiHelper pour assurer la bonne apparence de la
   boîte de dialogue demandant une date ;
*	 Ajout de la licence GPL pour le module complémentaire ;
*	 Les jours de la semaine ont été traduits, de sorte que le module
   complémentaire fonctionne correctement dans les différentes langues ;
*	 Changé le format de jour pour éviter les erreurs d'encodage.

## Changements pour la version 1.0 ##

*	 Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
