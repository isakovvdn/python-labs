import sympy as sp

x = sp.symbols('x')

f = x**2 + 3*x + 1

print("Производная:", sp.diff(f, x))
print("Интеграл:", sp.integrate(f, x))

print(sp.solve(x**2 - 4, x))