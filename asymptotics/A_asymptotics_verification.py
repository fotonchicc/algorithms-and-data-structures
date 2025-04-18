def parse_func(func):
    func_coeffs = list()
    values = func.replace('-', '+-').split('+')
    for value in values:
        value = value.strip()
        if value:
            degree = 0
            if 'x' in value:
                if 'x^' in value:
                    degree = value.split('x^')[1]
                    degree = int(degree)
                else:
                    degree = 1
            else:
                degree = 0
        if degree not in func_coeffs:
            func_coeffs.append(degree)

    return func_coeffs


def compare_func(f_coef, g_coef):

    max_f = max(f_coef, default=0)
    max_g = max(g_coef, default=0)

    if max_f < max_g:
        return 'YES', 'NO', 'NO'
    elif max_f > max_g:
        return 'NO', 'YES', 'NO'
    else:
        return 'YES', 'YES', 'YES'


f_input = input().strip()
g_input = input().strip()

f_x = parse_func(f_input)
g_x = parse_func(g_input)

Big_O, Big_Omega, Big_Theta = compare_func(f_x, g_x)

print(Big_O)
print(Big_Omega)
print(Big_Theta)