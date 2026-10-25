# Casos de integração gerados e selecionados

Os casos foram propostos com apoio de LLM a partir do contexto e dos arquivos
do protótipo. O prontuário é um fake local; não há conexão com um sistema real.

| ID | Cenário | Resultado esperado | Teste automatizado |
|---|---|---|---|
| INT-01 | Consultar horários e reservar um horário disponível | A API responde 201, registra a consulta no SQLite, envia o registro ao fake e deixa de listar o horário como disponível | `test_agendamento_atualiza_prontuario_e_remove_horario_disponivel` |
| INT-02 | Dois pacientes tentam reservar o mesmo horário, em sequência | A primeira tentativa responde 201 e a segunda responde 409; o horário fica reservado uma única vez | `test_nao_permite_reservar_duas_vezes_o_mesmo_horario` |
| INT-03 | O prontuário fica indisponível após o registro da consulta | A API responde 201 com integração pendente; a consulta permanece registrada e o horário fica reservado | `test_agendamento_fica_confirmado_se_prontuario_falhar` |
| INT-04 | Enviar solicitação sem o identificador do paciente | A API responde 422 e não registra a consulta | `test_rejeita_agendamento_sem_paciente` |
| INT-05 | Tentar reservar um horário que não existe para o médico | A API responde 409 e não registra a consulta | `test_rejeita_horario_que_nao_existe` |

## Limites dos casos

- O fake valida o comportamento do backend diante de sucesso ou indisponibilidade,
  mas não verifica comunicação de rede com um prontuário real.
- A persistência usa SQLite local; o protótipo não define estratégia de
  implantação ou banco de produção.
- Os horários iniciais são dados de exemplo.
- A atividade não define autenticação, autorização ou regras de cancelamento.
