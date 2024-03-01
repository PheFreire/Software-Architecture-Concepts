Arquitetura de software são padrões de desenvolvimento criado em torno de principios e boas praticas de design de codigo.

O intuito de toda arquitetura de software é garantir a estabilidade, crescimento e escalabilidade de um sistema, sendo:

- Estabilidade: Poder de alterar fluxos já desenvolvidos sem que outros fluxos ligados a este parem de funcionar ou precisem ser re-escritos

- Crecimento: Poder adicionar novas funcionalidades não antes previstas ou planejadas no inicio do sistema sem ter que re-arquitetar o mesmo

- Escalabilidade: Executar o sistema com a mesma performance e segrança para qualquer quantidade de usuarios

Para que um padrão de desenvolvimento seja considerado uma arquitetura de software garantindo a estabilidade, crescimento e escalabilidade em um sistema, este deve ultilizar alguns principios de design de codigo, sendo os mais basicos:

1 - Principio de responsabilidade unica 
	-- ./descentralizacao.py

2 - modularização
	-- ./modularizacao/README.md

3 - assinatura 
	-- ./assinatura/README.md

4 - segregação de interface e inverção de dependencia e substituição de liskov
	-- ./interface/README.md


Conceitos SOLID:
(S)ingle reponsability principle:	
	Um fluxo deve ser dividido em sub-processos que implementão uma unica funcionalidade da regra de negocio deste fluxo

(O)pen and close principle: 
	uma função deve estar fechada para modificações e aberta para integrações

(L)iskov Substitution: 
	Toda classe filha deve seguir as assinaturas da classe mãe podendo assim substituir sua classe mãe sem gerar gargalos

(I)nterface segregation: 
	Um fluxo não deve possuir como dependência as implementações de suas funcionalidades, ele deve depender unicamente das assinaturas de suas funcionalidades e estas devem ser garantidas por meio de interfaces.

(D)ependency Inversion: 
	O desing de um fluxo não deve possuir funcionalidades estaticas, mas sim, receber como parametro as implementações de suas funcionalidades através de instancias de interfaces. Dessa forma o codigo se torna dinámico em suas implementações e de facil modificações futuras

