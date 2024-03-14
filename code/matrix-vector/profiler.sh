#!/bin/bash

make clean
make all

sh ./run.sh > dump
echo 
python analyser.py 
