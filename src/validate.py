from re import match


def validate_type_request(data: dict):
    i = data['i'].strip()
    n = data['n'].strip()
    P = data['P']
    R = data['R']
    S = data['S']
    validate = [P, R, S]
    triangle = None

    if not match(r'^(([0-9]*[.])?[0-9]+)$', str(i)):
        return 'i'
    if not match(r'^([\s\d]+)$', str(n)):
        return 'n'
    for value in validate:
        if value == None:
            continue
        elif not match(r'^(([0-9]*[.])?[0-9]+)$', str(value.strip())):
            return 'triangle value'

        triangle = value

    if triangle == None:
        return 'triangle value'
    return None


def validate_rate(i):
    if not match(r'^(([0-9]*[.])?[0-9]+)$', str(i)):
        return False
    return True
