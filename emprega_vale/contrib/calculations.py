from collections import namedtuple
from decimal import Decimal
from math import inf
from typing import Union


def calculate_salary_with_social_security_discount(salary: Decimal) -> Union[int, float]:
    INSS = namedtuple('INSS', ['initial_value', 'limit_value', 'aliquot', 'deductible_value'])
    divisor = Decimal('100')

    deducted = Decimal('713.08')

    first_range = INSS(Decimal('1045'), Decimal('1045'), Decimal('7.5'), Decimal('0'))
    second_range = INSS(Decimal('1045.01'), Decimal('2089.60'), Decimal('9'), Decimal('15.67'))
    third_range = INSS(Decimal('2089.61'), Decimal('3134.40'), Decimal('12'), Decimal('78.36'))
    forth_range = INSS(Decimal('3134.41'), Decimal('6101.06'), Decimal('14'), Decimal('141.05'))

    ranges = (first_range, second_range, third_range, forth_range)

    for r in ranges:
        if r.initial_value <= salary <= r.limit_value:
            deducted = (salary * (r.aliquot / divisor)) - r.deductible_value
            break

    return salary - deducted


def calculate_salary_with_income_tax_discount(salary: Union[int, float], dependents: int) -> Union[int, float]:
    IRRF = namedtuple('IRRF', ['initial_value', 'limit_value', 'aliquot', 'deductible_value'])
    divisor = Decimal('100')
    dependents_deduction = dependents * Decimal('189.59')

    first_range = IRRF(Decimal('0'), Decimal('1903.98'), Decimal('0'), Decimal('0'))
    second_range = IRRF(Decimal('1903.99'), Decimal('2826.65'), Decimal('7.5'), Decimal('142.80'))
    third_range = IRRF(Decimal('2826.66'), Decimal('3751.05'), Decimal('15'), Decimal('354.80'))
    forth_range = IRRF(Decimal('3751.06'), Decimal('4664.68'), Decimal('22.5'), Decimal('636.13'))
    fifth_range = IRRF(Decimal('4664.69'), inf, Decimal('27.5'), Decimal('869.36'))

    ranges = (first_range, second_range, third_range, forth_range, fifth_range)

    for r in ranges:
        if r.initial_value <= salary <= r.limit_value:
            deducted = ((salary - max(0, dependents_deduction)) * (r.aliquot / divisor)) - r.deductible_value
            break

    return salary - deducted
