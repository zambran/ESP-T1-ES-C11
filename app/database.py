import os
import sqlite3
from pathlib import Path


HORARIOS_INICIAIS = [
    ("medico-1", "2026-11-02T09:00:00"),
    ("medico-1", "2026-11-02T10:00:00"),
]


class Database:
    def __init__(self, path: str | None = None):
        configured_path = path or os.getenv(
            "AGENDAMENTOS_DB_PATH",
            "data/agendamentos.sqlite3",
        )
        self.path = configured_path

        if self.path != ":memory:":
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)

        self.initialize()

    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS slots (
                    doctor_id TEXT NOT NULL,
                    starts_at TEXT NOT NULL,
                    PRIMARY KEY (doctor_id, starts_at)
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS appointments (
                    id TEXT PRIMARY KEY,
                    patient_id TEXT NOT NULL,
                    doctor_id TEXT NOT NULL,
                    starts_at TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE (doctor_id, starts_at),
                    FOREIGN KEY (doctor_id, starts_at)
                        REFERENCES slots (doctor_id, starts_at)
                )
                """
            )
            connection.executemany(
                """
                INSERT OR IGNORE INTO slots (doctor_id, starts_at)
                VALUES (?, ?)
                """,
                HORARIOS_INICIAIS,
            )
