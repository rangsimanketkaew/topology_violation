# tv_counting
tv_counting is a python program designed to compute the number of chain crossing between polymer. This code is designed to work with the coarse-graining simulation. It means that, **as long as you have a typical cartesian (XYZ) coordinate of a bead/particle of polymer chain, you can use this code to compute the topology violation events.** Additionally, tv_counting can be flexibly employed on interfacing with the general trajectory files since those are printed out by simulation using the general molecular dynamics simulation programs such as Gromacs, Amber, and LAMMPS.

---

# Coarse-Grained Modeling
Coarse-grained modeling (CG) is one of the mesoscale simulation technique that widely used in the computational chemistry and biology. A simple concept of CG is reducing the degree of freedom in calculation by grouping the atoms or fragment of molecule as an **united atom** (so called *bead*). CG also yeild the level of resolution of simulation at larger time and scale. More details of definition of CG can be found at (https://en.wikipedia.org/wiki/Coarse-grained_modeling). This model is a promising technique that many computational chemists has waited. It is very fast more than molecular dynamics (MD) simulation, whereas provides the accurate results and reasonably compared to experiments.

# Topology Violation in Polymer Simulation
The topology violation (TV) is the event that occurs during coarse-grained simulation of soft matter such as polymer. One can determine TV by counting the number of chain crossing between polymer. The TV is a primary parameter for evaluating the coarse-grained simulation technique such as **Dissipative Particle Dynamics** (DPD). There is several research in use of DPD simulation for modelling the polymer composite based on bead-bead spring interaction instead of atomistic model.

# Application in DPD simulation
Simulating the polymer to be consistent with the real physical properties of polymer is very important. One of the problematic issue is topology violation, which generally uccurs during simulation. [Goujon *et al.*](https://aip.scitation.org/doi/10.1063/1.2954022) studied topology violation and develop the technique to reduces number of polymer chain crossing event. [Sirk *et al.*](http://dx.doi.org/10.1063/1.3698476) reported the modified Segmental Repulsive Potential (mSRP) used with DPD simulation, DPD/mSRP. They also evaluate the performance of mSRP and reported the optimized parameter. [Ketkaew and Tantirungrotechai](http://onlinelibrary.wiley.com/doi/10.1002/mats.201700093/abstract) used the DPD and DPD/mSRP simulations to study the polyisoprene (natural rubber) entanglement. I personally suggest the LAMMPS manual for more practical details of [DPD simulation](http://lammps.sandia.gov/doc/pair_dpd.html) and [mSRP technique](http://lammps.sandia.gov/doc/pair_srp.html).

---

# Usage
## tv_counting
I strongly prefer to use tv_count.py source code instead of running tv_count.exe (executable file) becuase sometimes it has a problem with map function in python. You are encouraged to know the concept of topology violation, which will help you to quickly understand tv_counting clearly. </br>
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

## Utility

#### **remov_nLine** 
remov_nLine bash script can be used to prepare the XYZ coordinate file for tv_counting. It will create the file called *step#.txt* from the raw output file of molecular simulation. Again, remove_nLine can generate and adjust the format of coordinate of bead in simulated system to be cartesian (XYZ) coordinate at the same time. 
* **/utility/remove_nLine**
```
./remove_nLine.sh
```

#### tv_script.sh
This shell script is used to run the tv_counting.py and arrange the output from analysis. Both scripts should be carefully used. You can also learn the proper format of XYZ coordinate file by seeing [the test files](https://github.com/rangsimanketkaew/tv_counting/tree/master/test) in this repository.
* **/utility/tv_script.sh**
```
./tv_script.sh
```

---

# Motivation of Project
2016 Thailand Computational Chemistry Challenge by UBE. ([see details](https://sites.google.com/site/compchem403/event-news/compchem403-ceremony-tccc-ube-paccon2016))
 
# Contact info
Please send your question or comment or suggestion to me by rangsiman1993(at)gmail.com or visit https://nuttvichakarn.wordpress.com/ and https://sites.google.com/site/compchem403/home
