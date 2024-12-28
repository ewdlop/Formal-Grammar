from sympy import symbols, sqrt, expand

# Define the symbol
d = symbols('d')
alpha = sqrt(d)

# Define the element in the number field
x = symbols('x')
element = x + alpha

# Compute the norm of the element
# For a quadratic field, the norm of (a + b*sqrt(d)) is (a + b*sqrt(d))(a - b*sqrt(d)) = a^2 - b^2*d
a, b = symbols('a b')
element = a + b * alpha
conjugate_element = a - b * alpha

# Norm is the product of the element and its conjugate
norm = expand(element * conjugate_element)

print(f"The norm of the element {element} is: {norm}")
