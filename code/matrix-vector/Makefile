all: matvec_vanilla matvec_opt1 matvec_opt2 matvec_opt3 matvec_vec matvec_omp matvec_omp_vec matvec_simd matvec_simd_vec matvec_simd_omp

vec_flags=-march=native -ftree-vectorize -funroll-loops -ffast-math -fopt-info-vec-optimized
omp_flags=-fopenmp
simd_flags=-mavx2 -mfma
general_flags=-O3 -m64


matvec_vanilla:
	gcc -g -O0 mat-vec.c -o build/mat-vec0

matvec_opt1:
	gcc -g -O1 mat-vec.c -o build/mat-vec1

matvec_opt2:
	gcc -g -O2 mat-vec.c -o build/mat-vec2

matvec_opt3:
	gcc $(general_flags) mat-vec.c -o build/mat-vec3

matvec_vec:
	gcc $(general_flags) $(vec_flags) mat-vec.c -o build/mat-vec-vec

matvec_omp:
	gcc $(general_flags) $(omp_flags) mat-vec-omp.c -o build/mat-vec-omp

matvec_omp_vec:
	gcc $(general_flags) $(vec_flags) $(omp_flags) mat-vec-omp.c -o build/mat-vec-omp-vec

matvec_simd:
	gcc $(general_flags) $(simd_flags) mat-vec-simd.c -o build/mat-vec-simd

matvec_simd_vec:
	gcc $(general_flags) $(simd_flags) $(vec_flags) mat-vec-simd.c -o build/mat-vec-simd-vec

matvec_simd_omp:
	gcc $(general_flags) $(simd_flags) $(omp_flags) mat-vec-simd-omp.c -o build/mat-vec-simd-omp

matvec_simd_omp_vec:
	gcc $(general_flags) $(simd_flags) $(omp_flags) $(vec_flags)  mat-vec-simd-omp.c -o build/mat-vec-simd-omp

clean:
	rm -r build 
	