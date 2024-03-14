#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

#define MATRIX_SIZE 1000

double matrix[MATRIX_SIZE][MATRIX_SIZE];
double vector[MATRIX_SIZE];
double result[MATRIX_SIZE];

// Initialize matrix and vector with random values
void initialize()
{
    srand(time(NULL));
    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        for (int j = 0; j < MATRIX_SIZE; j++)
            matrix[j][i] = (double)rand() / RAND_MAX;
        vector[i] = (double)rand() / RAND_MAX;
    }
}

// // Perform matrix-vector multiplication
// void matrix_vector_multiply()
// {
//     int i, num_threads;
// #pragma omp parallel private(i) shared(matrix, vector) reduction(+ : result)
//     {
//         num_threads = omp_get_num_threads();
// #pragma omp parallel for private(i) shared(matrix, vector, result)
//         for (i = 0; i < MATRIX_SIZE; i++)
//         {
//             int res = 0, j, num_threads = omp_get_num_threads();
// #pragma omp parallel for private(j) shared(matrix, vector, result)
//             // #pragma omp parallel for reduction(+ : result[i]) private(i) shared(matrix, vector)
//             // #pragma omp parallel for reduction(+ : res) private(i) shared(matrix, vector)
//             {
//                 for (j = 0; j < MATRIX_SIZE; j++)
//                 {
//                     result[i] += matrix[i][j] * vector[j];
//                 }
//                 // res += matrix[i][j] * vector[j];
//             }
//             // result[i] = res;
//         }
//         // printf("Number of threads: %d\n", num_threads);
//     }
// }


// Perform matrix-vector multiplication
void matrix_vector_multiply() {
    int i, j;
    // int res;
    #pragma omp parallel for private(i, j) shared(matrix, vector, result) 
    for (i = 0; i < MATRIX_SIZE; i++) {
        for (j = 0; j < MATRIX_SIZE; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
        // result[i] = res;
    }
}


int main()
{
    initialize();

    clock_t start_time = clock();
    matrix_vector_multiply();
    clock_t end_time = clock();
    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    // Print time taken
    printf("Time taken: %f seconds\n", elapsed_time);

    // Calculate total floating point operations
    long long flops = 2 * MATRIX_SIZE * MATRIX_SIZE;

    // Calculate GFLOPS
    double gflops = flops / (elapsed_time * 1e9);
    printf("GFLOPS: %f\n", gflops);

    return 0;
}
