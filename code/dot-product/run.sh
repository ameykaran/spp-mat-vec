# ./dotp_vanilla
# ./dotp_opt1
# ./dotp_opt2
# ./dotp_opt3
# ./dotp_vec
# ./dotp_omp
# ./dotp_omp_vec


for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_vanilla  
done
echo Finished O0 1>&2

for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_opt1  
done
echo Finished O1 1>&2

for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_opt2  
done
echo Finished O2 1>&2

for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_opt3  
done
echo Finished O3 1>&2

for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_vec  
done
echo Finished Vec 1>&2

for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_omp  
done
echo Finished OMP 1>&2

for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_omp_vec  
done
echo Finished OMP-Vec 1>&2

echo "Done"
