import pandas as pd
import numpy as np
import sympy as sym
from matplotlib import pyplot as plt
from sympy import sympify
from tabulate import tabulate
from collections import defaultdict


def binary_search(f, a, b, l, eps) -> None:

	r = defaultdict(list)
	k = 1

	while True:
		r[k].append(a)
		r[k].append(b)

		ck = (a + b) / 2
		r[k].append(ck)

		if b - a <= l:
			break

		lmbd, mu = ck - eps, ck + eps

		r[k].append(lmbd)
		r[k].append(mu)

		if f(lmbd) > f(mu):
			a = lmbd
		else:
			b = mu

		k += 1

	print('\n\n')
	print(
		tabulate(
			pd.DataFrame.from_dict(r, orient='index').replace(np.nan, '-'),
			headers=['Iteration', 'a\u2096', 'b\u2096', 'c\u2096', '\u03bb', '\u03bc'],
			tablefmt='pretty'
		)
	)
	print('\n\n')


def golden_section_search(f, a, b, l) -> None:

	r = defaultdict(list)
	k = 1
	golden_ratio = 0.382
	q_golden_ratio = 0.618
	lmbd = a + golden_ratio * (b - a)
	mu = a + q_golden_ratio * (b - a)

	while True:

		r[k].append(a)
		r[k].append(b)

		c = b - a
		r[k].append(c)

		r[k].append(lmbd)
		r[k].append(mu)

		f_lmbd = f(lmbd)
		f_mu = f(mu)
		r[k].append(f_lmbd)
		r[k].append(f_mu)

		if c <= l:
			r['Solution'].append((a+b)/2)
			break

		if f_lmbd > f_mu:
			a = lmbd
			lmbd = mu
			mu = a + q_golden_ratio * (b - a)

		else:
			b = mu
			lmbd = a + golden_ratio * (b - a)
			mu = lmbd

		k += 1

	print('\n\n')
	print(
		tabulate(
			pd.DataFrame.from_dict(r, orient='index').replace(np.nan, '-'),
			headers=[
				'Iteration',
				'a\u2096',
				'b\u2096',
				'c\u2096',
				'\u03bb\u2096',
				'\u03bc\u2096',
				'f(\u03bb\u2096)',
				'f(\u03bc\u2096)',
				'Solution point'
			],
			tablefmt='pretty'
		)
	)
	print('\n\n')


def bolcano_search(f_pr, a, b, eps):

	r = defaultdict(list)
	k = 1

	while True:
		r[k].append(a)
		r[k].append(b)

		c = (a+b) / 2
		r[k].append(c)

		f_pr_c = f_pr(c)
		r[k].append(abs(f_pr_c))

		if abs(f_pr_c) <= eps:
			break

		if f_pr_c > 0:
			a = c
		else:
			b = c

		k += 1

		if k > 1000:
			raise ValueError('Method diverges.')

	print('\n\n')
	print(
		tabulate(
			pd.DataFrame.from_dict(r, orient='index').replace(np.nan, '-'),
			headers=['Iteration', 'a\u2096', 'b\u2096', 'c\u2096', '|f\'(x)|'],
			tablefmt='pretty'
		)
	)
	print('\n\n')


def one_dimensional_newton(f_first_pr, f_second_pr, x0, eps):

	x = x0
	k = 1

	while True:

		print(f'Iteration # {k}')
		x -= (f_first_pr(x) / f_second_pr(x))

		print(f'x{k} = {x}')

		if abs(f_first_pr(x)) <= eps:
			print(f'f\'({x}) = {f_first_pr(x)}\nf\'({x}) < \u03b5 : True \n\nSolution: {x}\n')
			break

		print(f'f\'({x}) = {f_first_pr(x)}\nf\'({x}) < \u03b5 : False\n')
		k += 1

	print('----------------------------\n')


