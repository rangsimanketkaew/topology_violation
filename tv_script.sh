#!/bin/bash

#cd .

#test & example
#nohup mpirun -np 4 python 1.py &
#wait
#nohup mpirun -np 4 python 2.py &

#echo "Job done"

#-----------------------------------------#

cd .
nohup mpirun -np 4 python tv_count.py &
wait
mv -f ./*output.txt ./output
wait
mv -f ./count.txt ./count

#You can change number of processor from 4 to N (N=positive integer)
#-----------------------------------------#

echo "Job done"

