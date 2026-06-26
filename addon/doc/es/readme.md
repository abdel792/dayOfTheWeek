# Día de la semana

* Autores: Abdel, Noelia.

Este complemento permite averiguar el día de la semana correspondiente a una fecha determinada.

Añade un submenú al menú Herramientas de NVDA denominado «Día de la semana», que contiene 2 elementos:

* El primero, denominado «Buscar un día», abre un cuadro de diálogo compuesto por 3 controles:

    * Un cuadro combinado para elegir o escribir la fecha;
    * Un botón «Aceptar» para mostrar un cuadro de mensaje con el día correspondiente;
    * Un botón «Cancelar» para cerrar el cuadro de diálogo.

* El segundo, denominado «Configuración del complemento Día de la semana», abre los parámetros del complemento para especificar si deseas anunciar las etiquetas de los campos de fecha o no. Está compuesto por los siguientes elementos:

    * Activar la accesibilidad del selector de fecha;
    * Nivel de anuncio de las etiquetas, con las 3 opciones siguientes:

        * Largo (opción predeterminada);
        * Corto (para anuncios abreviados);
        * Desactivado (para desactivar el anuncio de las etiquetas).

    * Activar el anuncio únicamente del valor del campo de fecha actual al desplazarse verticalmente;
    * Un botón «Aceptar» para guardar la configuración;
    * Un botón «Cancelar» para cancelar y cerrar el cuadro de diálogo.

## Notas

* Puedes cerrar estos cuadros de diálogo simplemente pulsando Escape;
* Puedes asignar un atajo para abrir estos cuadros de diálogo en el menú «Gestos de entrada» y, más concretamente, en la categoría «Día de la semana»;
* Si utilizas NVDA 2018.2 o una versión posterior, solo encontrarás un elemento en el menú Herramientas para buscar un día; la configuración del complemento estará disponible en el panel de configuración de NVDA.

## Compatibilidad

* Este complemento es compatible con las versiones de NVDA a partir de la 2019.3.

## Cambios de la versión 20240326.0.0

* Compatibilidad actualizada para NVDA 2024.1.;
* Se eliminó el enlace de descarga del README; el enlace de descarga de las futuras actualizaciones solo estará disponible en la tienda de complementos.

## Cambios de la versión 20231229.0.0

* Se añadió una implementación retrocompatible para admitir el modo Hablar bajo demanda, que estará disponible próximamente con NVDA 2024.1.

## Cambios de la versión 20231015.0.0

* Se corrigió un error detectado al navegar con la flecha arriba desde el selector de fecha en las últimas versiones de NVDA.

## Cambios de la versión 20230728.0.0

* Se aplicaron las reglas de flake8 y mypy al código;
* Se cambió la versión mínima compatible de NVDA a la 2019.3 para admitir las anotaciones introducidas en Python 3.

## Cambios de la versión 20230607.0.0

* Se añadieron los siguientes flujos de trabajo:
 * auto-update-translations: para actualizar automáticamente las traducciones desde el sistema de traducción de NVDA.
 * release-on-tag.yaml: para compilar y publicar el complemento en cuanto se publique una nueva etiqueta;
 * manual-release.yaml: para compilar y publicar manualmente nuevas versiones del complemento.
* Se actualizaron las traducciones.

## Cambios a partir de la versión 20230508.0.0

* • Se cambiaron el número de versión, la versión mínima de NVDA y el enlace de descarga de acuerdo con las convenciones y los requisitos de la tienda.

## Cambios de la versión 19.02

* Se cambió la numeración de las versiones al formato AA.MM (el año con 2 cifras, seguido de un punto y del mes con 2 cifras);
* Se añadió compatibilidad con el nuevo formato de versiones de los complementos, disponible desde NVDA 2019.1.

## Cambios de la versión 6.0

* Se añadieron los ajustes del complemento al panel de configuración de NVDA para NVDA 2018.2 y versiones posteriores;
* Se trasladó el elemento para buscar un día al menú Herramientas;
* Se añadió retrocompatibilidad del complemento con las versiones de NVDA anteriores a la 2018.2, que aún no incluían el panel de configuración.

## Cambios de la versión 5.0

* Se añadió compatibilidad del complemento con wxPython 4.0 y Python 3;
* Se corrigió un error relacionado con las rutas del complemento que contenían caracteres no ASCII.

## Cambios de la versión 4.0

* El complemento ahora es capaz de reconocer todos los formatos regionales de fecha que el usuario puede seleccionar;
* Se añadió retrocompatibilidad del complemento con las versiones de NVDA anteriores a la 2016.4, que incluían el módulo gui.guiHelper.

## Cambios de la versión 3.1

* Se volvió al formato anterior para el día de la semana, ya que permite reconocer un mayor número de idiomas;
* Se mejoró la accesibilidad del selector de fecha mediante el reconocimiento de los 3 campos «Día», «Mes» y «Año», así como de sus respectivos valores;
* Se añadió una técnica para integrar el idioma georgiano en el reconocimiento de los días de la semana;
* Se añadió un cuadro de diálogo de configuración para activar o desactivar la accesibilidad del selector de fecha;
* Se trasladó el submenú del complemento de «Herramientas» a «Preferencias»;
* Se cambió la categoría del complemento a «Día de la semana».

## Cambios de la versión 2.0

* Se utilizó el módulo gui.guiHelper para garantizar la correcta presentación del cuadro de diálogo que solicita una fecha;
* Se añadió la licencia GPL al complemento;
* Se tradujeron los días de la semana para que el complemento funcione correctamente en los distintos idiomas;
* Se modificó el formato del día para evitar errores de codificación.

## Cambios de la versión 1.0

* Versión inicial.
