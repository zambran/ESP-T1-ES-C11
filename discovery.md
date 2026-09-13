# Discovery Arquitetural com GenAI

## 1. Objetivo

Este documento registra o processo de utilização de Inteligência Artificial Generativa para apoiar a documentação arquitetural do aplicativo móvel de agendamento de consultas médicas.

O objetivo não foi delegar à IA a definição da arquitetura, mas utilizá-la como apoio para identificar lacunas, propor uma representação estrutural e comportamental e auxiliar na elaboração dos diagramas em Mermaid.

## 2. Contexto fornecido

O sistema é um aplicativo móvel para agendamento de consultas médicas. O cenário contempla pacientes, médicos, gerenciamento de agenda, agendamento de consultas, notificações e integração com um sistema externo de prontuário eletrônico.

Para esta atividade, o escopo foi reduzido à jornada de agendamento de uma consulta, incluindo consulta de disponibilidade, realização e confirmação do agendamento e integração posterior com o prontuário.

Como o cenário é acadêmico e possui informações limitadas, decisões não fornecidas foram tratadas como hipóteses e não como fatos.

## 3. Estratégia utilizada

A interação com a GenAI foi estruturada em etapas:

1. identificação de lacunas e perguntas;
2. revisão da descrição do sistema;
3. definição de hipóteses de trabalho;
4. geração do diagrama estrutural;
5. geração do diagrama comportamental;
6. revisão das propostas geradas;
7. registro das decisões e ajustes realizados.

Essa abordagem foi adotada para evitar que decisões inferidas pelo modelo fossem incorporadas à documentação sem validação.

## 4. Principais hipóteses adotadas

Durante o processo, foram adotadas as seguintes hipóteses para tornar o cenário suficientemente definido para a atividade:

* pacientes e médicos utilizam o mesmo aplicativo móvel;
* o backend é uma aplicação modular exposta por uma API única;
* existe um único banco de dados relacional;
* notificações são tratadas como responsabilidade do backend, sem especificar um provedor;
* o prontuário eletrônico é um sistema externo;
* a integração com o prontuário é encapsulada pelo backend;
* o agendamento é confirmado antes da atualização do prontuário;
* somente horários disponíveis podem ser agendados;
* um mesmo horário não pode ser reservado simultaneamente por dois pacientes.

Essas decisões são hipóteses de trabalho e não requisitos confirmados do sistema original.

## 5. Ajustes realizados sobre a geração da IA

A saída da GenAI foi utilizada como ponto de partida e revisada de acordo com o contexto disponível.

Os principais ajustes foram:

### API única

Foi adotada uma API única em vez de separar o backend em múltiplos serviços. A decisão reduz a complexidade e evita assumir uma arquitetura de microsserviços sem evidências no contexto.

### Backend modular

As responsabilidades de agenda, agendamento, persistência e notificações foram mantidas como responsabilidades internas do backend. A separação é conceitual e não representa necessariamente serviços independentes.

### Banco de dados

Foi adotado um único banco de dados relacional. A tecnologia específica não foi definida para evitar uma decisão arquitetural sem fundamento.

### Prontuário eletrônico

O prontuário foi mantido como sistema externo. A integração foi colocada sob responsabilidade do backend, evitando dependências diretas do aplicativo ou de outras partes do sistema com detalhes do sistema externo.

### Notificações

Não foi introduzido um provedor externo específico de notificações, pois essa informação não estava disponível. A responsabilidade foi mantida no backend.

### Sequência do agendamento

O fluxo foi definido de modo que o agendamento seja registrado e confirmado antes da atualização do prontuário. Isso reduz o acoplamento entre a operação principal e a integração externa.

### Cenário alternativo

Foi incluído no diagrama de sequência o caso de o horário escolhido já ter sido reservado. Essa situação representa uma regra mínima de negócio assumida para o exercício.

## 6. O que a GenAI inferiu corretamente

A IA conseguiu identificar corretamente elementos importantes do cenário, como:

* a existência de um aplicativo utilizado pelos usuários;
* a necessidade de um backend para intermediar as operações;
* a necessidade de persistência dos dados;
* a integração com um sistema externo de prontuário;
* a importância de separar a integração externa das demais responsabilidades;
* a jornada de agendamento como uma boa candidata a fluxo comportamental.

Também foi útil para identificar lacunas que não estavam explícitas no contexto original.

## 7. O que permaneceu como lacuna

Mesmo após a elaboração dos diagramas, não foram definidos:

* tecnologias utilizadas;
* autenticação e autorização;
* modelo detalhado de dados;
* contrato da integração com o prontuário;
* protocolo e formato dos dados trocados;
* mecanismo efetivo de notificações;
* tratamento de falhas da integração;
* regras detalhadas de disponibilidade e cancelamento;
* requisitos de segurança e privacidade;
* requisitos de desempenho e disponibilidade;
* infraestrutura e estratégia de implantação.

Esses pontos não foram preenchidos pela IA para evitar transformar suposições em decisões arquiteturais.

## 8. Artefatos resultantes

A partir do processo foram produzidos:

* `README.md` — documentação principal do sistema, diagramas e decisões;
* `diagrams/container.md` — código Mermaid da visão estrutural;
* `diagrams/sequence.md` — código Mermaid do fluxo de agendamento;
* `discovery.md` — registro do processo de discovery e das decisões tomadas sobre a saída da GenAI.

## 9. Conclusão

O uso de GenAI acelerou a identificação de lacunas e a construção inicial dos diagramas, mas a saída do modelo não foi tratada como definição arquitetural automática.

A revisão humana foi necessária principalmente para controlar o escopo, eliminar complexidade não justificada e diferenciar fatos conhecidos de hipóteses.

