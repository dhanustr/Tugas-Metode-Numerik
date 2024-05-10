import numpy as np

def input_vector(n):
    print("Masukkan elemen-elemen vektor (pisahkan dengan spasi):")
    vector = []
    for _ in range(n):
        element = float(input())
        vector.append(element)
    return np.array(vector)

def input_matrix():
    n_row = int(input("tentukan jumlah baris: "))
    n_col = int(input("tentukan jumlah kolom: "))
    print("Masukkan elemen-elemen matriks (pisahkan dengan spasi untuk pindah baris dan enter untuk pindah kolom):")
    matrix = []
    for _ in range(n_row):
        row = list(map(float, input().split()))
        if len(row) != n_col:
            print("Masukkan tepat %d angka untuk setiap baris" % n_col)
            return input_matrix()
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Masukkan matriks koefisien (A):")
    A = input_matrix()

    print("Masukkan vektor hasil (b):")
    b = input_vector(A.shape[0])  # Asumsi jumlah baris di matriks b sama dengan jumlah baris di matriks A

    try:
        A_inv = np.linalg.inv(A)
        x = np.dot(A_inv, b)
        print("Solusi sistem persamaan linearnya adalah:")
        print(x)
    except np.linalg.LinAlgError:
        print("Matriks koefisien tidak dapat diubah menjadi matriks balikan.")

if __name__ == "__main__":
    main()
