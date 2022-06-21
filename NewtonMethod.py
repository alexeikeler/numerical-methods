from tkinter import N
from utils import *

class NewtonMethod:
    def __init__(self, func, first_deriv, second_deriv, x0, eps):
        self.func = func
        self.first_deriv = first_deriv
        self.second_deriv = second_deriv
        self.x0 = x0
        self.eps = abs(eps)

        self.eps_char = '\u03B5'
        self.lambda_char = '\u03BB'
        self.mu_char = '\u03BC'

    def solve(self):
        print("=============")
        print("Метод Ньютона")
        print("=============\n")

        print(f"{self.eps_char} = {self.eps}")
        print(f"x0 = {self.x0}")
        print(f"f(x) = {str(self.func)}")
        print(f"f'(x) = {str(self.first_deriv)}")
        print(f"f\"(x) = {str(self.second_deriv)}")
        print("k = 0")
        print()

        i = -1
        curr_x = self.x0
        while True:
            i += 1
            print(f"Iteration {i+1}: ")
            f1 = self.first_deriv.eval(curr_x)
            f2 = self.second_deriv.eval(curr_x)
            print(f"f'(x{i}) = {str(self.first_deriv).replace('x', f'{curr_x:.4f}')} = {f1:.4f}")
            print(f"f\"(x{i}) = {str(self.second_deriv).replace('x', f'{curr_x:.4f}')} = {f2:.4f}")

            next_x = curr_x - f1 / f2
            print(f"x{i+1} = x{i} - f'(x{i}) / f\"(x{i}) = {curr_x:.4f} - {f1:.4f}/{f2:.4f} = {curr_x:.4f} - {f1/f2:.4f} = {next_x:.4f}")

            f1_new = self.first_deriv.eval(next_x)


            if abs(f1_new) <= self.eps:
                print(f"|f'(x{i+1})| = |{str(self.first_deriv).replace('x', f'{next_x:.4f}')}| = |{f1_new:.4f}| = {abs(f1_new):.4f} <= {self.eps}")
                break

            print(f"|f'(x{i+1})| = |{str(self.first_deriv).replace('x', f'{next_x:.4f}')}| = |{f1_new:.4f}| = {abs(f1_new):.4f} > {self.eps}")
            curr_x = next_x

            print(f"k = {i+1}")
            print()

        res = next_x
        print()
        print("Result: ")
        print(f"x* = {res:.4f}")
        print(f"f(x*) = {str(self.func).replace('x', f'{res:.4f}')} = {self.func.eval(res):.4f}")


def albert_var():
    x0 = 1.8
    eps = 0.1
    func = Func(lambda x: x**3 - 2*x**2 + x - 1, "x^3 - 2*x^2 + x - 1")
    deriv = Func(lambda x: 3*x**2 - 4*x + 1, "3*x^2 - 4*x + 1")
    second_deriv = Func(lambda x: 6*x - 4, "6*x - 4")
    ds = NewtonMethod(func=func, first_deriv=deriv, second_deriv=second_deriv, x0=x0, eps=eps)
    ds.solve()

def anton_var():
    x0 = 2.4
    eps = 0.1
    func = Func(lambda x: x**3 - 2*x**2 + x - 1, "x^3 - 2*x^2 + x - 1")
    deriv = Func(lambda x: 3*x**2 - 4*x + 1, "3*x^2 - 4*x + 1")
    second_deriv = Func(lambda x: 6*x - 4, "6*x - 4")
    ds = NewtonMethod(func=func, first_deriv=deriv, second_deriv=second_deriv, x0=x0, eps=eps)
    ds.solve()

def vova_var():
    x0 = 3.6
    eps = 0.1
    func = Func(lambda x: x**3 - 2*x**2 + x - 1, "x^3 - 2*x^2 + x - 1")
    deriv = Func(lambda x: 3*x**2 - 4*x + 1, "3*x^2 - 4*x + 1")
    second_deriv = Func(lambda x: 6*x - 4, "6*x - 4")
    ds = NewtonMethod(func=func, first_deriv=deriv, second_deriv=second_deriv, x0=x0, eps=eps)
    ds.solve()


if __name__ == "__main__":
    albert_var()
    
     
        