# Prompts usados na atividade

## Contexto fornecido à LLM

O sistema é um protótipo de agendamento de consultas. A API consulta horários
disponíveis e registra agendamentos em SQLite. O backend tenta atualizar um
sistema externo de prontuário por meio de um adaptador substituível por um fake.

Hipóteses deste protótipo:

- cada horário pertence a um médico;
- um horário não pode ser reservado duas vezes;
- o agendamento é confirmado antes da atualização do prontuário;
- se o prontuário falhar, o agendamento continua confirmado e a integração fica
  pendente;
- não há autenticação nem provedor real de prontuário implementados.

## Prompt 1 — Geração de cenários de integração

> Com base no contexto e nos arquivos `app/api.py`, `app/agendamentos.py`,
> `app/database.py` e `app/prontuario.py`, proponha cenários de teste de
> integração para o fluxo de agendamento.
>
> Para cada cenário, informe: objetivo, pré-condições, chamadas à API em ordem,
> resultado HTTP esperado, alterações esperadas no SQLite e resultado esperado
> da integração com o prontuário. Inclua o fluxo de sucesso, horário já
> reservado e falha do prontuário. Não invente endpoints ou regras além do
> contexto; marque qualquer hipótese adicional.

### Registro do resultado

A primeira geração foi organizada em `casos-gerados.md`. Os casos foram
limitados aos endpoints existentes e às regras explicitamente assumidas.

## Prompt 2 — Geração de casos de erro e dados de teste

> Com base no mesmo contexto e nos arquivos da API, proponha casos adicionais
> de integração focados em entradas inválidas, horários inexistentes,
> repetição de reserva e falha do prontuário.
>
> Para cada caso, forneça dados concretos de entrada, passos reproduzíveis e
> resultado observável na API e no SQLite. Indique quais casos podem ser
> automatizados com o prontuário fake. Não presuma autenticação, campos ou
> respostas que não existam no código.

### Registro do resultado

A segunda geração destacou validação de campos, horário inexistente e
persistência do agendamento quando o fake do prontuário falha. Os casos
selecionados também estão em `casos-gerados.md`.

## Ajustes feitos nos prompts

- Forneci o contexto arquitetural junto dos arquivos realmente implementados.
- Pedi resultados observáveis na API e no SQLite para evitar casos vagos.
- Especifiquei que o prontuário seria simulado e que não havia autenticação.
- Limitei os prompts aos endpoints existentes para reduzir sugestões inventadas.
