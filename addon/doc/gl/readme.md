# Day of the week #

*	 Autores: Abdel, Noelia.
*	 descargar [versión estable][1]
*	 descargar [versión de desenvolvemento][2]

Este complemento permíteche atopar un día da semana correspondente a unha
data escollida.

Engade un submenú no menú Preferencias do NVDA chamado "Día da semana", que
contén 2 elementos:


*	O primeiro chamado "Atopar un día", abre un diálogo composto de 3 controis:
	*	Unha Caixa de lista para escoller ou teclear a túa data;
	*	Un botón "Aceptar" para amosar una Caixa de mensaxe que conteña o teu día;
	*	Un botón "Cancelar" para pechar o diálogo.
*	O segundo chamado "Opcións do complemento dayOfTheWeek" abre os parámetros do complemento para especificar se desexas anunciar as etiquetas dos campos de data ou non, componse dos seguintes elementos:
	*	Habilitar a acesibilidade do selector de data;
	*	Nivel dos anuncios das etiquetas, entón ti terás 3 opcións:
		*	Longo (é a opción predeterminada);
		*	Curto (para os anuncios curtos);
		*	Desactivado (deshabilitar os anuncios das etiquetas).
	*	Habilitar anuncios do valor do campo de data actual só, ao moverse verticalmente;
	*	Un botón "Aceptar" para gardar a túa configuración;
	*	Un botón "Cancelar" para anular e pechar o diálogo.


## Notas ##

*	 Podes pechar este diálogo só premendo Escape.
*	 Podes asignar un atallo de teclado para abrir o diálogo no menú "Xestos
   de Entrada" e, máis concretamente, na categoría "Día da semana".

## Changes for 5.0 ##

*	 Engadida compatibilidade do complemento con Wx Python 4.0 e Python 3;
*	 Aranxado un erro con rutas de complementos que conteñen caracteres non
   ASCII.

## Changes for 4.0 ##

*	 The add-on is now able to recognize all the regional date formats that
   the user can choose;
*	 Added the backward compatibility of the add-on with the NVDA versions
   that preceded 2016.4, which included the gui.guiHelper module.

## Cambios para 3.1 ##

*	 Back to the previous format for the day of the week because it allows to
   recognize a greater number of languages;
*	 Mellora da acesibilidade do selector de datas co recoñecemento dos 3
   campos "Día", "Mes" e "Ano", e os seus respectivos valores;
*	 Engadida unha técnica para a integración da lingua Georgiana para o
   recoñecemento dos días da semana;
*	 Engadido un diálogo de configuración para habilitar ou deshabilitar a
   acesibilidade do selector de data;
*	 Movido o submenú do complemento de "Ferramentas" a "Preferencias";
*	 Cambiada a categoría do complemento a "Día da semana".

## Cambios para 2.0 ##

*	 Usa o módulo gui.guiHelper para asegurar a correcta apariencia do diálogo
   pedindo unha data;
*	 Engadida a licencia GPL para o complemento;
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Changed the day format to avoid encoding errors.

## Cambios para 1.0 ##

*	 Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
