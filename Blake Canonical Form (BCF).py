from sympy.logic.boolalg import And, Or, Not, Xor
from sympy.abc import A, B, C

# Example boolean function: A xor B and C
expr = Xor(A, And(B, C))

# Convert to Algebraic Normal Form (Zhegalkin Polynomial)
anf_expr = expr.simplify()

print("Original Expression: ", expr)
print("Algebraic Normal Form: ", anf_expr)
