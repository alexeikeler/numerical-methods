import pandas as pd
import numpy as np
import sympy as sym
from tabulate import tabulate


def main():

    n = int(input('Amount of variables: '))
    f = input('f = ')
    # n = 3
    # f = 'x1 ^ 3 + x2 ^ 2 + x3 ^ 2 + x2 * x3 - 3 * x1 + 6 * x2 + 2'
    # n = 2
    # f = '4*x1^2 + 3*x2^2 - 4*x1*x2 + x1'

    variables = sym.symbols(', '.join([f'x{i}' for i in range(1, n+1)]))

    partial_derivs = [sym.diff(f, variable) for variable in variables]

    roots = sym.solve(
        partial_derivs,
        variables
    )

    if type(roots) == dict:
        roots = [[float(value) for value in roots.values()]]

    print('\nPartial derivatives:', *partial_derivs, sep='\n')
    print(f'\nPoints: ', *roots, sep='\n')
    print()

    # 4*x1^2 + 3*x2^2 - 4*x1*x2 + x1
    # x1 ^ 3 + x2 ^ 2 + x3 ^ 2 + x2 * x3 - 3 * x1 + 6 * x2 + 2
    # sympify(input_func).subs({'x': x}).evalf()

    hessians = []
    minor_values = []

    for root in roots:
        hessian = []
        for part_deriv in partial_derivs:
            row = []
            for variable in variables:
                second_pd = sym.diff(part_deriv, variable)
                if n == 2:
                    row.append(
                        sym.sympify(second_pd).subs({'x1': root[0], 'x2': root[1]})
                    )
                elif n == 3:
                    row.append(
                        sym.sympify(second_pd).subs({'x1': root[0], 'x2': root[1], 'x3': root[2]})
                    )

            hessian.append(row)

        minor = []

        for i in range(n):
            matrix = np.array(hessian)
            minor.append(
                sym.Matrix(matrix[:i+1, :i+1]).det()
            )

        minor_values.append(minor)
        hessians.append(hessian)

    for i, hess in enumerate(hessians):
        dfhs = pd.DataFrame(hess)
        dfhs.index += 1
        print(f'H{roots[i]}:')
        print(
            tabulate(dfhs, headers=range(1, n+1), tablefmt='pretty'), '\n'
        )

        print(f'Minor values: {minor_values[i]}')

        if all(v > 0 for v in minor_values[i]):
            print(f'Point {roots[i]} is MINIMUM point.\n')
            continue

        if n == 2:
            if minor_values[i][1] > 0 and minor_values[i][0] < 0:
                print(f'Point {roots[i]} is MAXIMUM point.\n')
            else:
                print(f'There is no extremum in point {roots[i]}\n')

        if n == 3:
            if (minor_values[i][0] and minor_values[i][2] < 0) and (minor_values[i][1] > 0):
                print(f'Point {roots[i]} is MAXIMUM point.')

            elif minor_values[i][2] == 0:
                print(f'There is no extremum in point {roots[i]}\n')

            else:
                print(f'Point {roots[i]} is a seddle point\n')


if __name__ == '__main__':
    main()