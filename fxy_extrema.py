import pandas as pd
import numpy as np
import sympy as sym
from tabulate import tabulate


def main():

    ############################################################

    n = int(input('Amount of variables: '))
    variables = sym.symbols(', '.join([f'x{i}' for i in range(1, n+1)]))
    f = input('f{0} = '.format(variables))

    
    partial_derivs = [sym.diff(f, variable) for variable in variables]


    print('\nPartial derivatives:', *partial_derivs, sep='\n')
    print('\nSystem of equations:')
    
    print(" __\n|")
    for part_deriv in partial_derivs:
        print(f'| {part_deriv} = 0')
    print("|__")
    
    roots = sym.solve(
        partial_derivs,
        variables,
        dict=True
    )

    if len(roots) == 0:
        print("\nSystem of equations has no solutions!")
        exit()
    
    print(f'\nPoints (system solutions): ', *roots, sep='\n')
    print()

    ############################################################

    h = []
    for part_deriv in partial_derivs:
        row = []
        for variable in variables:
            second_pd = sym.diff(part_deriv, variable)
            row.append(second_pd)
        h.append(row)

    dfhs = pd.DataFrame(h)
    rows, cols = dfhs.shape

    print('Hessian H:')
    print(
        tabulate(dfhs, tablefmt='pretty', showindex=False), '\n'
    )
    
    ############################################################

    h_in_roots = []
    minor_values = []

    for root in roots:
        h_in_root = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(sym.sympify(dfhs.loc[i, j].subs(root)))
            h_in_root.append(row)


        minor = []

        for i in range(n):
            matrix = np.array(h_in_root)
            minor.append(
                sym.Matrix(matrix[:i+1, :i+1]).det()
            )

        minor_values.append(minor)

        h_in_roots.append(h_in_root)

    ############################################################

    for i, h in enumerate(h_in_roots):
        dfhs = pd.DataFrame(h)
        
        f_val = sym.sympify(f).subs(roots[i])

        print(f'H{roots[i]}:')
        print(
            tabulate(dfhs, tablefmt='pretty', showindex=False)
        )
        
        print(f'Minor values: {minor_values[i]}\n')
        print(f'f({roots[i]}) = {f_val}\n')

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
        print('--------------------------------------------------')
        

if __name__ == '__main__':
    main()