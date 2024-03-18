#!/bin/bash

make clean
mkdir -p build
make all
echo
export OMP_NUM_THREADS=4
sh tools/run.sh > build/dump
echo 
python tools/analyser.py > build/output
python tools/gen_report.py
xdg-open report.md