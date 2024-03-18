#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <immintrin.h>

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
    // srand(time(NULL));
    for (int i = 0; i < MATRIX_SIZE; i++)
    {
        for (int j = 0; j < MATRIX_SIZE; j++)
            matrix[i][j] = (double)rand() / RAND_MAX;
        vector[i] = (double)rand() / RAND_MAX;
    }
}

// Perform matrix-vector multiplication
void matrix_vector_multiply()
{
    for (int i = 0; i <= MATRIX_SIZE - 9; i += 8)
    {
        __m256d sum = _mm256_setzero_pd();
        for (int j = 0; j < MATRIX_SIZE; j++)
        {
            __m256d a = _mm256_loadu_pd(&matrix[i][j]);
            __m256d b = _mm256_set1_pd(vector[j]);
            sum = _mm256_fmadd_pd(a, b, sum);
        }
        _mm256_storeu_pd(&result[i], sum);
    }

    for (int i = MATRIX_SIZE / 8 * 8; i < MATRIX_SIZE; i++)
    {
        double sum = 0;
        for (int j = 0; j < MATRIX_SIZE; j++)
            sum += matrix[i][j] * vector[j];
        result[i] = sum;
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
