# Eigenvalues and Eigenvectors Calculation

## Introduction
This program calculates the eigenvalues and eigenvectors of 2x2 matrices using a Python implementation. It supports both real and complex eigenvalues and handles edge cases like zero matrices. The code is implemented in a class structure, with the main class `Eigen` providing methods to compute the eigenvalues and eigenvectors.

---

## Algorithm Explanation

### Eigenvalue Calculation
The eigenvalues of a 2x2 matrix are calculated using the characteristic polynomial:
$\text{det}(A - \lambda I) = 0$

For a matrix $ A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} $:

1. The characteristic polynomial is:

   $
   \lambda^2 - (a+d)\lambda + (ad - bc) = 0
   $

2. The roots of this quadratic equation are given by:

   $
   \lambda = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   $

   - If the discriminant $(b^2 - 4ac)$ is non-negative, the eigenvalues are real.
   - If the discriminant is negative, the eigenvalues are complex and calculated as:
   
     $
     \lambda = \text{real\_part} \pm \text{imaginary\_part}\cdot i
     $

### Eigenvector Calculation
For each eigenvalue $\lambda$ :
1. Solve $(A - \lambda I)v = 0$ for the eigenvector $v$.
2. Handle singular matrices and ensure non-trivial solutions.
3. If the matrix is zero, return arbitrary linearly independent vectors as eigenvectors.

---

## Edge Cases
1. **Zero Matrix**:
   - For matrices like $Z = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$, eigenvalues are 0, and eigenvectors are arbitrarily chosen as $[1, 0]$ and $[0, 1]$.

2. **Complex Eigenvalues**:
   - Handled using Python's `complex` type, ensuring accurate computation for matrices like $ X = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} $.

3. **Singular Matrices**:
   - Safeguards against division by zero with fallback solutions.

---

## How to Deploy

### Prerequisites
- Python 3.6 or above
- NumPy library (pre-installed in most Python environments)

### Installation
1. Clone the repository or copy the code into a local file, e.g., `main.py`.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Define the matrices to be processed in the `matrices` dictionary.
2. Run the script:
   ```bash
   python main.py
   ```
3. The program will compute and print the eigenvalues and eigenvectors for each matrix.

### Output
For each matrix, the script prints:
- Eigenvalues
- Eigenvectors

Example Output:
```
Matrix A:
  Eigenvalues: (7.0, -4.0)
  Eigenvector 1: [1.  0.2]
  Eigenvector 2: [1.  0.8]

Matrix B:
  Eigenvalues: (3.0, -7.0)
  Eigenvector 1: [1.  0.333333]
  Eigenvector 2: [1.  -0.333333]

Matrix C:
  Eigenvalues: (5.0, 3.0)
  Eigenvector 1: [1. -1.]
  Eigenvector 2: [1. -2.]

Matrix X:
  Eigenvalues: (1+1j, 1-1j)
  Eigenvector 1: [1.+0.j 0.-1.j]
  Eigenvector 2: [1.+0.j 0.+1.j]

Matrix Z:
  Eigenvalues: (0.0, 0.0)
  Eigenvector 1: [1 0]
  Eigenvector 2: [0 1]
```

---

## Notes
- The implementation is limited to 2x2 matrices.
- Complex eigenvalues and eigenvectors are supported.
- The algorithm assumes the input is a valid square matrix.



