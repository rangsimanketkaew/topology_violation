# Coarse-graining model.
Coarse grained simulation (CG) is one of the mesoscale simulation technique. The concept of CG is trying to reduce the degree of freedom of particle by grouping the fragment of molecule as an united atom (called bead). That means the million atoms in system will become to the new particles which has the degree of freedom lower than the old one. I strongly suggest you to read the definition of CG if you are interested in (https://en.wikipedia.org/wiki/Coarse-grained_modeling). This model is a promising technique that many computational chemists has waited. It is very fast more than Molecular Dynamics simulation, whereas provides the accurate results and reasonably compared to experimental evidence.

# Topology Violation
The topology violation (TV) is the event that occurs during coarse-grained simulation of polymer. We can investigate the TV by counting the number of chain crossing between polymer. The TV is a primary parameter for evaluating the coarse-grained simulation technique such as Dissipative Particle Dynamics (DPD). There is several research about using DPD simulation to model the polymer based on bead-bead spring interaction. Of course, during energy minimization or equilibration, the chain of polymer and its neighbor can be normally crossed. To avoid this phenomenon, many polymer physicist are developing other model or correcting DPD for improving polymer representative.

# tv_counting
tv_counting is a python code used to compute the number of chain crossing between polymer. The code is designed to work with the coarse-graining simulation. It means that, **as long as you have the typical XYZ coordinate of bead of monomer in polymer chain, you can this code to analyse your polymer simulation.** Additionally, tv_counting can be flexibly employed on interfacing with the general trajectory files since those are printed out by molecular dynamics simulation programs such as Gromacs, Amber, and LAMMPS. 

# Utility
The other script is remov_nLine used for preparing the XYZ coordinate file (step#.txt) before using the tv_counting code. The remove_nLine bash script will generate and adjust the format of xyz coordinate at the same time. Both scripts should be carefully used. You can also learn the proper format of XYZ coordinate file by seeing the test files in this repository.

# Usage
### tv_counting
I strongly suggest you to use tv_count.py source code instead of running tv_count.exe becuase sometimes it has a problem with map function. By the way, before using my code, you are encouraged to know about the concept of topology violation first which will help you to quickly understand tv_counting clearly. </br>
* **/src/tv_count.py**

Serial run
```
python tv_count.py
```
Parallel run
```
mpirun -np N python tv_count.py
```
where N = number of CPUs

* **tv_count.exe**
```
./tv_count.exe
```

### Utility

* **/utility/remove_nLine**
```
./remove_nLine.sh
```

* **/utility/tv_script.sh**
```
./tv_script.sh
```

## Application
You can find the application of topology violation analysis in the research article of THE JOURNAL OF CHEMICAL PHYSICS136, 134903 (2012) published by Timothy W Sirk et al. [http://dx.doi.org/10.1063/1.3698476]. Moreover, I personally suggest you to read LAMMPS manual about Dissipative Particle Dynamics (DPD) model and Segmental Repulsive Potential (SRP), these are the well-known and widely used coarse grained simulation.

## Motivation of Project
2016 Thailand Computational Chemistry Challenge by UBE.

## Contact info
Please send your question or comment ot suggestion to me by rangsiman1993(at)gmail.com or visit https://nuttvichakarn.wordpress.com/ and https://sites.google.com/site/compchem403/home
