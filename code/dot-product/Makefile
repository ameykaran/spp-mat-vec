MATH_FLAGS= -ffast-math 

all: dotp_vanilla dotp_opt1 dotp_opt2 dotp_opt3 dotp_vec dotp_omp dotp_omp_vec

dotp_vanilla: 
	gcc -O0 dotp_flops.c -o dotp_vanilla

dotp_opt1:
	gcc -O1 dotp_flops.c -o dotp_opt1

dotp_opt2:
	gcc -O2 dotp_flops.c -o dotp_opt2

dotp_opt3:
	gcc -O3 dotp_flops.c -o dotp_opt3 

dotp_vec:
	gcc -O3 ${MATH_FLAGS} -mtune=native -march=native -ftree-vectorize -funroll-loops -mavx2 -mfma dotp_flops.c -o dotp_vec

dotp_omp:
	gcc -O3 -fopenmp dotp_flops_omp.c -o dotp_omp 

dotp_omp_vec:
	gcc -O3 -fopenmp ${MATH_FLAGS} -mtune=native -march=native -ftree-vectorize -funroll-loops -mavx2 -mfma dotp_flops_omp.c -o dotp_omp_vec

clean:
	rm dotp_vanilla dotp_opt1 dotp_opt2 dotp_opt3 dotp_vec dotp_omp dotp_omp_vec dump
