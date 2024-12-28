from sympy.logic.boolalg import to_cnf

# Example expression: (A ∨ B) ∧ (¬C ∨ A)
expr = Or(A, B) & Or(Not(C), A)

# Convert to Conjunctive Normal Form
cnf_expr = to_cnf(expr, simplify=True)

print("Original Expression: ", expr)
print("Conjunctive Normal Form: ", cnf_expr)
