#!/bin/bash

cd .

#step1: rename the file from MD simulation to the general format of " step*.txt "
rename step_all_nvt_final_unwrap_2 step2 * 
wait

#step2: change file type to *.txt
rename 00.lammpstrj .txt *
wait
rename step2000 step *
wait 
rename step200 step *
wait
mv step20100.txt step100.txt
wait

#step3: delete an unnecessary line in the coor file
sed -i 1,+2348d step*.txt

echo ' --- Job done --- '
