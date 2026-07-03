# Dia da semana #

* Desenvolvedores: Abdel, Noelia.

Este complemento permite que você encontre o dia da semana correspondente a uma data escolhida.

Ele adiciona um submanu no menu Ferramentas do NVDA chamado "Dia da semana", contendo 2 itens:

* O primeiro, chamado "Buscar um dia", abre uma caixa de diálogo composta por 3 controles:

    * Uma caixa de listagem para escolher ou digitar a sua data;
    * Um botão "OK" para exibir uma caixa de mensagem contendo o seu dia;
    * Um botão "Cancelar" para fechar a caixa de diálogo.

* O segundo, chamado "Configurações do complemento dayOfTheWeek", abre os parâmetros do complemento para especificar se você deseja anunciar as etiquetas dos campos de data ou não, sendo composto pelos seguintes elementos:

    * Ativar a acessibilidade do seletor de data;
    * Nível de anúncio das etiquetas, onde você terá 3 opções:

        * Longo (é a opção padrão);
        * Curto (para anúncios curtos);
        * Desativado (para desativar os anúncios de etiquetas).

    * Ativar o anúncio apenas do valor do campo de data atual ao se mover verticalmente;
    * Um botão "OK" para salvar a sua configuração;
    * Um botão "Cancelar" para cancelar e fechar a caixa de diálogo.

## Notas ##

* Você pode fechar essas caixas de diálogo simplesmente pressionando Escape;
* Você pode atribuir um atalho para abrir essas caixas de diálogo no menu "Gestos de entrada" e, mais precisamente, na categoria "Dia da semana";
* Se você usa o NVDA 2018.2 ou superior, encontrará apenas um item no menu de ferramentas para buscar o seu dia, e as configurações do complemento estarão no painel de configurações do NVDA.

## Compatibilidade ##

* Este complemento é compatível com as versões do NVDA a partir da 2019.3 em diante.

## Alterações para 20240326.0.0

* Atualizada a compatibilidade para nvda-2024.1.;
* Removido o link de download do readme, o link de download para futuras atualizações agora estará disponível apenas a partir da loja de complementos.

## Alterações para 20231229.0.0 ##

* Adicionada uma implementação compatível com versões anteriores para suportar o modo de fala sob demanda, que estará brevemente disponível com o nvda-2024.1.

## Alterações para 20231015.0.0 ##

* Corrigido um erro detectado ao navegar com a seta para cima a partir do seletor de data nas últimas versões do NVDA.

## Alterações para 20230728.0.0 ##

* Aplicadas as regras do flake8 e mypy ao código;
* Alterada a versão mínima suportada do NVDA para a 2019.3 para suportar as anotações introduzidas no Python 3.

## Alterações para 20230607.0.0 ##

* Adicionados os seguintes fluxos de trabalho:
 * auto-update-translations - para atualizar automaticamente as traduções a partir do sistema de tradução do NVDA.
 * release-on-tag..yaml: para construir e publicar o complemento assim que uma nova etiqueta for enviada;
 * manual-release.yaml: para construir e lançar novas versões do complemento manualmente.
* Traduções atualizadas.

## Alterações para a versão 20230508.0.0 e posteriores ##

* • Alterado o número de versão, a versão mínima do NVDA e o link de download de acordo com as convenções/requisitos da loja.

## Alterações para 19.02 ##

* Alterada a numeração das versões utilizando AA.MM (O ano em 2 dígitos, seguido de um ponto, seguido do mês em 2 dígitos);
* Adicionada compatibilidade com o novo formato de versões de complementos, surgido desde o nvda 2019.1.

## Alterações para 6.0 ##

* Adicionadas as configurações do complemento ao painel de configurações do NVDA para o NVDA 2018.2 e superior;
* Movido o item para buscar um dia para o menu ferramentas;
* Adicionada a compatibilidade com versões anteriores do complemento com as versões do NVDA que precederam a 2018.2, que incluíam o painel de configurações.

## Alterações para 5.0 ##

* Adicionada a compatibilidade do complemento com o wxPython 4.0 e Python3;
* Corrigido um erro com os caminhos do complemento que contêm caracteres não ASCII.

## Alterações para 4.0 ##

* O complemento agora é capaz de reconhecer todos os formatos de data regionais que o usuário pode escolher;
* Adicionada a compatibilidade com versões anteriores do complemento com as versões do NVDA que precederam a 2016.4, que incluíam o módulo gui.guiHelper.

## Alterações para 3.1 ##

* Retorno ao formato anterior para o dia da semana porque permite reconhecer um maior número de idiomas;
* Melhorada a acessibilidade do seletor de data com o reconhecimento dos 3 campos 'Dia', 'Mês' e 'Ano', e seus respectivos valores;
* Adicionada uma técnica para a integração do idioma georgiano para o reconhecimento dos dias da semana;
* Adicionado um diálogo de configuração para ativar ou desativar a acessibilidade do seletor de data;
* Movido o submanu do complemento de "Ferramentas" para "Preferências";
* Alterada a categoria do complemento para "Dia da semana".

## Alterações para 2.0 ##

* Utilizado o módulo gui.guiHelper para garantir a correta aparência da caixa de diálogo que solicita uma data;
* Adicionada a licença GPL ao complemento;
* Os dias da semana foram traduzidos, de modo que o complemento funcione corretamente nos diferentes idiomas;
* Alterado o formato do dia para evitar erros de codificação.

## Alterações para 1.0 ##

* Versão inicial.
