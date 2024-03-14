all: o0 o1 o2 o3 vec omp omp_vec

o0:
	gcc -O0 mem_bw.c -o mem_o0	

o1:
	gcc -O1 mem_bw.c -o mem_o1

o2:
	gcc -O2 mem_bw.c -o mem_o2

o3:
	gcc -O3 mem_bw.c -o mem_o3

vec:
	gcc -O3 -march=native -ftree-vectorize -funroll-loops -ffast-math -mavx2 -mfma mem_bw.c -o mem_vec

omp:
	gcc -O3 -march=native -mtune=native -fopenmp mem_bw.c -o mem_omp

omp_vec:
	gcc -O3 -march=native -mtune=native -ftree-vectorize -funroll-loops -ffast-math -mavx2 -mfma mem_bw.c -o mem_omp_vec

clean:
	rm mem_o0 mem_o1 mem_o2 mem_o3 mem_vec mem_omp mem_omp_vec 