from enum import Enum


class CinemaErrors(Enum):
    CINE_NO_ENCONTRADO = 'CINE_NO_ENCONTRADO'
    HORARIO_NO_ENCONTRADO = 'HORARIO_NO_ENCONTRADO'
    BUTACA_OCUPADA = 'BUTACA_OCUPADA'
