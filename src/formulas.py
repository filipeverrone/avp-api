def get_S_from_R(i, n, R): return R * (((1 + i) ** n) - 1) / i
def get_S_from_P(i, n, P): return P * (1 + i) ** n
def get_P_from_S(i, n, S): return S / ((1 + i) ** n)
def get_P_from_R(i, n, R): return R * ((1 - (1 / ((1 + i) ** n))) / i)
def get_R_from_P(i, n, P): return P / ((1 - (1 / ((1 + i) ** n))) / i)
def get_R_from_S(i, n, S): return S * i / (((1 + i) ** n) - 1)


def main(
    i=None,
    n=None,
    S=None,
    P=None,
    R=None,
):
    if i == None or n == None:
        raise Exception()

    i = i / 100

    if S == None:
        if P == None:
            if R == None:
                raise Exception()
            S = get_S_from_R(i, n, R)
            P = get_P_from_R(i, n, R)
        else:
            S = get_S_from_P(i, n, P)
            R = R if R != None else get_R_from_P(i, n, P)
    elif P == None:
        P = get_P_from_S(i, n, S)
        R = R if R != None else get_R_from_S(i, n, S)
    else:
        R = R if R != None else get_R_from_S(i, n, S)

    i = 100 * i

    print(
        f'''
    i = {i}%
    n = {n}
    S = {S} (amount)
    P = {P} (principal, initial capital)
    R = {R} (payment)
        '''
    )

    return {
        'i': f'{i}%',
        'n': n,
        'S': S,
        'P': P,
        'R': R,
    }
