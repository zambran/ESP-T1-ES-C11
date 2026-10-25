class ProntuarioIndisponivel(Exception):
    """O sistema externo de prontuário não está disponível."""


class ProntuarioFake:
    """
    Simulação local do prontuário eletrônico.

    Nos testes, use falhar=True para exercitar o cenário de indisponibilidade.
    Substitua esta classe por um adaptador HTTP quando houver um contrato real
    do sistema externo.
    """

    def __init__(self, falhar: bool = False):
        self.falhar = falhar
        self.agendamentos_recebidos: list[dict] = []

    def atualizar(self, agendamento: dict) -> None:
        if self.falhar:
            raise ProntuarioIndisponivel

        self.agendamentos_recebidos.append(agendamento)
