# Dia da semana #

* Programadores: Abdel, Noelia.

Este suplemento permite-lhe encontrar o dia da semana correspondente a uma data escolhida.

Adiciona um subejdor no menu Ferramentas do NVDA chamado "Dia da semana", contendo 2 itens:

* O primeiro, chamado "Procurar um dia", abre um diálogo composto por 3 controlos:

    * Uma caixa de lista para escolher ou ditar a sua data;
    * Um botão "OK" para exibir uma caixa de mensagem contendo o seu dia;
    * Um botão "Cancelar" para fechar o diálogo.

* O segundo, chamado "Parâmetros do suplemento dayOfTheWeek", abre os parâmetros do suplemento para especificar se deseja anunciar as etiquetas dos campos de data ou não, sendo composto pelos seguintes elementos:

    * Ativar a acessibilidade do seletor de data;
    * Nível de anúncio das etiquetas, onde terá 3 opções:

        * Longo (é a opção por defeito);
        * Curto (para anúncios curtos);
        * Desativado (para desativar os anúncios de etiquetas).

    * Ativar o anúncio apenas do valor do campo de data atual, ao mover-se verticalmente;
    * Um botão "OK" para guardar a sua configuração;
    * Um botão "Cancelar" para cancelar e fechar o diálogo.

## Notas ##

* Pode fechar estes diálogos simplesmente premindo Escape;
* Pode atribuir um atalho para abrir estes diálogos no menu "Gestos de entrada" e, mais precisamente, na categoria "Dia da semana";
* Se usa o NVDA 2018.2 ou superior, encontrará apenas um item no menu de ferramentas para procurar o seu dia, e os parâmetros do suplemento estarão no painel de definições do NVDA.

## Compatibilidade ##

* Este suplemento é compatível com as versões do NVDA desde a 2019.3 em diante.

## Alterações para 20240326.0.0

* Atualizada a compatibilidade para nvda-2024.1.;
* Eliminada a hiperligação de transferência do readme, a hiperligação de transferência para futuras atualizações estará agora disponível apenas a partir da loja de suplementos.

## Alterações para 20231229.0.0 ##

* Adicionada uma implementação compatível com versões anteriores para suportar o modo de fala sob pedido, que estará brevemente disponível com o nvda-2024.1.

## Alterações para 20231015.0.0 ##

* Corrigido um erro detetado ao navegar com a seta para cima a partir do seletor de data nas últimas versões do NVDA.

## Alterações para 20230728.0.0 ##

* Aplicadas as regras do flake8 e mypy ao código;
* Alterada a versão mínima suportada do NVDA para a 2019.3 para suportar as anotações introduzidas no Python 3.

## Alterações para 20230607.0.0 ##

* Adicionados os seguintes fluxos de trabalho:
 * auto-update-translations - para atualizar automaticamente as traduções a partir do sistema de tradução do NVDA.
 * release-on-tag..yaml: para construir e publicar o suplemento assim que uma nova etiqueta for enviada;
 * manual-release.yaml: para construir e lançar novas versões do suplemento manualmente.
* Traduções atualizadas.

## Alterações para a versão 20230508.0.0 e posteriores ##

* • Alterado o número de versão, a versão mínima do NVDA e a hiperligação de transferência de acordo com as convenções/requisitos da loja.

## Alterações para 19.02 ##

* Alterada a numeração das versões utilizando AA.MM (O ano em 2 dígitos, seguido de um ponto, seguido do mês em 2 dígitos);
* Adicionada compatibilidade com o novo formato de versões de suplementos, surgido desde o nvda 2019.1.

## Alterações para 6.0 ##

* Adicionados os parâmetros do suplemento ao painel de definições do NVDA para o NVDA 2018.2 e superior;
* Movido o item para procurar um dia para o menu ferramentas;
* Adicionada a compatibilidade com versões anteriores do suplemento com as versões do NVDA que precederam a 2018.2, que incluíam o painel de definições.

## Alterações para 5.0 ##

* Adicionada la compatibilidade do suplemento com o wxPython 4.0 e Python3;
* Corrigido um erro com os caminhos do suplemento que contêm carateres não ASCII.

## Alterações para 4.0 ##

* O suplemento é agora capaz de reconhecer todos os formatos de data regionais que o utilizador pode escolher;
* Adicionada a compatibilidade com versões anteriores do suplemento com as versões do NVDA que precederam a 2016.4, que incluíam o módulo gui.guiHelper.

## Alterações para 3.1 ##

* Regresso ao formato anterior para o dia da semana porque permite reconhecer um maior número de idiomas;
* Melhorada a acessibilidade do seletor de data com o reconhecimento dos 3 campos 'Dia', 'Mês' e 'Ano', e os seus respetivos valores;
* Adicionada uma técnica para a integração do idioma georgiano para o reconhecimento dos dias da semana;
* Adicionado um diálogo de configuração para ativar ou desativar a acessibilidade do seletor de data;
* Movido o subejdor do suplemento de "Ferramentas" para "Preferências";
* Alterada a categoria do suplemento para "Dia da semana".

## Alterações para 2.0 ##

* Utilizado o módulo gui.guiHelper para garantir a correta aparência do diálogo que solicita uma data;
* Adicionada a licença GPL ao suplemento;
* Os dias da semana foram traduzidos, de modo a que o suplemento funcione corretamente nos diferentes idiomas;
* Alterado o formato do dia para evitar erros de codificação.

## Alterações para 1.0 ##

* Versão inicial.
