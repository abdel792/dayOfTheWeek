# Day of the week #

* Autores: Abdel, Noelia.

Este complemento te permite encontrar un día de la semana correspondiente a
una fecha elegida.

Añade un submenú en el menú Herramientas de NVDA llamado "Día de la semana",
que contiene 2 elementos:

* El primero, llamado "Buscar un día", abre un diálogo con 3 controles:

    * Un cuadro de lista para elegir o teclear tu fecha;
    * Un botón "Aceptar" para mostrar un cuadro de mensaje que contenga tu
      día;
    * Un botón "Cancelar" para cerrar el diálogo.

* El segundo, llamado "Ajustes del complemento DayOfTheWeek" abre los
  parámetros del complemento para especificar si deben anunciarse etiquetas
  para los campos de fecha o no. Lo componen los siguientes elementos:

    * Habilita la accesibilidad del selector de fecha;
    * Nivel de anuncio de las etiquetas, que ofrece las siguientes opciones:

        * Largo (opción por defecto);
        * Corto (para anuncios cortos);
        * Desactivado (para desactivar el anuncio de etiquetas).

    * Activar anuncio solamente del campo de fecha actual, al moverse
      verticalmente;
    * Un botón "Aceptar" para guardar la configuración;
    * Un botón "Cancelar" para cancelar y cerrar el diálogo.

## Notas ##

* Puedes cerrar estos diálogos tan sólo pulsando Escape;
* Puedes asignar un atajo de teclado para abrir estos diálogos en el menú
  "Gestos de Entrada" y, más concretamente, en la categoría "Día de la
  semana".;
* Si utilizas NVDA 2018.2 o superior, sólo encontrarás un elemento en el
  menú herramientas para buscar el día, las opciones del complemento estarán
  en el panel opciones de NVDA.

## Compatibilidad ##

* Este complemento es compatible con las versiones de NVDA desde la 2019.3
  en adelante.

## Cambios para 20240326.0.0

* Se actualiza la compatibilidad para NVDA 2024.1.;
* Se elimina el enlace de descarga de la documentación, el enlace de
  descarga de futuras actualizaciones ahora sólo estará disponible desde la
  tienda de complementos.

## Cambios para 20231229.0.0 ##

* Se ha añadido una implementación retrocompatible para soportar el modo de
  voz a petición, que pronto estará disponible con NVDA 2024.1.

## Cambios para 20231015.0.0 ##

* Se corrige un fallo detectado al navegar con flecha arriba en el selector
  de fecha en las versiones más recientes de NVDA.

## Cambios para 20230728.0.0 ##

* Aplicadas las reglas de Flake8 y Mipy al código;
* Cambiada la versión mínima soportada de NVDA a la 2019.3 para soportar las
  anotaciones de tipos introducidas en Python 3.

## Cambios para 20230508.0.0 y posteriores ##

* Cambiado el número de versión, la versión mínima de NVDA y el enlace de
  descarga según las convenciones y los requisitos de la tienda.

## Cambios para 19.02 ##

* Se ha cambiado el número de versión usando el esquema AA.MM (dos dígitos
  para el año, seguidos de un punto y dos dígitos para el mes);
* Se ha añadido compatibilidad con el nuevo formato de versión de
  complementos, disponible desde NVDA 2019.1.

## Cambios para 6.0 ##

* añadidas las opciones del complemento al panel opciones de NVDA para NVDA
  2018.2 y superiores;
* Movido el elemento para buscar un día al menú herramientas;
* Añadida la compatibilidad hacia atrás del complemento con las versiones de
  NVDA que precedieron a la versión 2018.2, que incluye el panel de
  opciones.

## Cambios para 5.0 ##

* Añadido la compatibilidad del complemento con wxPython 4.0 y Python3;
* Arreglado un error con rutas de complementos que no contienen caracteres
  ASCII.

## Cambios para 4.0 ##

* El complemento es ahora capaz de reconocer todos los formatos de fecha
  regional que el usuario puede elegir;
* Añadido la compatibilidad hacia atrás del complemento con las versiones de
  NVDA que precedieron a la versión 2016.4, que incluía el módulo
  gui.guiHelper.

## Cambios para 3.1 ##

* Retorno al formato anterior para el día de la semana porque permite
  reconocer un mayor número de idiomas;
* Mejora de la accesibilidad del selector de fechas con el reconocimiento de
  los 3 campos "Día", "Mes" y "Año", y sus respectivos valores;
* Añadida una técnica para la integración del idioma Georgiano para el
  reconocimiento de los días de la semana;
* Añadido un diálogo de configuración para habilitar o deshabilitar la
  accesibilidad del selector de fecha;
* Movido el submenú del complemento de "Herramientas" a "Preferencias";
* Cambiada la categoría del complemento a "Día de la semana".

## Cambios para 2.0 ##

* Utiliza el módulo gui.guiHelper para asegurar la correcta apariencia del
  diálogo pidiendo una fecha;
* Añadida la licencia GPL para el complemento;
* Los días de la semana se han traducido, para que el complemento funcione
  correctamente en los distintos idiomas;
* Cambiado el formato del día para evitar errores de codificación.

## Cambios para 1.0 ##

* Versión inicial.

[[!tag dev stable]]
