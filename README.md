# tv_counting
tv_counting python script is a post-analysis tool for counting the number of event of polymer chain crossing (topology violation, TV) which have been simulated with the coarse-graining model. This tv_counting script can be flexibly employed on interface with the general trajectory or dump files those are printed out by general used MD programs such as Gromacs, Amber, LAMMPS programs. As long as you have the typical coordinate of polymer in xyz format, you could this script to analyse the topology violation.

# Coarse-graining model.
Coarse grained simulation (CG) is one of the mesoscale simulation technique. The concept of CG is trying to reduce the degree of freedom of particle by grouping the fragment of molecule as an united atom (called bead). That means the million atoms in system will become to the new particles which has the degree of freedom lower than the old one. I strongly suggest you to read the definition of CG if you are interested in (https://en.wikipedia.org/wiki/Coarse-grained_modeling). This model is a promising technique that many computational chemists has waited. It is very faster than Molecular Dynamics simulation, whereas provides the accurate results and reasonably compared to experimental evidence.

# remove_nLine
The remove_nLIne bash script is used to generate/adjust the format of xyz coordinate to suitably work with tv_count.py script afterward. Please be careful in using both of scripts, you can also learn what the proper format of coordinate by seeing test files in this repository.

## Application
You can find the application of topology violation analysis in the research article of THE JOURNAL OF CHEMICAL PHYSICS136, 134903 (2012) published by Timothy W Sirk et al. [http://dx.doi.org/10.1063/1.3698476]. Moreover, I personally suggest you to read LAMMPS manual about Dissipative Particle Dynamics (DPD) model and Segmental Repulsive Potential (SRP), these are the well-known and widely used coarse grained simulation.

## Motivation of Project
The motivation of this repository comes with the challenging in project of 2016 Thailand Computationl Chemistry Challenge by UBE.

## Contact info
ANy questions, comments, suggests, e-mail me by rangsiman1993(at)gmail.com or visit https://nuttvichakarn.wordpress.com/ and https://sites.google.com/site/compchem403/home
