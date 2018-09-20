# Dia da semana #

*	 Autores: Abdel, Noelia.
*	 baixar [versão estável] [1]
*	 baixar [versão de desenvolvimento] [2]

Este extra permite que encontre um dia da semana correspondente a uma data
escolhida.

Adiciona um submenu no menu Preferências do NVDA chamado "Dia da semana",
contendo 2 itens:


* O primeiro chamado "Pesquisar um dia", abre uma caixa de diálogo composta por 3 controlos:
* Uma caixa de listagem para escolher ou digitar a sua data;
* Um botão "OK" para mostrar uma caixa de mensagem que contém o seu dia;
* Um botão "Cancelar" para fechar a caixa de diálogo.
* O segundo, nomeado "Configurações do extra dayOfTheWeek" abre os parâmetros do extra para especificar se deseja indicar etiquetas para campos de data ou não, é composto dos seguintes elementos:
* Permite a acessibilidade do seletor de data;
* Nível das novidades dos rótulos, terá 3 opções:
* Longo (é a escolha padrão);
* Curto (para avisos curtos);
* Desligado (para desativar anúncios de etiquetas).
* Active o anúncio do valor actual do campo da data apenas, quando se move verticalmente;
* Um botão "OK" para salvar a sua configuração;
* Um botão "Cancelar" para cancelar e fechar a caixa de diálogo.

## Notas: ##

*	 You can close these dialogs just by pressing Escape;
*	 Pode atribuir um atalho, para abrir essas caixas de diálogo, no menu
   "Definir comandos" e, mais precisamente, na categoria "Dia da semana".
*	 Se estiver a usar o NVDA 2018.2 ou superior, encontrará apenas um item no
   menu de ferramentas para procurar o seu dia, as configurações do add-on
   estarão no painel de configurações do NVDA.

## Alterações para 6.0 ##

*	 adicionaram-se as configurações de addon ao painel de configurações do
   NVDA para o NVDA 2018.2 e superior;
*	 Movido o item para pesquisar um dia para o menu de ferramentas;
*	 Adicionada a compatibilidade com versões anteriores do complemento com as
   versões do NVDA anteriores a 2018.2, que incluíam o painel de
   configurações.

## Alterações para 5.0 ##

*	 Adicionada a compatibilidade do add-on com wxPython 4.0 e Python3;
*	 Corrigido um bug com caminhos do extra, que contenham caracteres
   não-ASCII.

## Alterações para 4.0 ##

*	 O extra agora é capaz de reconhecer todos os formatos regionais de data
   que o utilizador possa escolher;
*	 Adicionada a compatibilidade com as versões NVDA que precederam a 2016.4,
   que incluíam o módulo gui.guiHelper.

## Mudanças para 3.1 ##

*	 Voltar ao formato anterior para o dia da semana porque permite reconhecer
   um maior número de idiomas;
*	 Melhorada a acessibilidade do selector de data com o reconhecimento dos 3
   campos "Dia", "Mês" e "Ano", e seus respectivos valores;
*	 Adicionada uma técnica para a integração da língua georgiana para o
   reconhecimento dos dias da semana;
*	 Adicionada uma caixa de diálogo de configuração para activar ou
   desactivar a acessibilidade do selector de data;
*	 O menu do extra foi movido de ferramentas para preferências.
*	 Alterada a categoria do extra para "Dia da semana".

## Mudanças para 2.0 ##

*	 passou a Usar-se o módulo gui.guiHelper para garantir a aparência
   correcta da caixa de diálogo solicitando uma data;
*	 Adicionada a licença GPL ao extra.
*	 Os dias da semana foram traduzidos, de modo que, agora, o extra funciona
   correctamente nos diferentes idiomas;
*	 Alterado o formato do dia para evitar erros de codificação.

## Alterações para 1.0 ##

*	 Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
