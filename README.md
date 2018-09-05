## tv_counting
tv_counting, written in python 2.7, is a program for computing the number of chain crossing between polymer chains - topology violation of polymeric system - in multi-scale simulation. tv_counting can be used as a post-analysis with molecular dynamics program such as Gromacs, Amber, and LAMMPS.

## Coarse-Grained Modeling
Coarse-grained (CG) modelling is one of the meso-scale simulation technique that widely used in computational chemistry and biology. A concept of CG is reduction of the degree of freedom in simulated system by replacing atoms in molecule by a chunk called **bead**. CG modelling yeilds the resolution of simulation at larger time and scale. More details of CG modelling can be found at (https://en.wikipedia.org/wiki/Coarse-grained_modeling). This model is a promising technique that many computational chemists has waited. It can be said that CG is faster than a classical molecular dynamics (MD) simulation, and still provides the accurate and reasonable results compared to experiments.

## Topology Violation in Polymer Simulation
The topology violation (TV) is the event that occurs during coarse-grained simulation of soft matter such as polymer. One can determine TV by counting the number of chain crossing between polymer. The TV is a primary parameter for evaluating the coarse-grained simulation technique such as **Dissipative Particle Dynamics** (DPD). There is several research in use of CG/DPD simulation for modelling the polymer composite based on bead-bead spring interaction instead of atomistic model.

## Application to DPD simulation
Simulating the polymer to be consistent with the real physical properties of polymer is very important. One of the problematic issue is topology violation, which generally uccurs during simulation. [Goujon *et al.*](https://aip.scitation.org/doi/10.1063/1.2954022) studied topology violation and develop the technique to reduces number of polymer chain crossing event. [Sirk *et al.*](http://dx.doi.org/10.1063/1.3698476) reported the modified Segmental Repulsive Potential (mSRP) used with DPD simulation, DPD/mSRP. They also evaluate the performance of mSRP and reported the optimized parameter. [Ketkaew and Tantirungrotechai](http://onlinelibrary.wiley.com/doi/10.1002/mats.201700093/abstract) used the DPD and DPD/mSRP simulations to study the polyisoprene (natural rubber) entanglement. I personally suggest the LAMMPS manual for more practical details of [DPD simulation](http://lammps.sandia.gov/doc/pair_dpd.html) and [mSRP technique](http://lammps.sandia.gov/doc/pair_srp.html).

## Normal Usage
#### tv_count.py and tv_count.exe
I strongly prefer to use tv_count.py source code rather than tv_count.exe becuase the latter sometimes has a problem with map function in python. You are also expected to understand the concept of coarse-grained modelling and topology violation in polymer simulation before using tv_counting code. </br>

**Execute program using python interpreter** </br>
Source code is available at
```
/src/tv_count.py
```

- Serial run
```
python tv_count.py
```
- Parallel run
```
mpirun -np N python tv_count.py
```
where N = number of CPUs

**Execute program using compiled file**
```
./tv_count.exe
```

## Utilities

#### **remov_nLine.sh** 
remov_nLine bash script is used to create a suitable XYZ coordinate file for tv_counting program. It will create the file called *step#.txt* from the raw output or trajectory file printed by molecular dynamics program you use. You can see a example of a suitable XYZ coordinate by with this [test files](https://github.com/rangsimanketkaew/tv_counting/tree/master/test).

* **/utility/remove_nLine**
```
./remove_nLine.sh
```

#### tv_script.sh
tv_script.sh is used to run tv_counting.py and save the analysis output. Use this script to help you to manage tv_counting calculation when you have a ton of coordinate input files.

* **/utility/tv_script.sh**
```
./tv_script.sh
```

## Motivation of Project
- 2016 Thailand Computational Chemistry Challenge by UBE. 
- https://sites.google.com/site/compchem403/event-news/compchem403-ceremony-tccc-ube-paccon2016
 
## Author
- Rangsiman Ketkaew, Thammasat University, Thailand.
- If having question or comment, send to me via rangsiman1993@gmail.com or rangsiman_k@sci.tu.ac.th
- https://sites.google.com/site/rangsiman1993/ and https://sites.google.com/site/compchem403/
