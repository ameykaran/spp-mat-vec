#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <omp.h>

#define MATRIX_SIZE 1028

double matrix[MATRIX_SIZE][MATRIX_SIZE];
double vector[MATRIX_SIZE];
double result[MATRIX_SIZE];

// Function to get current time in microseconds
long long current_time()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (long long)tv.tv_sec * 1000000LL + (long long)tv.tv_usec;
}

// Initialize matrix and vector with random values
void initialize()
{
    int i;
#pragma omp parallel private(i) shared(matrix, vector)
    {
#pragma omp for
        for (i = 0; i < MATRIX_SIZE; i++)
        {
            for (int j = 0; j < MATRIX_SIZE; j++)
                matrix[j][i] = (double)rand() / RAND_MAX;
            vector[i] = (double)rand() / RAND_MAX;
        }
    }
}

// Perform matrix-vector multiplication
void matrix_vector_multiply()
{
    int i, j;
#pragma omp parallel private(i) shared(matrix, vector) reduction(+ : result)
    {
#pragma omp for
        for (i = 0; i < MATRIX_SIZE; i++)
        {
            double res = 0;
            for (j = 0; j < MATRIX_SIZE; j++)
                res += matrix[i][j] * vector[j];
            result[i] = res;
        }
    }
}

int main()
{
    initialize();

    long long start_time = current_time();
    matrix_vector_multiply();
    long long end_time = current_time();
    double elapsed_time = (end_time - start_time) / 1000000.0; // Convert to seconds

    // Print time taken
    printf("Time taken: %f seconds\n", elapsed_time);

    // Calculate total floating point operations
    long long flops = 2 * MATRIX_SIZE * MATRIX_SIZE;

    // Calculate GFLOPS
    double gflops = flops / (elapsed_time * 1e9);
    printf("GFLOPS: %f\n", gflops);

    return 0;
}
