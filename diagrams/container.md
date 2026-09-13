flowchart LR
    Paciente["Paciente"]
    Medico["Médico"]

    subgraph Sistema["Sistema de Agendamento de Consultas"]
        App["Aplicativo Mobile<br/>Interface para pacientes e médicos"]

        Backend["API / Backend<br/>Aplicação modular"]
        Banco[("Banco de Dados<br/>Relacional")]

        App -->|"Solicita operações"| Backend
        Backend -->|"Lê e grava dados"| Banco
    end

    Prontuario["Sistema de Prontuário Eletrônico<br/><<external>>"]

    Paciente -->|"Utiliza"| App
    Medico -->|"Utiliza"| App

    Backend -->|"Integração com prontuário"| Prontuario
