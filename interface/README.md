Sabemos que o fluxo no main funciona desde que a assinatura de suas funcionalidades sejam garantidas, ou seja a implementação interna das funcionalidades pode ser absolutamente qualquer desde que mantenha a assinatura

Podemos nos aproveitar do fato que a implementação interna das funcionalidades de um fluxo não importam e criar fluxos que possuim funcionalidades com implementação interna dinamica ou seja funcionalidades podem trocar a implementação interna durante  o funcionamento do programa criando assim um programa sem dependencias

Exemplo:
	A funcionalidade "create_user" deve receber uma "string" e salvar dados no banco.
	Fundamentalmente para o fluxo não faz diferença se o "create_user" está internamente em sua implementação criando um usuario em um banco "postgreSQL" ou dentro de um "Json" desde que a assinatura do "create_user" se mantenha a mesma.
	Assim, podemos fazer mais de um tipo de função "create_user" cada uma criando um usuario de forma diferente na hora de executar o fluxo especificarmos qual dos "create_user" sera usado na execução do fluxo, isso de maneira dinamica


Para realizarmos o processo descrito no exemplo acima, precisamos ultilizar uma tecnica chamada "inversão de dependencia". Para a inversão de dependencia, nosso fluxo não deve ter internamente descrito qual "crete_user" que será usado, ao contratio, ele deve recebe-lo de maneira dinamica no formato de um parametro do fluxo.

Mas agora temos outro problema: "como que garantimos que o "create_user" que será inserido como parametro terá as mesmas assinaturas obrigatorias que a função "create_user" deve ter para os fluxos continuarem funcionando sem problemas?!"
- Simples, usamos a herança da programação orientado objeto!

A herança do orientado objeto garante que toda classe gerada apartir de outra, deverá seguir todos os seus comportamentos de assinatura, sendo estes: nome dos metodos, entradas dos metodos e saida do metodos.

Sendo assim teremos uma classe interface, que existirá com o intuito de descrever qual é a assinatura obrigatoria que outras classes devem seguir para implementar uma funcionalidade de maneira dinamica.

Esta classe interface não implementará nenhum codigo interno, e será usada como exigencia de tipagem que deve ser satisfeita para o fluxo funcionar. Ou seja qualquer classe filha que tiver o mesmo comportamento de assinatura que uma classe interface (sua classe mãe) poderá substitui-la como parametro em seu lugar dentro do fluxo e o nome disso é substituição de liskov.

