from sympy.logic.boolalg import to_dnf

# Example expression: (A ∧ B) ∨ (¬C ∧ A)
expr = And(A, B) | And(Not(C), A)

# Convert to Disjunctive Normal Form
dnf_expr = to_dnf(expr, simplify=True)

print("Original Expression: ", expr)
print("Disjunctive Normal Form: ", dnf_expr)
