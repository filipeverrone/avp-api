from enum import Enum


def convert_to_float(num):
    if not num:
        return None
    return float(num)


def take_results_positions(data: dict):
    i = data['i']
    n = data['n']
    P = data['P']
    R = data['R']
    S = data['S']

    show = ''
    for key in data.keys():
        show += f'<br>{key} = {data[key]}</br>'

    return show + '<br />'


def format_float(num: float):
    return f'{num:.2f}'


class RateConvertEnum(Enum):
    month = 1
    bimester = 2
    trimester = 3
    four_month = 4
    five_month = 5
    semester = 6
    year = 12


def rate_conversion(rate_from: RateConvertEnum, rate_to: RateConvertEnum):
    if rate_from.value == RateConvertEnum.month.value:
        return rate_to.value
    if rate_from.value == RateConvertEnum.year.value:
        return 12 / rate_to.value
    return 1
