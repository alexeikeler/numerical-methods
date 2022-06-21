# numerical-methods


<details>
           <summary>Bolzano method</summary>
           You should specify:
           <b>a<b/>: real number
             <b>b<b/>: real number
           <b>eps<b/>: real number
             <b>func</b>: Func class instance, with lambda function and it's string representation
             <b>deriv</b>: Func class instance, with lambda function and it's string representation
             <br/>
             
             Example:
             ```
             def anton_var():
    a, b = -9, -6
    eps = 0.3
    func = Func(lambda x: (x + 7)**2, "(x + 7)^2")
    deriv = Func(lambda x: 2 * x + 14, "2*x + 14")
    ds = BolzanoMethod(func=func, deriv=deriv, a=a, b=b, eps=eps)
    ds.solve()
             ```
</details>
