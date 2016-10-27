#!/bin/bash

cd .
nohup mpirun -np 4 python tv_count.py &
wait
mv -f *output.txt ./output
wait
mv -f count.txt ./count

echo " ---- Job done ---- "

