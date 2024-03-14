for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec0  
    echo Finished O0
done

for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec1  
    echo Finished O1
done

for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec2  
    echo Finished O2
done

for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec3  
    echo Finished O3
done

for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec-vec  
    echo Finished Vec
done

for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec-omp  
    echo Finished OMP
done

for i in {1..25}; do
    echo "Running iteration $i"
    ./mat-vec-omp-vec  
    echo Finished OMP-Vec
done

echo "Done"
