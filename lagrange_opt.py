import sympy as sp
sp.init_printing(use_latex=True)


def solve(f, variables, lagrage_multipliers, constraints):
    # Lagrange function is sum of products of contraint and lagrange multiplier

    lf = f
    for index, contraint in enumerate(constraints):
        lf += contraint * lagrage_multipliers[index]

    print('\n------------------------------------------------------\n')
    print('Lagrangian: ')
    sp.pprint(lf)
    print('\n------------------------------------------------------\n')

    print('\n------------------------------------------------------\n')
    grad_lf = [sp.diff(lf, variable) for variable in variables]
    print('Partial derivatives of Lagrangian: \n')
    for grad in grad_lf:
        sp.pprint(grad)
    print('\n------------------------------------------------------\n')

    print('\n------------------------------------------------------\n')
    print('System of equations (all = 0): \n')

    eqs = grad_lf
    for constraint in constraints:
        eqs = eqs + [constraint]

    for eq in eqs:
        sp.pprint(eq)
    print('\n------------------------------------------------------\n')

    solutions = sp.solve(eqs, variables+lagrage_multipliers, dict=True)

    ###
    print('\n------------------------------------------------------\n')
    hessian = sp.Matrix()
    for i, grad in enumerate(grad_lf):
        row = []
        for variable in variables:
            row.append(sp.diff(grad, variable))
        hessian = hessian.row_insert(i, sp.Matrix([row]))

    print('Hessian H:\n')
    sp.pprint(hessian)
    print('\n------------------------------------------------------\n')

    ###

    for index, solution in enumerate(solutions):

        h_in_point = sp.Matrix()
        rows = sp.shape(hessian)[0]

        for i in range(rows):
            row = hessian.row(i)
            evaluated_row = []
            for item in row:
                evaluated_row.append(item.subs(solution))
            h_in_point = h_in_point.row_insert(i, sp.Matrix([evaluated_row]))

        print(f'\n--------------------Solution # {index+1}----------------------')
        print(f'Point # {index+1}:\n')
        sp.pprint(solution)

        print(f'\nFunction value in point # {index + 1}:\n')
        sp.pprint(f.subs(solution))

        print(f'\nH in this point:\n')
        sp.pprint(h_in_point)

        if h_in_point.is_positive_definite:
            print(f'\nFunction achives local MINIMUM in point # {index+1} subject to constraint.\n')
        else:
            print(f'\nFunction achives local MAXIMUM in point # {index+1} subject to constraint.\n')

        print('------------------------------------------------------\n')


def main():

    variables_number = int(input('Number of variables: '))
    variables = list(sp.var(' ,'.join([f'x{i}' for i in range(1, variables_number+1)])))
    print(variables)
    f = sp.parse_expr(input(f'f{variables} = '))

    constrains_number = int(input('Number of constraints: '))
    constrains = [sp.parse_expr(input(f'Constrain # {i}: ')) for i in range(1, constrains_number+1)]
    print(constrains)
    lmbds = [sp.symbols(f'lambda{i}') for i in range(1, constrains_number+1)]
    print(lmbds)
    solve(
         f,
         variables,
         lmbds,
         constrains,
    )


if __name__ == '__main__':
    main()
