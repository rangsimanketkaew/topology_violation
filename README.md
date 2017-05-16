# tv_counting
tv_counting is a python code that used to be a post-analysis tool for polymer simulation by counting the number of event of polymer chain crossing (topology violation or TV) which have been simulated with the coarse-graining model. The script can be flexibly employed on interface with the general trajectory or dump files those are printed out by several molecular dynamics simulation programs such as Gromacs, Amber, and LAMMPS programs. As long as you have the typical coordinate of polymer in XYZ format, you could this script to analyse your polymeric system.

# Coarse-graining model.
Coarse grained simulation (CG) is one of the mesoscale simulation technique. The concept of CG is trying to reduce the degree of freedom of particle by grouping the fragment of molecule as an united atom (called bead). That means the million atoms in system will become to the new particles which has the degree of freedom lower than the old one. I strongly suggest you to read the definition of CG if you are interested in (https://en.wikipedia.org/wiki/Coarse-grained_modeling). This model is a promising technique that many computational chemists has waited. It is very fast more than Molecular Dynamics simulation, whereas provides the accurate results and reasonably compared to experimental evidence.

# remove_nLine
The remove_nLIne bash script is used to generate/adjust the format of xyz coordinate to suitably work with tv_count.py script afterward. Please be careful in using both of scripts, you can also learn what the proper format of coordinate by seeing test files in this repository.

# Usage
I strongly suggest you to use tv_count.py source code instead of running tv_count.exe becuase sometimes it has a problem with map function. By the way, before using my code, you are encouraged to know about the concept of topology violation first which will help you to quickly understand tv_counting clearly. </br>
* **/src/tv_count.py:**

Serial run
```
python tv_count.py
```
Parallel run
```
mpirun -np N python tv_count.py
```
where N = number of CPUs

* **remove_nLine:**
```
./remove_nLine.sh
```

* **tv_count.exe**
```
./tv_count.exe
```

## Application
You can find the application of topology violation analysis in the research article of THE JOURNAL OF CHEMICAL PHYSICS136, 134903 (2012) published by Timothy W Sirk et al. [http://dx.doi.org/10.1063/1.3698476]. Moreover, I personally suggest you to read LAMMPS manual about Dissipative Particle Dynamics (DPD) model and Segmental Repulsive Potential (SRP), these are the well-known and widely used coarse grained simulation.

## Motivation of Project
2016 Thailand Computational Chemistry Challenge by UBE.

## Contact info
Please send your question or comment ot suggestion to me by rangsiman1993(at)gmail.com or visit https://nuttvichakarn.wordpress.com/ and https://sites.google.com/site/compchem403/home
