HORARIO_EXEMPLO = "2026-11-02T09:00:00"


def payload_agendamento() -> dict:
    return {
        "paciente_id": "paciente-123",
        "medico_id": "medico-1",
        "horario": HORARIO_EXEMPLO,
    }


def test_agendamento_atualiza_prontuario_e_remove_horario_disponivel(
    client,
    prontuario_fake,
):
    horarios_antes = client.get(
        "/horarios",
        params={"medico_id": "medico-1"},
    )
    assert horarios_antes.status_code == 200
    assert HORARIO_EXEMPLO in horarios_antes.json()["horarios"]

    resposta = client.post("/agendamentos", json=payload_agendamento())

    assert resposta.status_code == 201
    dados = resposta.json()
    assert dados["paciente_id"] == "paciente-123"
    assert dados["medico_id"] == "medico-1"
    assert dados["horario"] == HORARIO_EXEMPLO
    assert dados["integracao_prontuario"] == "atualizada"
    assert len(prontuario_fake.agendamentos_recebidos) == 1

    horarios_depois = client.get(
        "/horarios",
        params={"medico_id": "medico-1"},
    )
    assert HORARIO_EXEMPLO not in horarios_depois.json()["horarios"]


def test_nao_permite_reservar_duas_vezes_o_mesmo_horario(client):
    primeira_resposta = client.post(
        "/agendamentos",
        json=payload_agendamento(),
    )
    segunda_resposta = client.post(
        "/agendamentos",
        json={
            **payload_agendamento(),
            "paciente_id": "paciente-456",
        },
    )

    assert primeira_resposta.status_code == 201
    assert segunda_resposta.status_code == 409
    assert segunda_resposta.json()["detail"] == "Horário indisponível"


def test_agendamento_fica_confirmado_se_prontuario_falhar(
    client,
    prontuario_fake,
):
    prontuario_fake.falhar = True

    resposta = client.post("/agendamentos", json=payload_agendamento())

    assert resposta.status_code == 201
    assert resposta.json()["integracao_prontuario"] == "pendente"

    horarios_depois = client.get(
        "/horarios",
        params={"medico_id": "medico-1"},
    )
    assert HORARIO_EXEMPLO not in horarios_depois.json()["horarios"]


def test_rejeita_agendamento_sem_paciente(client):
    payload_invalido = {
        "medico_id": "medico-1",
        "horario": HORARIO_EXEMPLO,
    }

    resposta = client.post("/agendamentos", json=payload_invalido)

    assert resposta.status_code == 422


def test_rejeita_horario_que_nao_existe(client):
    payload = {
        **payload_agendamento(),
        "horario": "2026-11-02T15:00:00",
    }

    resposta = client.post("/agendamentos", json=payload)

    assert resposta.status_code == 409
    assert resposta.json()["detail"] == "Horário indisponível"
