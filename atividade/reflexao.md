# Reflexão sobre os prompts

## Influência na qualidade e diversidade

O prompt de cenários de integração direcionou a geração para o fluxo completo:
consulta de horários, reserva, persistência e atualização do prontuário. Isso
ajudou a relacionar os componentes envolvidos e a definir resultados observáveis
em cada etapa.

O prompt de erros e dados de teste ampliou a variedade dos casos ao enfatizar
entradas inválidas, horário inexistente, repetição de reserva e indisponibilidade
do prontuário. Ele complementou o fluxo principal com condições que poderiam
ser omitidas por um pedido genérico.

## Ajustes que ajudaram

Informar os endpoints e os comportamentos implementados tornou as sugestões
mais específicas. Também foi necessário declarar que o prontuário era simulado,
que o SQLite era o banco usado pelo protótipo e quais regras eram hipóteses.
Esses limites reduziram casos dependentes de funcionalidades que ainda não
existem.

## Resultado da execução

Preencher após executar a suíte:

- Comando usado:
- Quantidade de testes aprovados:
- Falhas encontradas:
- Casos alterados ou descartados após a execução:
- O que a execução revelou sobre os casos gerados:
