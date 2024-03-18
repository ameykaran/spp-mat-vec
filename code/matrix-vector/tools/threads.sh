#!/bin/bash

for num in {1..50}; do
    export OMP_NUM_THREADS=$num
    echo OMP_NUM_THREADS=$OMP_NUM_THREADS
    for i in {1..10}; do
        ./build/mat-vec-simd-omp
    done
    echo
done
