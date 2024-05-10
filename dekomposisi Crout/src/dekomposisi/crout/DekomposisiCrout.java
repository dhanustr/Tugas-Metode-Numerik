/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package dekomposisi.crout;

import java.util.Scanner;

/**
 *
 * @author Dhanu
 */
public class DekomposisiCrout {

        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan jumlah variabel: ");
        int n = scanner.nextInt();

        double[][] A = new double[n][n];
        double[] B = new double[n];

        System.out.println("Masukkan koefisien matriks A:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("A[" + (i+1) + "][" + (j+1) + "]: ");
                A[i][j] = scanner.nextDouble();
            }
        }

        System.out.println("Masukkan vektor hasil B:");
        for (int i = 0; i < n; i++) {
            System.out.print("B[" + (i+1) + "]: ");
            B[i] = scanner.nextDouble();
        }

        double[][] L = new double[n][n];
        double[][] U = new double[n][n];

        // Proses dekomposisi Crout
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                double sum = 0;
                for (int k = 0; k < i; k++) {
                    sum += L[i][k] * U[k][j];
                }
                if (i == j) {
                    U[i][j] = 1;
                } else {
                    U[i][j] = A[i][j] - sum;
                }
            }

            for (int j = i; j < n; j++) {
                double sum = 0;
                for (int k = 0; k < i; k++) {
                    sum += L[j][k] * U[k][i];
                }
                L[j][i] = (A[j][i] - sum) / U[i][i];
            }
        }

        // Solusi sistem persamaan linear
        double[] Y = new double[n];
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < i; j++) {
                sum += L[i][j] * Y[j];
            }
            Y[i] = (B[i] - sum) / L[i][i];
        }

        double[] X = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += U[i][j] * X[j];
            }
            X[i] = (Y[i] - sum) / U[i][i];
        }

        // Menampilkan solusi
        System.out.println("\nSolusi dari sistem persamaan linear:");
        for (int i = 0; i < n; i++) {
            System.out.println("X[" + (i+1) + "] = " + X[i]);
        }
    }
}


