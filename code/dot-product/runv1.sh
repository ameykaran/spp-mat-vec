for i in {1..25}; do
    echo "Running iteration $i"
    ./dotp_vanilla
    ./dotp_opt1
    ./dotp_opt2
    ./dotp_opt3
    ./dotp_vec
    ./dotp_omp
    ./dotp_omp_vec
    echo 
      
    if (( $i % 5 == 0 )); then
        echo "Running iteration $i" 1>&2 
    fi
done