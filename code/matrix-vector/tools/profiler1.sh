#!/bin/bash


time sh tools/threads.sh > build/dump1
echo 

python tools/analyser1.py