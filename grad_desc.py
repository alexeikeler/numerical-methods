import sympy as sp
import numpy as np

def main():

    f = input('f(x, y) = ')
    variables = sp.symbols('x, y')

    xk: list = [float(x) for x in input('x0 = ').split()]

    eps = float(input('eps = '))
    h = float(input('h = '))

    grad = [sp.diff(f, variable) for variable in variables]
    f_callable = lambda xk: sp.sympify(f).subs({'x': xk[0], 'y': xk[1]})

    grad_xy = lambda xy: np.array(
        [partial_deriv.subs({'x': xy[0], 'y': xy[1]}) for partial_deriv in grad]
    )

    xk_prev = xk
    for i in range(1000):
        xk -= (h*grad_xy(xk))

        f_xk = f_callable(xk)
        f_xk_prev = f_callable(xk_prev)
        abs_diff = abs(f_xk - f_xk_prev)

        if abs_diff < eps:
            print(f'\nx{i+1}: {xk} <---- Solution')
            print(f'|f(x{i+1}) - f(x{i})| < eps: True')
            print(f'|{f_xk} - {f_xk_prev}| < {eps}')
            print(f'{abs_diff} < {eps}: True')
            break

        print(f'\nx{i + 1} = {xk}')
        print(f'|f(x_{i+1}) - f(x_{i})| < eps: False')
        print(f'|{f_xk} - {f_xk_prev}| < {eps}')
        print(f'{abs_diff} < {eps}: False\n')

        xk_prev = xk


if __name__ == '__main__':
    main()