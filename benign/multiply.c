#include <stdio.h>

void matrix_multiply(int* matrix1, int* matrix2, int* result) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            result[i * 2 + j] = 0;
            for (int k = 0; k < 2; k++) {
                result[i * 2 + j] += matrix1[i * 2 + k] * matrix2[k * 2 + j];
            }
        }
    }
}
void print_matrix(int* matrix) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", matrix[i * 2 + j]);
        }
        printf("\n");
    }
}
int main() {
    int matrix1[4] = {1, 2, 3, 4};
    int matrix2[4] = {5, 6, 7, 8};
    int result[4] = {0};
    matrix_multiply(matrix1, matrix2, result);
    printf("\nResult Matrix:\n");
    print_matrix(result);
    return 0;
}
