from IPython.core.display import display
from sympy.interactive import printing

printing.init_printing(use_latex=True)

import sympy as sp

x = sp.symbols("x")
f = sp.Function("O")(x)
diffeq = sp.Eq(f.diff(x, x) + 7 * f, 0)
display(diffeq)
display(sp.dsolve(diffeq, f))

