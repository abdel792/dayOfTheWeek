# Day of the week #

* Autores: Abdel, Noelia.
* descargar [versión estable][1]
* descargar [versión de desenvolvemento][2]

Este complemento permíteche atopar un día da semana correspondente a unha
data escollida.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * Un botón "Cancelar" para cerrar el diálogo.

* The second one named "dayOfTheWeek add-on settings" opens the parameters
  of the add-on to specify whether you want to report labels for date fields
  or not, it is composed of the following elements:

    * Enable accessibility of the date selector;
    * Level of the announces of labels, you will then have 3 choices:

        * Long (it's the default choice);
        * Short (for short announcements);
        * Off (to disable labels announcements).

    * Enable announcement of the current date field value only, when moving
      vertically;
    * An "OK" button to save your configuration;
    * A "Cancel" button to cancel and close the dialog.

## Notas ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* Se usas NVDA 2018.2 ou superior, só atoparás un elemento no menú
  ferramentas para procurar o día, as opcións do complemento estarán no
  panel opcións de NVDA.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Cambios para 6.0 ##

* Engadidas as opcións do complemento ao panel opcións do NVDA para NVDA
  2018.2 e superiores;
* Movido o elemento para procurar un día ao menú ferramentas;
* Engadida a compatibilidade cara atrás do complemento coas versións do NVDA
  que precederan á 2018.2, que inclúe o panel Opcións.

## Cambios para 5.0 ##

* Engadida compatibilidade do complemento con Wx Python 4.0 e Python 3;
* Aranxado un erro con rutas de complementos que conteñen caracteres non
  ASCII.

## Cambios para 4.0 ##

* O complemento ahora é quen de recoñecer todos os formatos de rexión que o
  usuario poda escoller;
* Engadida a compatibilidade cara atrás do complemento coas versións do NVDA
  que precederan á 2016.4, que inclúe o módulo gui.guiHelper.

## Cambios para 3.1 ##

* Volta ao formato anterior para o día da semana porque permite recoñecer un
  meirande número de linguas;
* Mellora da acesibilidade do selector de datas co recoñecemento dos 3
  campos "Día", "Mes" e "Ano", e os seus respectivos valores;
* Engadida unha técnica para a integración da lingua Georgiana para o
  recoñecemento dos días da semana;
* Engadido un diálogo de configuración para habilitar ou deshabilitar a
  acesibilidade do selector de data;
* Movido o submenú do complemento de "Ferramentas" a "Preferencias";
* Cambiada a categoría do complemento a "Día da semana".

## Cambios para 2.0 ##

* Usa o módulo gui.guiHelper para asegurar a correcta apariencia do diálogo
  pedindo unha data;
* Engadida a licencia GPL para o complemento;
* Traducíronse os días da semana, para que o complemento funcione
  correctamente nas distintas linguas;
* Cambiouse o formato de día para evitar erros de codificación.

## Cambios para 1.0 ##

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
