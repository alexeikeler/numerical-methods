class Func:
    def __init__(self, func, func_str):
        self.func = func
        self.func_str = func_str

    def eval(self, *args):
        return self.func(*args)
    
    def __str__(self):
        return self.func_str