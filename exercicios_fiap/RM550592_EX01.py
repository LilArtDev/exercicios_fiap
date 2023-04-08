from enum import Enum
from typing import Union


class SignatureTypes(Enum):
    BASIC = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4


SIGNATURE_PERCENTAGES = {"BASIC": 0.3,
                         "SILVER": 0.2,
                         "GOLD": 0.1,
                         "PLATINUM": 0.05}


def print_line():
    return print()


def format_currency(value: Union[int, float]):
    return f"R$ {value:.2f}"


def calculate_amount_to_pay(signature_type: int, annual_revenue: float) -> float:
    return annual_revenue * SIGNATURE_PERCENTAGES[SignatureTypes(signature_type).name]


try:
    print('Bem vindo!')
    print_line()

    print('1. Basic')
    print('2. Silver')
    print('3. Gold')
    print('4. Platinum')
    print_line()

    customer_signature_type = int(
        input('Informe qual é o tipo da assinatura: '))

    if (SignatureTypes(customer_signature_type) not in SignatureTypes.__members__.values()):
        raise ValueError('Tipo de assinatura inválida')

    customer_annual_revenue = float(
        input('Agora informe o faturamento anual: R$ '))
    print_line()

    if (customer_annual_revenue < 0):
        raise ValueError('O faturamento não deve ser negativo!')

    amount_to_pay = calculate_amount_to_pay(
        customer_signature_type, customer_annual_revenue)

    print(f'Você deve pagar a quantia de {format_currency(amount_to_pay)}')

except ValueError as e:
    print_line()
    print('Erro no dado enviado, ', e)

finally:
    print_line()
    print('Encerrando o programa...')
