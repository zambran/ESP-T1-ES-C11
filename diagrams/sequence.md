sequenceDiagram
    actor Paciente
    participant App as Aplicativo Mobile
    participant API as API / Backend
    participant BD as Banco de Dados
    participant PE as Prontuário Eletrônico

    Paciente->>App: Consulta horários disponíveis
    App->>API: Solicita horários
    API->>BD: Consulta disponibilidade
    BD-->>API: Retorna horários disponíveis
    API-->>App: Exibe horários disponíveis

    Paciente->>App: Seleciona horário
    App->>API: Solicita agendamento
    API->>BD: Valida disponibilidade

    alt Horário disponível
        API->>BD: Registra agendamento
        BD-->>API: Agendamento registrado
        API-->>App: Confirma agendamento
        App-->>Paciente: Exibe confirmação

        API->>PE: Atualiza informações da consulta
        PE-->>API: Retorna resultado da integração
    else Horário indisponível
        BD-->>API: Horário já reservado
        API-->>App: Informa indisponibilidade
        App-->>Paciente: Solicita escolha de outro horário
    end
