# Dia da semana #

* Autores: Abdel, Noelia.
* baixar [versão estável] [1]
* baixar [versão de desenvolvimento] [2]

Este extra permite que encontre um dia da semana correspondente a uma data
escolhida.

It adds a submenu in the NVDA Tools menu named "Day of the week", containing
2 items:

* The first one named "Search a day", opens a dialog composed of 3 controls:

    * A listbox to choose or type your date;
    * An "OK" button to display a messageBox containing your day;
    * A "Cancel" button to close the dialog.

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

## Notas: ##

* You can close these dialogs just by pressing Escape.
* You can assign a shortcut to open these dialogs in "Input gestures" menu
  and, more precisely, in the "Day of the week" category.;
* Se estiver a usar o NVDA 2018.2 ou superior, encontrará apenas um item no
  menu de ferramentas para procurar o seu dia, as configurações do add-on
  estarão no painel de configurações do NVDA.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.1.

## Changes for 19.02 ##

* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Alterações para 6.0 ##

* adicionaram-se as configurações de addon ao painel de configurações do
  NVDA para o NVDA 2018.2 e superior;
* Movido o item para pesquisar um dia para o menu de ferramentas;
* Adicionada a compatibilidade com versões anteriores do complemento com as
  versões do NVDA anteriores a 2018.2, que incluíam o painel de
  configurações.

## Alterações para 5.0 ##

* Adicionada a compatibilidade do add-on com wxPython 4.0 e Python3;
* Corrigido um bug com caminhos do extra, que contenham caracteres
  não-ASCII.

## Alterações para 4.0 ##

* O extra agora é capaz de reconhecer todos os formatos regionais de data
  que o utilizador possa escolher;
* Adicionada a compatibilidade com as versões NVDA que precederam a 2016.4,
  que incluíam o módulo gui.guiHelper.

## Mudanças para 3.1 ##

* Voltar ao formato anterior para o dia da semana porque permite reconhecer
  um maior número de idiomas;
* Melhorada a acessibilidade do selector de data com o reconhecimento dos 3
  campos "Dia", "Mês" e "Ano", e seus respectivos valores;
* Adicionada uma técnica para a integração da língua georgiana para o
  reconhecimento dos dias da semana;
* Adicionada uma caixa de diálogo de configuração para activar ou desactivar
  a acessibilidade do selector de data;
* O menu do extra foi movido de ferramentas para preferências.
* Alterada a categoria do extra para "Dia da semana".

## Mudanças para 2.0 ##

* passou a Usar-se o módulo gui.guiHelper para garantir a aparência correcta
  da caixa de diálogo solicitando uma data;
* Adicionada a licença GPL ao extra.
* Os dias da semana foram traduzidos, de modo que, agora, o extra funciona
  correctamente nos diferentes idiomas;
* Alterado o formato do dia para evitar erros de codificação.

## Alterações para 1.0 ##

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
