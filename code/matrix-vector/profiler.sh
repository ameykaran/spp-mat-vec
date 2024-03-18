#!/bin/bash

make clean
mkdir -p build
make all
echo
sh ./run.sh > ./build/dump
echo 
python analyser.py > ./build/output
python gen_report.py