def one_dimensional_f_extr(f, a, b):
	f_copy = f
	x = sym.Symbol('x')
	f1dx = sym.diff(f, x)
	f = lambda x: sympify(f_copy).subs({'x': x}).evalf()

	print('\n----------------------------------------------------------------------')

	print(
		f'First order derivative: {f1dx}\nSolving {f1dx} = 0'
	)
	print('----------------------------------------------------------------------\n')

	roots = sym.solveset(f1dx, x, domain=sym.Reals)

	if type(roots) != sym.FiniteSet:
		try:
			roots = sym.FiniteSet(*sym.solve(f1dx, x, domain=sym.Reals))
		except Exception as e:
			raise ValueError('EROOR WHILE CONVERTING SOLUTION TO FINITE_SET', repr(e))

	print('\n----------------------------------------------------------------------')
	print(f'Initial roots: {roots}')
	print('----------------------------------------------------------------------\n')

	for root in roots:
		if root < a or root > b:
			print(f'\n{root} \u2209 [{a}, {b}]')
			roots -= sym.FiniteSet(root)

	print('\n----------------------------------------------------------------------')
	print(f'Roots \u2208 [{a}, {b}]: {roots}')
	print('----------------------------------------------------------------------\n')

	f_values = [(a, f(a)), (b, f(b))]

	print('\n----------------------------------------------------------------------')

	print(f'a = {a}\nf(a) = {f(a)}\n')
	print(f'b = {b}\nf(b) = {f(b)}\n')

	for i, root in enumerate(roots):
		f_values.append((root, f(root)))
		print(f'x{i + 1} = {root}\nf(x{i + 1}) = {f(root)}\n')

	print('----------------------------------------------------------------------\n')

	print('\n----------------------------------------------------------------------')

	min_f, max_f = min(f_values, key=lambda x: x[1]), max(f_values, key=lambda x: x[1])

	print(f'Minimum {f_copy} value on [{a}, {b}]:\n{min_f}')
	print(f'Maximum {f_copy} value on [{a}, {b}]:\n{max_f}')

	print('----------------------------------------------------------------------\n')

	draw = input('\nShow points on graph? (y\\n): ')

	if draw == 'y':
		x = np.linspace(a, b, 100)
		y = [f(xs) for xs in x]

		plt.plot(x, y, color='blue')

		for i, fvals in enumerate(f_values):
			plt.scatter(float(fvals[0]), float(fvals[1]), color='red')

		plt.tight_layout()
		plt.show()

	else:
		print('\nDone\n')


def get_single_variable_function():
	return input('\nf(x) = ')


def print_menu():

	alg_descr = [
		('Дихотомический поиск', 'f, l, eps, a, b'),
		('Метод золотого сечения', 'f, l, a, b'),
		('Поиск Больцано', 'f\', eps, a, b'),
		('Одномерный метод Ньютона', 'f\', f\'\', x\u2080'),
		('Экстремум функции одной переменной', 'f, a, b')
	]

	menu_df = pd.DataFrame(alg_descr)
	menu_df.columns = ['Метод', 'Входные параметры']
	menu_df.index += 1

	print(
		tabulate(
			menu_df, headers=menu_df.columns, tablefmt='pretty', showindex=True
		)
	)


def get_sv_func():
	input_func = input('\nf(x) = ')
	f = lambda x: sympify(input_func).subs({'x': x}).evalf()
	return f


def get_first_order_deriv():
	input_func = input('\nf\'(x) = ')
	f_pr = lambda x: sympify(input_func).subs({'x': x}).evalf()
	return f_pr


def get_second_order_deriv():
	input_func = input('\nf\'\'(x) = ')
	f_double_pr = lambda x: sympify(input_func).subs({'x': x}).evalf()
	return f_double_pr


def get_boundary():
	a, b = [float(x) for x in input('[a, b] = ').split()]
	return a, b


def get_l():
	return float(input('Enter l: '))


def get_eps():
	return float(input('Enter eps: '))


def get_x0():
	return float(input('Enter x0: '))


def main():

	print_menu()

	while True:

		method = input('\nSelect method (by index): ')

		if method == '1':
			f = get_sv_func()
			a, b = get_boundary()
			l = get_l()
			eps = get_eps()

			binary_search(f, a, b, l, eps)

		elif method == '2':
			f = get_sv_func()
			a, b = get_boundary()
			l = get_l()

			golden_section_search(f, a, b, l)

		elif method == '3':
			f_pr = get_first_order_deriv()
			a, b = get_boundary()
			eps = get_eps()

			bolcano_search(f_pr, a, b, eps)

		elif method == '4':
			f_first_pr = get_first_order_deriv()
			f_second_pr = get_second_order_deriv()
			x0 = get_x0()
			eps = get_eps()

			one_dimensional_newton(f_first_pr, f_second_pr, x0, eps)

		elif method == '5':
			f = get_single_variable_function()
			print(f)
			a, b = get_boundary()
			# f = '3*x**3 + 7*x**2 - 3*x + 2'
			# a, b = -5, 5
			one_dimensional_f_extr(f, a, b)

		else:
			raise ValueError('Unexpected method')


if __name__ == '__main__':
	main()