Para que a documentação pudesse servir como contexto suficiente para um agente de desenvolvimento implementar o sistema sem inventar decisões, seria necessário complementá-la com requisitos de negócio detalhados, modelo de dados, contratos de integração, requisitos não funcionais, decisões tecnológicas, regras de segurança e estratégias para tratamento de falhas e implantação.

## 10. Prompts utilizados

### 10.1 Prompt para discovery

```text
Você é um arquiteto de software sênior apoiando uma atividade acadêmica de documentação arquitetural com a abordagem diagrams as code.

Considere o seguinte sistema:

O sistema é um aplicativo móvel para agendamento de consultas médicas. O cenário contempla pacientes, médicos, gerenciamento de agenda, agendamento de consultas, notificações e integração com um sistema externo de prontuário eletrônico.

O contexto é puramente acadêmico e possui informações limitadas. Para esta atividade, o escopo deve ser reduzido à jornada de agendamento de uma consulta, contemplando consulta de horários disponíveis, realização e confirmação do agendamento e integração posterior com o prontuário.

Algumas hipóteses de trabalho foram adotadas:
- pacientes e médicos utilizam o mesmo aplicativo móvel;
- o backend é uma aplicação modular exposta por uma API única;
- existe um único banco de dados relacional;
- notificações são responsabilidade do backend, sem especificação de provedor;
- o prontuário eletrônico é um sistema externo;
- a integração com o prontuário é encapsulada pelo backend;
- o agendamento é confirmado antes da atualização do prontuário;
- somente horários disponíveis podem ser agendados;
- um mesmo horário não pode ser reservado simultaneamente por dois pacientes.

Antes de gerar qualquer diagrama:

1. Identifique as principais lacunas do contexto.
2. Diferencie fatos fornecidos de hipóteses e inferências.
3. Aponte decisões arquiteturais que não podem ser determinadas com segurança a partir do contexto.
4. Sugira uma estrutura mínima e coerente para uma visão C4 no nível Container.
5. Sugira uma jornada crítica adequada para um diagrama de sequência.

Não invente tecnologias, protocolos, endpoints ou requisitos não fornecidos. Quando uma decisão não puder ser determinada, trate-a como lacuna ou hipótese explícita.
```

### 10.2 Prompt para o diagrama estrutural

```text
Você é um arquiteto de software sênior. Gere um diagrama estrutural em Mermaid, utilizando uma visão inspirada no C4 no nível de Containers.

Contexto:

O sistema é um aplicativo móvel para agendamento de consultas médicas. Pacientes e médicos utilizam o mesmo aplicativo, com funcionalidades diferentes conforme o perfil.

O backend é uma aplicação modular exposta por uma API única. Suas responsabilidades incluem agenda, agendamento, persistência e notificações.

O sistema utiliza um único banco de dados relacional.

Existe um sistema externo de prontuário eletrônico. A integração com esse sistema deve ser encapsulada pelo backend, evitando que o aplicativo móvel ou outras responsabilidades internas dependam diretamente de detalhes do sistema externo.

Escopo:
- aplicativo móvel;
- API/backend;
- persistência;
- agenda e agendamento;
- integração com prontuário eletrônico.

Restrições:
- manter o nível C4 Container;
- não representar classes, componentes, endpoints ou tabelas;
- não assumir tecnologias específicas;
- não introduzir microsserviços sem justificativa;
- representar o prontuário como sistema externo;
- manter a integração externa encapsulada;
- mostrar apenas dependências relevantes ao escopo.

Entregue:
1. brevemente, liste as suposições necessárias;
2. gere o código Mermaid completo;
3. explique brevemente as principais decisões representadas.

Não invente fatos ausentes do contexto.
```

### 10.3 Prompt para o diagrama comportamental

```text
Você é um arquiteto de software sênior. Gere um diagrama de sequência em Mermaid para representar a jornada crítica de agendamento de uma consulta.

Contexto:

O sistema é um aplicativo móvel de agendamento de consultas médicas. Pacientes e médicos utilizam o mesmo aplicativo.

O aplicativo se comunica com uma API/backend modular. O backend consulta e persiste informações em um único banco de dados relacional.

O paciente deve estar identificado para realizar um agendamento. Somente horários disponíveis podem ser agendados e um mesmo horário não pode ser reservado simultaneamente por dois pacientes.

Após o registro e confirmação do agendamento, o backend pode atualizar o sistema externo de prontuário eletrônico. Essa integração deve permanecer encapsulada no backend.

O mecanismo de notificações não deve assumir um provedor tecnológico específico.

Escopo da sequência:
- paciente consulta horários;
- aplicativo solicita disponibilidade ao backend;
- backend consulta o banco;
- paciente seleciona um horário;
- backend valida a disponibilidade;
- agendamento é registrado;
- sistema confirma o agendamento;
- backend realiza a integração com o prontuário;
- representar também o cenário de horário indisponível.

Restrições:
- utilizar Mermaid;
- não representar endpoints;
- não assumir protocolos;
- não detalhar tecnologias;
- distinguir claramente sistema externo;
- não inventar comportamento para situações que não foram definidas.

Entregue o código Mermaid completo e, depois, liste as suposições utilizadas.
```

## 11. Rastreabilidade

Os prompts acima representam a intenção de manter rastreável o processo de utilização da GenAI. As respostas geradas pelo modelo foram tratadas como propostas iniciais e passaram por revisão humana antes de serem incorporadas aos artefatos finais.

As versões finais dos diagramas estão disponíveis em:

* [`diagrams/container.md`](diagrams/container.md)
* [`diagrams/sequence.md`](diagrams/sequence.md)

A documentação consolidada está disponível em [`README.md`](README.md).
