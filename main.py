import numpy as np
from numpy import linalg


class Eigen:
    def __init__(self, matrix):
        self.matrix = matrix
        self.value_1 = None
        self.value_2 = None
        self.vector_1 = None
        self.vector_2 = None

    def eigenValue(self):
        # The coefficients of the det(A-λ*I) polynomial
        a = 1
        b = -self.matrix[0][0] - self.matrix[1][1]
        c = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        # Using the quadratic formula: λ = (-b ± √(b^2 - 4ac)) / 2a
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            # Complex eigenvalues
            real_part = -b / (2 * a)
            imaginary_part = (abs(discriminant)**0.5) / (2 * a)
            value_1 = complex(real_part, imaginary_part)
            value_2 = complex(real_part, -imaginary_part)
        else:
            # Real eigenvalues
            value_1 = float((-b + discriminant**0.5) / (2 * a))
            value_2 = float((-b - discriminant**0.5) / (2 * a))

        self.value_1 = value_1
        self.value_2 = value_2
        return value_1, value_2

    def eigenVector(self):
        # Ensure eigenvalues are computed first
        if self.value_1 is None or self.value_2 is None:
            self.eigenValue()

        eigenvectors = []

        if np.allclose(self.matrix, 0):  # Check for zero matrix
            # For zero matrix, return arbitrary linearly independent vectors
            eigenvectors = [np.array([1, 0]), np.array([0, 1])]
        else:
            for eigenvalue in (self.value_1, self.value_2):
                # Solve (A - λI)v = 0
                modified_matrix = self.matrix - eigenvalue * np.eye(2)

                # Handle singular matrix cases
                try:
                    if abs(modified_matrix[0][0]) > abs(modified_matrix[1][0]):
                        x = 1
                        y = -modified_matrix[0][1] / modified_matrix[0][0]
                    else:
                        y = 1
                        x = -modified_matrix[1][0] / modified_matrix[1][1]
                    vector = np.array([x, y])
                except ZeroDivisionError:
                    vector = np.array([1, 0])  # Default to an arbitrary vector

                eigenvectors.append(vector)

        self.vector_1, self.vector_2 = eigenvectors
        return eigenvectors


# Example matrices
matrices = {
    "A": np.array([[1, 6], [5, 2]]),
    "B": np.array([[2, 3], [3, -6]]),
    "C": np.array([[7, 2], [-4, 1]]),
    "X": np.array([[1, 1], [-1, 1]]),
    "Z": np.array([[0, 0], [0, 0]])
}

# Compute and print eigenvalues and eigenvectors
for name, matrix in matrices.items():
    print(f"Matrix {name}:")
    eigen = Eigen(matrix)
    try:
        eigenvalues = eigen.eigenValue()
        eigenvectors = eigen.eigenVector()
        print(f"  Eigenvalues: {eigenvalues}")
        print(f"  Eigenvector 1: {eigenvectors[0]}")
        print(f"  Eigenvector 2: {eigenvectors[1]}")
    except Exception as e:
        print(f"  Error: {e}")
    print()
