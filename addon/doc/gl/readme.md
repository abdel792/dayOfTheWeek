# Día da semana #

* Desenvolvedores: Abdel, Noelia.

Este complemento permítelle atopar o día da semana correspondente a unha data elixida.

Engade un submenú no menú Ferramentas de NVDA chamado "Día da semana", que contén 2 elementos:

* O primeiro, chamado "Buscar un día", abre un diálogo composto por 3 controis:

    * Unha caixa de lista para escoller ou escribir a súa data;
    * Un botón "Aceptar" para mostrar unha caixa de mensaxe que contén o seu día;
    * Un botón "Cancelar" para pechar o diálogo.

* O segundo, chamado "Configuración do complemento dayOfTheWeek", abre os parámetros do complemento para especificar se desexa anunciar as etiquetas dos campos de data ou non, e está composto polos seguintes elementos:

    * Activar a accesibilidade do selector de data;
    * Nivel de anuncio das etiquetas, onde terá 3 opcións:

        * Longo (é a opción por defecto);
        * Curto (para anuncios curtos);
        * Desactivado (para desactivar os anuncios de etiquetas).

    * Activar o anuncio só do valor do campo de data actual, ao moverse verticalmente;
    * Un botón "Aceptar" para gardar a súa configuración;
    * Un botón "Cancelar" para cancelar e pechar o diálogo.

## Notas ##

* Pode pechar estes diálogos simplemente premendo Escape;
* Pode asignar un atallo para abrir estes diálogos no menú "Xestos de entrada" e, máis precisamente, na categoría "Día da semana";
* Se usa NVDA 2018.2 ou superior, atopará só un elemento no menú de ferramentas para buscar o seu día, a configuración do complemento estará no panel de configuración de NVDA.

## Compatibilidade ##

* Este complemento é compatible coas versións de NVDA que van desde a 2019.3 en diante.

## Cambios para 20240326.0.0

* Actualizada a compatibilidade para nvda-2024.1.;
* Eliminada a ligazón de descarga do readme, a ligazón de descarga para futuras actualizacións agora só estará dispoñible desde a tenda de complementos.

## Cambios para 20231229.0.0 ##

* Engadida unha implementación compatible con versións anteriores para soportar o modo de fala baixo demanda, que pronto estará dispoñible con nvda-2024.1.

## Cambios para 20231015.0.0 ##

* Corrixiuse un erro detectado ao navegar coa frecha arriba desde o selector de data nas últimas versións de NVDA.

## Cambios para 20230728.0.0 ##

* Aplicadas as regras de flake8 e mypy ao código;
* Cambiouse a versión mínima soportada de NVDA á 2019.3 para admitir as anotacións introducidas en Python 3.

## Cambios para 20230607.0.0 ##

* Engadíronse os seguintes fluxos de traballo:
 * auto-update-translations - para actualizar automaticamente as traducións desde o sistema de tradución de NVDA.
 * release-on-tag..yaml: para construír e publicar o complemento tan pronto como se envíe unha nova etiqueta;
 * manual-release.yaml: para construír e lanzar novas versións do complemento manualmente.
* Traducións actualizadas.

## Cambios para a versión 20230508.0.0 e posteriores ##

* • Cambiouse o número de versión, a versión mínima de NVDA e a ligazón de descarga segundo as convencións/requisitos da tenda.

## Cambios para 19.02 ##

* Cambiouse a numeración das versións usando AA.MM (O ano en 2 díxitos, seguido dun punto, seguido do mes en 2 díxitos);
* Engadida compatibilidade co novo formato de versións de complementos, aparecido desde nvda 2019.1.

## Cambios para 6.0 ##

* Engadiuse a configuración do complemento ao panel de configuración de NVDA para NVDA 2018.2 e superior;
* Moveuse o elemento para buscar un día ao menú ferramentas;
* Engadiuse a compatibilidade con versións anteriores do complemento coas versións de NVDA que precederon á 2018.2, que incluían o panel de configuración.

## Cambios para 5.0 ##

* Engadida a compatibilidade do complemento con wxPython 4.0 e Python3;
* Corrixiuse un erro coas rutas do complemento que conteñen caracteres non ASCII.

## Cambios para 4.0 ##

* O complemento agora é capaz de recoñecer todos os formatos de data rexionais que o usuario pode elixir;
* Engadiuse a compatibilidade con versións anteriores do complemento coas versións de NVDA que precederon á 2016.4, que incluían o módulo gui.guiHelper.

## Cambios para 3.1 ##

* Volveuse ao formato anterior para o día da semana porque permite recoñecer un maior número de idiomas;
* Mellorouse la accesibilidade do selector de data con recoñecemento dos 3 campos 'Día', 'Mes' e 'Ano', e os seus respectivos valores;
* Engadiuse unha técnica para a integración do idioma xeorxiano para o recoñecemento dos días da semana;
* Engadiuse un diálogo de configuración para activar ou desactivar a accesibilidade do selector de data;
* Moveuse o submenú do complemento desde "Ferramentas" a "Preferencias";
* Cambiouse a categoría do complemento a "Día da semana".

## Cambios para 2.0 ##

* Usouse o módulo gui.guiHelper para garantir a correcta aparencia do diálogo que solicita unha data;
* Engadiuse a licenza GPL ao complemento;
* Os días da semana foron traducidos, de xeito que o complemento funcione correctamente nos diferentes idiomas;
* Cambiouse o formato do día para evitar erros de codificación.

## Cambios para 1.0 ##

* Versión inicial.
