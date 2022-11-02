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
