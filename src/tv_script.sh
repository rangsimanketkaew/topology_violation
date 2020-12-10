#!/bin/bash

python3 tv.py
wait
mv -f *output.txt ./output # Pleae create /output/ folder beforeward
wait
mv -f count.txt ./count # Please create /count/ folder beforeward
echo "----Job done----"
