# numerical-methods


<details>
           <summary>Bolzano method</summary>
           <br/>
           You should specify:
           <ul>
           <li>
           <b>a</b>: real number
           </li>
           <li>
             <b>b</b>: real number
             </li>
             <li>
           <b>eps</b>: real number
           </li>
           <li>
             <b>func</b>: Func class instance, with lambda function and it's string representation
             </li>
             <li>
             <b>deriv</b>: Func class instance, with lambda function and it's string representation
             </li>
             </ul>
             <br/>
             
https://github.com/alexeikeler/numerical-methods/blob/661d7b3da09461fcbf4bbe50daefd2b8b220d24e/BolzanoMethod.py#L71-L77

</details>



<details>
           <summary>Dichotomizing search</summary>
           <br/>
           You should specify:
           <ul>
           <li>
           <b>a</b>: real number
           </li>
           <li>
             <b>b</b>: real number
             </li>
             <li>
           <b>l</b>: real number
           </li>
           <li>
             <b>func</b>: Func class instance, with lambda function and it's string representation
             </li>
             </ul>
             <br/>
             
             
```python
def anton_var():
    a, b = -9, -6
    eps = 0.1
    l = 0.5
    func = Func(lambda x: (x + 7)**2, "(x + 7)^2")
    ds = DichotomizingSearch(func=func, a=a, b=b, eps=eps, l=l)
    ds.solve()
```
</details>


<details>
           <summary>Golden ration method</summary>
           <br/>
           You should specify:
           <ul>
           <li>
           <b>a</b>: real number
           </li>
           <li>
             <b>b</b>: real number
             </li>
             <li>
           <b>l</b>: real number
           </li>
           <li>
             <b>func</b>: Func class instance, with lambda function and it's string representation
             </li>
             </ul>
             <br/>
             
             
```python
def anton_var():
    a, b = -9, -6
    l = 0.5
    func = Func(lambda x: (x + 7)**2, "(x + 7)^2")
    ds = GoldenRationMethod(func=func, a=a, b=b, l=l)
    ds.solve()
```
</details>



<details>
           <summary>Newton method</summary>
           <br/>
           You should specify:
           <ul>
           <li>
           <b>x0</b>: real number
           </li>
           <b>eps</b>: real number
           </li>
           <li>
             <b>func</b>: Func class instance, with lambda function and it's string representation
             </li>
             <li>
             <b>deriv</b>: Func class instance, with lambda function and it's string representation
             </li>
                          <li>
             <b>second deriv</b>: Func class instance, with lambda function and it's string representation
             </li>
             </ul>
             <br/>
             
             
```python
def anton_var():
    x0 = 2.4
    eps = 0.1
    func = Func(lambda x: x**3 - 2*x**2 + x - 1, "x^3 - 2*x^2 + x - 1")
    deriv = Func(lambda x: 3*x**2 - 4*x + 1, "3*x^2 - 4*x + 1")
    second_deriv = Func(lambda x: 6*x - 4, "6*x - 4")
    ds = NewtonMethod(func=func, first_deriv=deriv, second_deriv=second_deriv, x0=x0, eps=eps)
    ds.solve()
```
</details>