import pytest
from fastapi.testclient import TestClient

from app.agendamentos import Agenda
from app.api import app, get_agenda, get_prontuario
from app.database import Database
from app.prontuario import ProntuarioFake


@pytest.fixture
def prontuario_fake() -> ProntuarioFake:
    return ProntuarioFake()


@pytest.fixture
def client(tmp_path, prontuario_fake):
    banco_temporario = Database(str(tmp_path / "testes.sqlite3"))
    agenda_temporaria = Agenda(banco_temporario)

    app.dependency_overrides[get_agenda] = lambda: agenda_temporaria
    app.dependency_overrides[get_prontuario] = lambda: prontuario_fake

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
