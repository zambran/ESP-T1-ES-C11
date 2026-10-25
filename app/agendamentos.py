import uuid

from .database import Database


class HorarioIndisponivel(Exception):
    """O horário não existe ou já foi reservado."""


class Agenda:
    def __init__(self, database: Database):
        self.database = database

    def listar_disponiveis(self, medico_id: str) -> list[str]:
        with self.database.connect() as connection:
            rows = connection.execute(
                """
                SELECT slots.starts_at
                FROM slots
                LEFT JOIN appointments
                    ON appointments.doctor_id = slots.doctor_id
                    AND appointments.starts_at = slots.starts_at
                WHERE slots.doctor_id = ?
                    AND appointments.id IS NULL
                ORDER BY slots.starts_at
                """,
                (medico_id,),
            ).fetchall()

        return [row["starts_at"] for row in rows]

    def agendar(
        self,
        paciente_id: str,
        medico_id: str,
        horario: str,
    ) -> dict:
        with self.database.connect() as connection:
            # Serializa reservas concorrentes para evitar dupla marcação.
            connection.execute("BEGIN IMMEDIATE")

            slot = connection.execute(
                """
                SELECT 1
                FROM slots
                WHERE doctor_id = ? AND starts_at = ?
                """,
                (medico_id, horario),
            ).fetchone()

            if slot is None:
                raise HorarioIndisponivel

            reservado = connection.execute(
                """
                SELECT 1
                FROM appointments
                WHERE doctor_id = ? AND starts_at = ?
                """,
                (medico_id, horario),
            ).fetchone()

            if reservado is not None:
                raise HorarioIndisponivel

            appointment_id = str(uuid.uuid4())
            connection.execute(
                """
                INSERT INTO appointments (id, patient_id, doctor_id, starts_at)
                VALUES (?, ?, ?, ?)
                """,
                (appointment_id, paciente_id, medico_id, horario),
            )

        return {
            "id": appointment_id,
            "paciente_id": paciente_id,
            "medico_id": medico_id,
            "horario": horario,
        }
