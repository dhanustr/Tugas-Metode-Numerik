import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1

    for k in range(n):
        U[k, k:] = A[k, k:] - L[k, :k] @ U[:k, k:]
        L[k+1:, k] = (A[k+1:, k] - L[k+1:, :] @ U[:, k]) / U[k, k]

    return L, U

def solve_lu(A, b):
    L, U = lu_decomposition(A)
    n = len(A)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = b using forward substitution
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # Solve Ux = y using backward substitution
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x

# memasukan matrix A dan vector b
n = int(input("Masukkan ukuran dimensi matriks (n): "))
print("Masukkan matriks A (ukuran {}x{}) dan vektor b (ukuran {}).".format(n, n, n))
A = np.zeros((n, n))
b = np.zeros(n)
for i in range(n):
    row = list(map(float, input("Masukkan baris ke-{} dari matriks A: (pisahkan dengan spasi) ".format(i+1)).split()))
    A[i, :] = row
b = np.array(list(map(float, input("Masukkan vektor b: (pisahkan dengan spasi)").split())))

# Solve the system
x = solve_lu(A, b)
print("Solusi sistem persamaan linearnya adalah:")
print(x)
