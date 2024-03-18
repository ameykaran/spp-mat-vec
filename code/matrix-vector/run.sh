#!/bin/bash

for i in {1..25}; do
    ./build/mat-vec0  
    ./build/mat-vec1  
    ./build/mat-vec2  
    ./build/mat-vec3  
    ./build/mat-vec-vec  
    ./build/mat-vec-omp  
    ./build/mat-vec-omp-vec  
    ./build/mat-vec-simd  
    ./build/mat-vec-simd-vec
    ./build/mat-vec-simd-omp

    echo $i

    if (( $i % 5 == 0 )); then
        echo "Finished iteration $i" 1>&2
    fi
done

echo "Done"
