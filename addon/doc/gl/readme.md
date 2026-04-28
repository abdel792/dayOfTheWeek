# Day of the week

- Autores: Abdel, Noelia.

Este complemento permíteche atopar un día da semana correspondente a unha
data escollida.

Engade un submenú no menú Ferramentas do NVDA chamado "Día da semana", que
contén 2 elementos:

- O primeiro, chamado "Procurar un día", abre un diálogo composto por tres
  controis:

  - Unha caixa de lista para escoller ou escribir a túa data;
  - Un botón "Aceptar" para amosar un cadro de mensaxe que conteña o teu
    día.
  - Un botón "Cancelar" para cerrar el diálogo.

- O segundo, chamado Opcións do complemento dayOfTheWeek, abre os parámetros
  do complemento para especificar se queres que se informe das etiquetas dos
  campos de data ou non, composto polos seguintes elementos:

  - Habilitar a acesibilidade do selector de data;

  - Nivel dos anunciados das &etiquetas, terás tres opcións:

    - Longo (é a opción por defecto);
    - curto (para anuncios curtos);
    - Desactivado (para deshabilitar os anuncios das etiquetas).

  - Habilitar só os anunciados do valor do campo de data actual, ao
    moverse verticalmente;

  - Un botón "Aceptar" para gardar a túa configuración;

  - Un botón "Cancelar" para cancelar e pechar o diálogo.

## Notas

- Podes pechar estes diálogos só premendo Escape;
- Podes asignar un atallo de teclado para abrir estes diálogos no menú
  "Xestos de Entrada" e, máis concretamente, na categoría "Día da semana";
- Se usas NVDA 2018.2 ou superior, só atoparás un elemento no menú
  ferramentas para procurar o día, as opcións do complemento estarán no
  panel opcións de NVDA.

## Compatibilidade

- This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0

- Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0

- Applied the flake8 and mypy rules to the code;
- Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond

- Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Cambios para 19.02

- Modificado o numerado de versións utilizando YY.MM (o ano en dous díxitos,
  seguido dun punto, seguido polo mes en dous díxitos);

## Cambios para 6.0

- Engadidas as opcións do complemento ao panel opcións do NVDA para NVDA
  2018.2 e superiores;
- Movido o elemento para procurar un día ao menú ferramentas;

## Cambios para 5.0

- Engadida compatibilidade do complemento con Wx Python 4.0 e Python 3;
- Aranxado un erro con rutas de complementos que conteñen caracteres non
  ASCII.
- Added the backward compatibility of the add-on with the NVDA versions that preceded 2018.2, which included the settings panel.

## Cambios para 4.0

- O complemento ahora é quen de recoñecer todos os formatos de rexión que o
  usuario poda escoller;
- Engadida a compatibilidade cara atrás do complemento coas versións do NVDA
  que precederan á 2016.4, que inclúe o módulo gui.guiHelper.

## Cambios para 3.1

- Volta ao formato anterior para o día da semana porque permite recoñecer un
  meirande número de linguas;
- Mellora da acesibilidade do selector de datas co recoñecemento dos 3
  campos "Día", "Mes" e "Ano", e os seus respectivos valores;

## Cambios para 2.0

- Usa o módulo gui.guiHelper para asegurar a correcta apariencia do diálogo
  pedindo unha data;
- Engadida a licencia GPL para o complemento;
- Traducíronse os días da semana, para que o complemento funcione
  correctamente nas distintas linguas;
- Cambiouse o formato de día para evitar erros de codificación.
- Moved the add-on submenu from "Tools" to "Preferences";
- Changed the add-on category to "Day of the week".

## Cambios para 1.0

- Versión inicial.
- Added the GPL license to the addon;
- Days of the week have been translated, so that the add-on works properly in the different languages;
- Changed the day format to avoid encoding errors.

## Changes for 1.0

- Initial version.
