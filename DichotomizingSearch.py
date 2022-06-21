
from utils import *


class DichotomizingSearch:
    def __init__(self, func, a, b, eps, l):
        self.func = func
        self.a, self.b = (a, b) if a < b else (b, a)
        self.eps = abs(eps)
        self.l = abs(l)

        self.eps_char = '\u03B5'
        self.lambda_char = '\u03BB'
        self.mu_char = '\u03BC'

    def initialize(self):
        print("==================")
        print("Дихотомічний пошук")
        print("==================\n")

        print(f"l = {self.l} > 0;")
        print(f"{self.eps_char} = {self.eps} > 0;")
        print(f"[a1 = {self.a}; b1 = {self.b}];")
        print("k0 = 0;\n")   

    def solve(self):
        self.initialize()

        curr_a, curr_b = self.a, self.b 
        i = 0
        while True:
            i += 1
            print(f"Iteration {i}: ")

            c = (curr_a + curr_b) * 0.5 
            print(f"c{i} = (a{i} + b{i}) / 2")
            print(f"c{i} = {curr_a + curr_b:.4f} / 2 = {c:.4f}")
            print()

            if curr_b - curr_a <= self.l:
                break

            print(f"b{i} - a{i} > l;")
            print(f"{curr_b:.4f} - ({curr_a:.4f}) = {curr_b - curr_a:.4f} > {self.l}")
            print()

            lamb = c - self.eps
            mu = c + self.eps
            print(f"{self.lambda_char}{i} = (a{i} + b{i}) / 2 - {self.eps_char} = {c:.4f} - {self.eps} = {lamb:.4f}")
            print(f"{self.mu_char}{i} = (a{i} + b{i}) / 2 + {self.eps_char} = {c:.4f} + {self.eps} = {mu:.4f}")


            f_lamb = self.func.eval(lamb)
            f_mu = self.func.eval(mu)
            print(f"f({self.lambda_char}{i}) = {str(self.func).replace('x', f'{lamb:.2f}')} = {f_lamb:.4f}")
            print(f"f({self.mu_char}{i}) = {str(self.func).replace('x', f'{mu:.2f}')} = {f_mu:.4f}")

            if f_lamb > f_mu:
                curr_a = lamb
                print(f"f({self.lambda_char}{i}) > f({self.mu_char}{i}), then: ")
                print(f"a{i+1} = {self.lambda_char}{i} = {lamb:.4f}")
                print(f"b{i+1} = b{i} = {curr_b:.4f}")
            else:
                curr_b = mu
                print(f"f({self.lambda_char}{i}) < f({self.mu_char}{i}), then: ")
                print(f"a{i+1} = a{i} = {curr_a:.4f}")
                print(f"b{i+1} = {self.mu_char}{i} = {mu:.4f}")

            print(f"k{i} = k{i-1} + 1 = {i-1} + 1 = {i}")
            print()
            print()

        print(f"b{i} - a{i} < l; {curr_b:.4f} - ({curr_a:.4f}) = {curr_b - curr_a:.2f} < {self.l}")
        print(f"k{i} = k{i-1} + 1 = {i-1} + 1 = {i}")

        print()
        print("Result: ")
        print(f"x* = {c:.4f}")
        print(f"f(x*) = {self.func.eval(c):.4f}")
        return c


def albert_var():
    a, b = -3, -0
    eps = 0.1
    l = 0.5
    func = Func(lambda x: (x + 1)**2, "(x + 1)^2")
    ds = DichotomizingSearch(func=func, a=a, b=b, eps=eps, l=l)
    ds.solve()

def anton_var():
    a, b = -9, -6
    eps = 0.1
    l = 0.5
    func = Func(lambda x: (x + 7)**2, "(x + 7)^2")
    ds = DichotomizingSearch(func=func, a=a, b=b, eps=eps, l=l)
    ds.solve()

def vova_var():
    a, b = -21, -18
    eps = 0.1
    l = 0.5
    func = Func(lambda x: (x + 19)**2, "(x + 19)^2")
    ds = DichotomizingSearch(func=func, a=a, b=b, eps=eps, l=l)
    ds.solve()



if __name__ == "__main__":
    albert_var()

