all: matvec_vanilla matvec_opt1 matvec_opt2 matvec_opt3 matvec_vec matvec_omp matvec_omp_vec

matvec_vanilla:
	gcc -O0 mat-vec.c -o mat-vec0

matvec_opt1:
	gcc -O1 mat-vec.c -o mat-vec1

matvec_opt2:
	gcc -O2 mat-vec.c -o mat-vec2

matvec_opt3:
	gcc -O3 mat-vec.c -o mat-vec3

matvec_vec:
	gcc -O3 -march=native -ftree-vectorize -funroll-loops -ffast-math -mavx2 -mfma mat-vec.c -o mat-vec-vec

matvec_omp:
	gcc -O3 -fopenmp mat-vec-omp.c -o mat-vec-omp

matvec_omp_vec:
	gcc -O3 -fopenmp -march=native -ftree-vectorize -funroll-loops -ffast-math -mavx2 -mfma mat-vec-omp.c -o mat-vec-omp-vec

clean:
	rm mat-vec0 mat-vec1 mat-vec2 mat-vec3 mat-vec-vec mat-vec-omp mat-vec-omp-vec dump
	