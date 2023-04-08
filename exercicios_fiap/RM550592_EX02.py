from enum import Enum
from typing import Union


class WeekDays(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5


DAY_LABELS = {"SEGUNDA": 'Segunda',
              "TERCA": 'Terça',
              "QUARTA": 'Quarta',
              "QUINTA": 'Quarta',
              "SEXTA": 'Sexta'}


def print_line():
    return print()

def render_day_name(day: WeekDays) -> str:
    return f"{DAY_LABELS[day.name]} Feira"

try:
    print('Bem vindo!')
    print_line()

    more_voted_day = {"day": WeekDays.SEGUNDA, "votes": 0}

    for day in WeekDays:
        day_votes = int(
            input(f'Informe quantos alunos votaram na {render_day_name(day)}: '))

        if (day_votes < 0):
            raise ValueError('O número de votos não pode ser negativo!')
        elif (day_votes > more_voted_day["votes"]):
            more_voted_day = {"day": day, "votes": day_votes}

    print_line()
    print(
        f'O dia mais votado para a realização das lives foi {render_day_name(more_voted_day["day"])}!')

except ValueError as e:
    print_line()
    print('Erro no dado enviado, ', e)

finally:
    print_line()
    print('Encerrando o programa...')
