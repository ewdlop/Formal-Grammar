import numpy as np
from scipy.linalg import jordan_form

# Example matrix
A = np.array([[5, 4, 2, 1],
              [0, 1, 0, 0],
              [0, 0, 4, 3],
              [0, 0, 0, 1]])

# Compute Jordan normal form
J, P = jordan_form(A)

print("Jordan Normal Form:")
print(J)
print("Transformation Matrix:")
print(P)
