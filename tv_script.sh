#!/bin/bash

cd .

# nohup mpirun -np N python tv_count.py &
# where N is the number of the processor for MPI (N = positive integer, says, N=4)

nohup mpirun -np 1 python tv_count.py &
wait
mv -f *output.txt ./output # Pleae create /output/ folder beforeward
wait
mv -f count.txt ./count # Please create /count/ folder beforeward

echo "----Job done----"
