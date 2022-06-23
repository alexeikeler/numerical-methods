# numerical-methods
<details>
           <summary>Single variable optimization methods</summary>
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
             
https://github.com/alexeikeler/numerical-methods/blob/bb3184de1e268a8afd104d2f476d53b206279fe9/DichotomizingSearch.py#L91-L97
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
             
https://github.com/alexeikeler/numerical-methods/blob/bb3184de1e268a8afd104d2f476d53b206279fe9/GoldenRatioMethod.py#L107-L112
</details>



<details>
           <summary>Newton method</summary>
           <br/>
           You should specify:
           <ul>
           <li>
           <b>x0</b>: real number
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
                          <li>
             <b>second deriv</b>: Func class instance, with lambda function and it's string representation
             </li>
             </ul>
https://github.com/alexeikeler/numerical-methods/blob/bb3184de1e268a8afd104d2f476d53b206279fe9/NewtonMethod.py#L71-L78
</details>
           
</details>

<details>
           <summary>Multivariable optimization methods</summary>
           <details>
                      <summary> fxy_extrema.py - Programm for finding function extremum. </summary>
                      <br/>
                      You should specify:
                      <ul>
                      <li>
                      <b>n</b>: amount of variables
                      </li>
                      <li>
                      <b>f(x1, x2, ..., xn)</b>: function 
                      </li>
                      </ul>
           </details>

<details>
<summary> lagrange_opt.py - Programm for finding function extemum subject to constraints.</summary> 

  <br/>
  You should specify:
  <ul>
  <li>
  <b></b> Number of variables.
  </li>
  <li>
  <b>f(x1, x2, ..., xn)</b>: function 
  </li>
  <li>
  <b></b>Number of constraints. 
  </li>
  <li>
  <b>g1, g2, ..., gn</b>: Constraints. 
  </li>
  </ul>
<br/>
Example:
<ul>
    <li>
    Number of variables: 2
    </li>
    <li>
    f[x1, x2] = 6-4*x1-3*x2   
    </li>
    <li>
    Number of constraints: 1
    </li>
    <li>
    Constraint # 1: x1**2 + x2**2 - 1
    </li>
</ul>
  <b>!!!Important!!!</b>
  <li>
  Constraints must be written like the one in example above, i.e. NOT LIKE x1**2 + x2**2 = 1 but x1**2 + x2**2 - 1. 
  In other words you must move everything from left to right.
  </li>
</ul>


