from utils import *

class BolzanoMethod:
    def __init__(self, func, deriv, a, b, eps):
        self.func = func
        self.deriv = deriv
        self.a, self.b = (a, b) if a < b else (b, a)
        self.eps = abs(eps)

        self.eps_char = '\u03B5'
        self.lambda_char = '\u03BB'
        self.mu_char = '\u03BC'

    def solve(self):
        print("==============")
        print("Метод Больцано")
        print("==============\n")
        print(f"{self.eps_char} = {self.eps};")
        print(f"[a0 = {self.a}; b0 = {self.b}];")
        print(f"f(x) = {str(self.func)};")
        print(f"f'(x) = {str(self.deriv)};")
        print(f"k = 0;")
        print()

        curr_a, curr_b = self.a, self.b
        i = 0
        while True:
            i += 1
            print(f"Iteration {i}: ")
            c = (curr_a + curr_b) / 2   
            print(f"c{i} = (a{i} + b{i}) / 2 = ({curr_a:.4f} + ({curr_b:.4f})) / 2 = {c}")

            deriv_val = self.deriv.eval(c)
            if abs(deriv_val) <= self.eps:
                print(f"|f'(c{i})| = |{str(self.deriv).replace('x', f'{c:.4f}')}| = |{deriv_val}| = {abs(deriv_val)} <= {self.eps}")
                break

            print(f"|f'(c{i})| = |{str(self.deriv).replace('x', f'{c:.4f}')}| = |{deriv_val}| = {abs(deriv_val)} > {self.eps}")

            if self.deriv.eval(c) > 0:
                print(f"f'(c{i}) = {deriv_val} > 0")
                print(f"a{i+1} = a{i} = {curr_a}")
                print(f"b{i+1} = c{i} = {c}")
                curr_b = c
            else:
                print(f"f'(c{i}) = {deriv_val} < 0")
                print(f"a{i+1} = c{i} = {c}")
                print(f"b{i+1} = b{i} = {curr_b}")
                curr_a = c

            print(f"k = {i}")
            print()

        res = c
        print()
        print("Result: ")
        print(f"x* = {res}")
        print(f"f(x*) = {self.func.eval(res)}")

        return res


def albert_var():
    a, b = -3, 0
    eps = 0.3
    func = Func(lambda x: (x + 1)**2, "(x + 1)^2")
    deriv = Func(lambda x: 2 * x + 2, "2*x + 2")
    ds = BolzanoMethod(func=func, deriv=deriv, a=a, b=b, eps=eps)
    ds.solve()

def anton_var():
    a, b = -9, -6
    eps = 0.3
    func = Func(lambda x: (x + 7)**2, "(x + 7)^2")
    deriv = Func(lambda x: 2 * x + 14, "2*x + 14")
    ds = BolzanoMethod(func=func, deriv=deriv, a=a, b=b, eps=eps)
    ds.solve()

def vova_var():
    a, b = -21, -18
    eps = 0.3
    func = Func(lambda x: (x + 19)**2, "(x + 19)^2")
    deriv = Func(lambda x: 2 * x + 38, "2*x + 38")
    ds = BolzanoMethod(func=func, deriv=deriv, a=a, b=b, eps=eps)
    ds.solve()



if __name__ == "__main__":
    albert_var()
        
