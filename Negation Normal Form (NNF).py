from sympy.logic.boolalg import Not, And, Or
from sympy.abc import A, B, C

# Example expression: ¬(A ∧ B) ∨ (¬C ∧ A)
expr = Or(Not(And(A, B)), And(Not(C), A))

# Convert to Negation Normal Form
nnf_expr = expr.to_nnf()

print("Original Expression: ", expr)
print("Negation Normal Form: ", nnf_expr)
