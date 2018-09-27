# Day of the week #

*	 Autores: Abdel, Noelia.
*	 descargar [versión estable][1]
*	 descargar [versión de desarrollo][2]

Este complemento te permite encontrar un día de la semana correspondiente a
una fecha elegida.

Añade un submenú en el menú Preferencias de NVDA llamado "Día de la semana",
que contiene 2 elementos:


*	El primero llamado "Encontrar un día", abre un diálogo compuesto de 3 controles:
	*	Un cuadro de lista para elegir o teclear tu fecha;
	*	Un botón "Aceptar" para mostrar un cuadro de mensaje que contenga tu día;
	*	Un botón "Cancelar" para cerrar el diálogo.
*	El segundo llamado "Opciones del complemento dayOfTheWeek" abre los parámetros del complemento para especificar si deseas anunciar las etiquetas de los campos de fecha o no, se compone de los siguientes elementos:
	*	Habilitar la accesibilidad del selector de fecha;
	*	Nivel de los anuncios de las etiquetas, entonces tú tendrás 3 opciones:
		*	Largo (es la opción predeterminada);
		*	Corto (para los anuncios cortos);
		*	Desactivado (deshabilitar los anuncios de las etiquetas).
	*	Habilitar anuncios del valor del campo de fecha actual solamente, al moverse verticalmente;
	*	Un botón "Aceptar" para guardar tu configuración;
	*	Un botón "Cancelar" para anular y cerrar el diálogo.

## Notas ##

*	 Puedes cerrar estos diálogos tan sólo pulsando Escape.
*	 Puedes asignar un atajo de teclado para abrir estos diálogos en el menú
   "Gestos de Entrada" y, más concretamente, en la categoría "Día de la
   semana".
*	 Si utilizas NVDA 2018.2 o superior, sólo encontrarás un elemento en el
   menú herramientas para buscar el día, las opciones del complemento
   estarán en el panel opciones de NVDA.

## Cambios para 6.0 ##

*	 Añadidas las opciones del complemento al panel opciones de NVDA para NVDA
   2018.2 y superiores;
*	 Movido el elemento para buscar un día al menú herramientas;
*	 Añadida la compatibilidad hacia atrás del complemento con las versiones
   de NVDA que precedieron a la versión 2018.2, que incluye el panel de
   opciones.

## Cambios para 5.0 ##

*	 Añadido la compatibilidad del complemento con wxPython 4.0 y Python3;
*	 Arreglado un error con rutas de complementos que no contienen caracteres
   ASCII.

## Cambios para 4.0 ##

*	 El complemento es ahora capaz de reconocer todos los formatos de fecha
   regional que el usuario puede elegir;
*	 Añadido la compatibilidad hacia atrás del complemento con las versiones
   de NVDA que precedieron a la versión 2016.4, que incluía el módulo
   gui.guiHelper.

## Cambios para 3.1 ##

*	 Retorno al formato anterior para el día de la semana porque permite
   reconocer un mayor número de idiomas;
*	 Mejora de la accesibilidad del selector de fechas con el reconocimiento
   de los 3 campos "Día", "Mes" y "Año", y sus respectivos valores;
*	 Añadida una técnica para la integración del idioma Georgiano para el
   reconocimiento de los días de la semana;
*	 Añadido un diálogo de configuración para habilitar o deshabilitar la
   accesibilidad del selector de fecha;
*	 Movido el submenú del complemento de "Herramientas" a "Preferencias";
*	 Cambiada la categoría del complemento a "Día de la semana".

## Cambios para 2.0 ##

*	 Utiliza el módulo gui.guiHelper para asegurar la correcta apariencia del
   diálogo pidiendo una fecha;
*	 Añadida la licencia GPL para el complemento;
*	 Los días de la semana se han traducido, para que el complemento funcione
   correctamente en los distintos idiomas;
*	 Cambiado el formato del día para evitar errores de codificación.

## Cambios para 1.0 ##

*	 Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
