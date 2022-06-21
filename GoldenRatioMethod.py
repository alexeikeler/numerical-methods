from utils import *

class GoldenRationMethod:
    def __init__(self, func, a, b, l):
        self.func = func
        self.a, self.b = (a, b) if a < b else (b, a)
        self.l = abs(l)

        self.gold_left = 0.382
        self.gold_right = 0.618

        self.eps_char = '\u03B5'
        self.lambda_char = '\u03BB'
        self.mu_char = '\u03BC'

    def solve(self):
        print("=======================")
        print("Метод золотого перетину")
        print("=======================\n")

        lamb = self.a + self.gold_left * (self.b - self.a)
        mu = self.a + self.gold_right * (self.b - self.a)

        print(f"l = {self.l} > 0;")
        print(f"[a1 = {self.a}; b1 = {self.b}];")
        print(f"{self.lambda_char}1 = a1 + {self.gold_left} * (b1 - a1) = {self.a} + {self.gold_left * (self.b - self.a):.4f} = {lamb}")
        print(f"{self.mu_char}1 = a1 + {self.gold_right} * (b1 - a1) = {self.a} + {self.gold_right * (self.b - self.a):.4f} = {mu}")
        print(f"k = 1;\n")

        curr_a, curr_b = self.a, self.b
        i = 0
        while True:
            i += 1
            print(f"Iteration {i}: ")
            

            if (curr_b - curr_a) <= self.l:
                print(f"b{i} - a{i} <= l;")
                print(f"{curr_b:.4f} - ({curr_a:.4f}) = {curr_b - curr_a:.4f} < {self.l};")
                print()
                break
            
            print(f"b{i} - a{i} > l;")
            print(f"{curr_b:.4f} - ({curr_a:.4f}) = {curr_b - curr_a:.4f} > {self.l};")
            print()

            f_lamb = self.func.eval(lamb)
            f_mu = self.func.eval(mu)

            if f_lamb > f_mu:
                print(f"f({self.lambda_char}{i}) > f({self.mu_char}{i}), then: ")

                curr_a = lamb
                print(f"a{i+1} = {self.lambda_char}{i} = {lamb:.4f}")
                print(f"b{i+1} = b{i} = {curr_b:.4f}")

                lamb = mu
                print(f"{self.lambda_char}{i+1} = {self.mu_char}{i} = {mu:.4f}")

                mu = curr_a + self.gold_right * (curr_b - curr_a)
                print(f"{self.mu_char}{i+1}" + 
                        f" = a{i+1} + {self.gold_right} * (b{i+1} - a{i+1})" +
                        f" = {curr_a:.4f} + {self.gold_right} * ({curr_b:.4f} - ({curr_a:.4f}))" +
                        f" = {curr_a:.4f} + {self.gold_right * (curr_b - curr_a):.4f}" +
                        f" = {mu:.4f}")
            else:
                print(f"f({self.lambda_char}{i}) < f({self.mu_char}{i}), then: ")

                curr_b = mu
                print(f"a{i+1} = a{i} = {curr_a:.4f}")
                print(f"b{i+1} = {self.mu_char}{i} = {mu:.4f}")

                mu = lamb
                print(f"{self.mu_char}{i+1} = {self.lambda_char}{i} = {lamb:.4f}")

                lamb = curr_a + self.gold_left * (curr_b - curr_a)
                print(f"{self.lambda_char}{i+1}" + 
                        f" = a{i+1} + {self.gold_left} * (b{i+1} - a{i+1})" +
                        f" = {curr_a:.4f} + {self.gold_left} * ({curr_b:.4f} - ({curr_a:.4f}))" +
                        f" = {curr_a:.4f} + {self.gold_left * (curr_b - curr_a):.4f}" +
                        f" = {lamb:.4f}")

            f_lamb = self.func.eval(lamb)
            f_mu = self.func.eval(mu)
            print(f"f({self.lambda_char}{i+1}) = {str(self.func).replace('x', f'{lamb:.4f}')} = {f_lamb:.4f}")
            print(f"f({self.mu_char}{i+1}) = {str(self.func).replace('x', f'{mu:.4f}')} = {f_mu:.4f}")

            print(f"k={i+1}")
            print("\n")


        res = (curr_a + curr_b) * 0.5
        print("Resutls: ")
        print(f"x* = {res:.4f}")
        print(f"f(x*) = {self.func.eval(res):.4f}")

        return res


def albert_var():
    a, b = -3, -0
    l = 0.5
    func = Func(lambda x: (x + 1)**2, "(x + 1)^2")
    ds = GoldenRationMethod(func=func, a=a, b=b, l=l)
    ds.solve()

def anton_var():
    a, b = -9, -6
    l = 0.5
    func = Func(lambda x: (x + 7)**2, "(x + 7)^2")
    ds = GoldenRationMethod(func=func, a=a, b=b, l=l)
    ds.solve()

def vova_var():
    a, b = -21, -18
    l = 0.5
    func = Func(lambda x: (x + 19)**2, "(x + 19)^2")
    ds = GoldenRationMethod(func=func, a=a, b=b, l=l)
    ds.solve()


if __name__ == "__main__":

    albert_var()
