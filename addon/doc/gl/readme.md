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

## Cambios para 5.0 ##

*	 Engadida compatibilidade do complemento con Wx Python 4.0 e Python 3;
*	 Aranxado un erro con rutas de complementos que conteñen caracteres non
   ASCII.

## Cambios para 4.0 ##

*	 O complemento ahora é quen de recoñecer todos os formatos de rexión que o
   usuario poda escoller;
*	 Engadida a compatibilidade cara atrás do complemento coas versións do
   NVDA que precederan á 2016.4, que inclúe o módulo gui.guiHelper.

## Cambios para 3.1 ##

*	 Volta ao formato anterior para o día da semana porque permite recoñecer
   un meirande número de linguas;
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
*	 Traducíronse os días da semana, para que o complemento funcione
   correctamente nas distintas linguas;
*	 Cambiouse o formato de día para evitar erros de codificación.

## Cambios para 1.0 ##

*	 Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
