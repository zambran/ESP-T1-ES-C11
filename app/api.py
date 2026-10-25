from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from .agendamentos import Agenda, HorarioIndisponivel
from .database import Database
from .prontuario import ProntuarioFake, ProntuarioIndisponivel


app = FastAPI(
    title="API de Agendamento de Consultas",
    version="0.1.0",
)

database = Database()
agenda = Agenda(database)
prontuario = ProntuarioFake()


class AgendamentoInput(BaseModel):
    paciente_id: str = Field(min_length=1)
    medico_id: str = Field(min_length=1)
    horario: str = Field(min_length=1)


def get_agenda() -> Agenda:
    return agenda


def get_prontuario() -> ProntuarioFake:
    return prontuario


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/horarios")
def listar_horarios(
    medico_id: str,
    servico_agenda: Agenda = Depends(get_agenda),
) -> dict:
    return {
        "medico_id": medico_id,
        "horarios": servico_agenda.listar_disponiveis(medico_id),
    }


@app.post("/agendamentos", status_code=201)
def criar_agendamento(
    payload: AgendamentoInput,
    servico_agenda: Agenda = Depends(get_agenda),
    servico_prontuario: ProntuarioFake = Depends(get_prontuario),
) -> dict:
    try:
        registro = servico_agenda.agendar(
            paciente_id=payload.paciente_id,
            medico_id=payload.medico_id,
            horario=payload.horario,
        )
    except HorarioIndisponivel as exc:
        raise HTTPException(
            status_code=409,
            detail="Horário indisponível",
        ) from exc

    try:
        servico_prontuario.atualizar(registro)
    except ProntuarioIndisponivel:
        # Hipótese do exercício: o agendamento continua confirmado.
        return {
            **registro,
            "integracao_prontuario": "pendente",
        }

    return {
        **registro,
        "integracao_prontuario": "atualizada",
    }
