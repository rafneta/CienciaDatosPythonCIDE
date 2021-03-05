# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.8.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import sympy



def taylor(f, x, x0,n):
  
    if n == 0:
        return f.subs(x, x0)
    else:
        return sympy.diff(f,x,n).subs(x,x0)/sympy.factorial(n) * (x - x0) ** n + taylor(f,x,x0,n-1)
    
    




