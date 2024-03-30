# Dia da semana (Day of the week) #

* Autores: Abdel, Noelia.

Esse complemento permite que encontre um dia da semana correspondente a uma
data escolhida.

Adiciona um submenu no menu Ferramentas do NVDA chamado "Dia da semana", que
contém 2 itens:

* O primeiro, chamado "Pesquisar um dia" abre um diálogo composto por 3
  controles:

    * Uma caixa de lista para escolher ou escrever a sua data;
    * Um botão "OK" para mostrar uma caixa de mensagem que contém o seu dia;
    * Um botão "Cancelar" para fechar o diálogo.

* O segundo, denominado "Configuração do complemento Dia da semana" abre os
  parâmetros do complemento para indicar se deseja escrever rótulos para
  campos de data ou não, é composto pelos seguintes elementos:

    * Habilitar acessibilidade do seletor de datas;
    * Nível dos anúncios dos rótulos, onde terá 3 opções:

        * Longo (é a escolha padrão);
        * Curto (para anúncios curtos);
        * Desligado (para desativar os anúncios de rótulos).

    * Habilitar o anúncio somente do valor do campo de data atual, ao se
      mover verticalmente;
    * Um botão "OK" para salvar a sua configuração;
    * Um botão "Cancelar" para cancelar e fechar o diálogo.

## Notas ##

* Pode fechar estas caixas de diálogo pressionando Esc;
* Pode atribuir uma tecla de atalho, para abrir estas caixas de diálogo, no
  menu "Definir comandos" e, mais precisamente, na categoria "Dia da
  semana";
* Se estiver usando o NVDA 2018.2 ou superior, encontrará apenas um item no
  menu de ferramentas para pesquisar o seu dia, as configurações do
  complemento estarão no painel de configurações do NVDA.

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

## Alterações para 19.02 ##

* Alterada a Numeração de versão, usando AA.MM (O ano em 2 dígitos, seguido
  por um ponto, seguido pelo mês em 2 dígitos);
* Adicionado a compatibilidade com o novo formato de versão do complemento,
  aparecido desde o nvda 2019.1.

## Alterações para 6.0 ##

* adicionado as configurações do complemento ao painel de configurações do
  NVDA para o NVDA 2018.2 e superiores;
* Movido o item para pesquisar um dia para o menu de ferramentas;
* Adicionada a retrocompatibilidade do complemento com as versões do NVDA
  anteriores a 2018.2, que incluíam o painel de configurações.

## Alterações para 5.0 ##

* Adicionada a compatibilidade do add-on com wxPython 4.0 e Python3;
* Corrigida uma falha com caminhos do complemento, que contenham caracteres
  não-ASCII.

## Alterações para 4.0 ##

* O complemento agora é capaz de reconhecer todos os formatos regionais de
  data que o usuário possa escolher;
* Adicionada a retrocompatibilidade do complemento com as versões do NVDA
  que precederam a 2016.4, que incluíam o módulo gui.guiHelper.

## Alterações para 3.1 ##

* Voltar ao formato anterior para o dia da semana porque permite reconhecer
  um maior número de idiomas;
* Melhorada a acessibilidade do seletor de data com o reconhecimento dos 3
  campos 'Dia', 'Mês' e 'Ano', e seus respectivos valores;
* Adicionada uma técnica para a integração da língua Georgiana para o
  reconhecimento dos dias da semana;
* Adicionada uma caixa de diálogo de configuração para habilitar ou
  desabilitar a acessibilidade do seletor de data;
* O submenu do complemento foi movido de "Ferramentas" para "Preferências";
* Alterada a categoria do complemento para "Dia da semana".

## Alterações para 2.0 ##

* Passou a usar-se o módulo gui.guiHelper para garantir a aparência correta
  da caixa de diálogo solicitando uma data;
* Adicionada a licença GPL ao complemento;
* Os dias da semana foram traduzidos, de modo que, agora, o complemento
  funciona corretamente nos diferentes idiomas;
* Alterado o formato do dia para evitar erros de codificação.

## Alterações para 1.0 ##

* Versão inicial.

[[!tag dev stable]]
