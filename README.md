# Agendamento de Consultas

Protótipo acadêmico de uma API para consultar horários e registrar agendamentos. O projeto usa SQLite para persistência e simula a integração com um sistema externo de prontuário por meio de um fake substituível nos testes.

## Escopo do protótipo

O fluxo implementado é:

1. Consultar horários disponíveis para um médico.
2. Reservar um horário.
3. Persistir o agendamento no SQLite.
4. Tentar atualizar o prontuário simulado.

Se o prontuário simulado falhar, o agendamento continua confirmado e a API informa que a integração está pendente. Essa é uma hipótese adotada para o exercício, não um requisito confirmado de um sistema real.

O protótipo não implementa autenticação, cancelamento, aplicativo móvel nem integração com um prontuário real. Os horários iniciais são dados de exemplo.

## Requisitos

- Python 3.10 ou superior
- pip

## Instalação

Abra um terminal na pasta raiz do repositório.

No PowerShell do Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se o PowerShell impedir a ativação do ambiente virtual, abra o Prompt de Comando e use:

```bat
.venv\Scripts\activate.bat
```

## Executar a API

Na pasta raiz do projeto, com o ambiente virtual ativado:

```powershell
uvicorn app.api:app --reload
```

A API estará disponível em:

- Base: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs
- Verificação de saúde: http://127.0.0.1:8000/health

O SQLite é criado automaticamente em `data/agendamentos.sqlite3`, relativo à pasta de onde a API foi iniciada.

Para usar outro arquivo de banco no PowerShell, defina a variável antes de iniciar a API:

```powershell
$env:AGENDAMENTOS_DB_PATH = "data/demo.sqlite3"
uvicorn app.api:app --reload
```

## Experimentar os endpoints

Os exemplos abaixo usam PowerShell.

### Consultar horários

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/horarios?medico_id=medico-1" `
  -Method Get
```

### Criar um agendamento

```powershell
$body = @{
  paciente_id = "paciente-123"
  medico_id = "medico-1"
  horario = "2026-11-02T09:00:00"
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/agendamentos" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

Uma reserva bem-sucedida retorna o agendamento e o estado da integração com o prontuário. Uma nova tentativa de reservar o mesmo horário retorna HTTP `409`. Uma solicitação com campos obrigatórios ausentes retorna HTTP `422`.

## Executar os testes

Com o ambiente virtual ativado, na pasta raiz do projeto:

```powershell
pytest -v
```

Os testes usam um banco SQLite temporário e um prontuário fake. Eles cobrem a consulta e reserva de horário, a tentativa de duplicar uma reserva, a falha do prontuário e entradas inválidas.

## Estrutura do projeto

```text
.
├── app/
│   ├── __init__.py
│   ├── agendamentos.py
│   ├── api.py
│   ├── database.py
│   └── prontuario.py
├── atividade/
│   ├── casos-gerados.md
│   ├── prompts.md
│   └── reflexao.md
├── tests/
│   ├── conftest.py
│   └── integration/
│       └── test_agendamentos.py
└── requirements.txt
```

## Atividade sobre prompts e testes de integração

A pasta `atividade/` registra os prompts usados para propor cenários de integração, os casos selecionados e a reflexão sobre a qualidade e a diversidade das sugestões.

Os casos foram associados a testes automatizados. Depois de executar a suíte, complete `atividade/reflexao.md` com o comando utilizado, os resultados observados e quaisquer ajustes feitos nos casos.
