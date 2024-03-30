# Dia da semana #

* Autores: Abdel, Noelia.

Este extra permite que encontre um dia da semana correspondente a uma data
escolhida.

Adiciona um submenu no menu Preferências do NVDA chamado "Dia da semana",
que contém 2 itens:

* O primeiro, chamado "Pesquisar um dia" abre uma caixa de diálogo composta
  por 3 controlos:

    * Uma caixa de lista para escolher ou escrever a sua data;
    * Um botão "OK" para mostrar uma caixa de mensagem que contém o seu dia;
    * Um botão "Cancelar" para fechar a caixa de diálogo.

* O segundo, denominado "Configuração do extra dayOfTheWeek" abre os
  parâmetros do extra para indicar se deseja escrever rótulos para campos de
  data ou não, é composto pelos seguintes elementos:

    * Activar acessibilidade do selector de datas;
    * Nível dos anúncios dos rótulos, onde terá 3 opções:

        * Longo (é a escolha padrão);
        * Curto (para indicações curtas)
        * off (para desactivar os anúncios).

    * Activar o anúncio do valor do campo de data actual somente quando se
      mover verticalmente;
    * Um botão "OK" para guardar a sua configuração;
    * Um botão "Cancelar" para cancelar e fechar a caixa de diálogo.

## Notas: ##

* Pode fechar estas caixas de diálogo, pressionando escape.
* Pode atribuir uma tecla de atalho, para abrir estas caixas de diálogo, no
  menu "Definir comandos" e, mais precisamente, na categoria "Dia da
  semana".
* Se estiver a usar o NVDA 2018.2 ou superior, encontrará apenas um item no
  menu de ferramentas para procurar o seu dia, as configurações do add-on
  estarão no painel de configurações do NVDA.

## Compatibilidade ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Alterações para 19.0.2 ##

* Alterada a Numeração de versão, usando AA.MM (O ano em 2 dígitos, seguido
  por um ponto, seguido pelo mês em 2 dígitos);
* Acrescentada a compatibilidade com o novo formato de versão do extra, que
  irá surgir a partir desde o nvda 2019.1.

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
