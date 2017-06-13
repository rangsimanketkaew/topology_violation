## Topology Violation Analysis for Polymer: Python code for calculating the number of polymer chian crossing.
## V. 1.1, 17 Oct 2016: Creat project, collecting XYZ coordinate & Calculate Dot product.
## V. 1.2, 19 Dec 2016: Updated usage & User friendly interfaced.
## V. 1.3, 23 Feb 2017: Speed up computation, combining two-code.
## V. 2.1, 14 May 2017: Import necessary function, make it fast more & more

import numpy as np
import math
import time
import datetime

print ("							\n\
!           ==================================== 		\n\
!           | The Topology Violation Analysis  | 		\n\
!           ==================================== 		\n\
! 								\n\
! <> Written by Rangsiman Ketkaew 				\n\
!    Student in Computational Chemistry 			\n\
!    Computational Chemistry Research Unit (CCRU)               \n\
!    Department of Chemistry, Faculty of Science and Technology \n\
!    Thammasat University, Pathum Thani, Thailand               \n\
! 							        \n\
! <> E-mail : rangsiman1993@gmail.com			        \n\
!    Website: https://sites.google.com/site/compchem403/	\n\
!")

N=5 # Number of file start from step0.txt, step1.txt, ...
B=200 # Number of bead of polymer in simulation system

#print ("! Number of file that include coordinate of bead in XYZ format")
#N = int(input("! Enter Number of File: "))
#print ("! Number of bead in your simulation system")
#B = int(input("! Enter Number of Bead: "))

## You can (must) change N and B to satify your computation (integer number)
## The name of coor file need to be in format of "step*.txt", where * refers to the number of
## successive file starts from 0, 1, 2, 3, ... till the last file.
        # The general format of coor file contains 5 columns
        # The example file can be found at /example/
        # 0th column is number of bead/molecule
        # 1st column is the number of polymer chain
        # 2nd column is the coor of particle on X axis
        # 3rd column is the coor of particle on Y axis
        # 4th column is the coor of particle on Z axis
        # 5th column is empty

# ---------------------------------------------------------------------------------------------- #

print ("! Calculating the number of polymer chain crossing from your files ...")

def findDist(x,y):
    delta = np.subtract(x,y)
    temp = [delta[0]*delta[0], delta[1]*delta[1], delta[2]*delta[2]]
    dist = math.sqrt((temp[0] + temp[1] + temp[2]))

    return dist

numFile = 0

while numFile < N :

    fileName = "step"+str(numFile)+".txt"  # string of filename
    f = open(fileName,'r')

    vector_list = []

    for line in f :
        v = line.split()
        values = map(float,v[2:5])  # extract only the coordinate in xyz from column 2nd-5th
        vector_list.append(values)

    # This line finished to read and store data to list.
    f.close()

    fileName = "step"+str(numFile)+"_output.txt"
    g = open(fileName,'w')
    #g2 = open("output2.txt",'w') # no save

    vector_raw = vector_list[0:B] ## vector_list[x:y] is bead no. x --> no. y
    # if you need to use all of data in a file, you can use vector_list to run this code.

    i = 0

    while i < len(vector_raw)-1 :
        j = i + 1
        while j < len(vector_raw) :
            dist = findDist(vector_raw[i], vector_raw[j])

            if dist <= 0.8 : ## 1.0 = global cut-off <-- You can flexibly change the distance of cutoff.
                ## case one distance <= 1.0
                a = np.subtract(vector_raw[j],vector_raw[i])
                result = "%d -> %d , %f %f %f \n" % (i, j, a[0], a[1], a[2])

                g.write(result)

            #elif dist > 0.8 :
                ## case two distance > 1.0
                #a = np.subtract(vector_raw[j],vector_raw[i])
                #result = "%d -> %d , %f %f %f \n" % (i, j, a[0], a[1], a[2])

                #g2.write(result)

            j += 1
        i += 1
        
    g.close()

    # update numFile (number of file data)
    numFile += 1

## Second job, dot product of two vectors and finding alpha (in degree unit)

def findDist(v):
    v = [v[0]*v[0], v[1]*v[1], v[2]*v[2]]
    dist = math.sqrt((v[0] + v[1] + v[2]))
    return dist

numFile = 1

sum_count = []
c = open("count.txt",'w')

while numFile < N :

    fileName1 = "step"+str(numFile-1)+"_output.txt"
    fileName2 = "step"+str(numFile)+"_output.txt"

    f1 = open(fileName1,'r')
    f2 = open(fileName2,'r')

    vect_1 = []
    vect_2 = []

    for line in f1 :
        values = line.split(',')
        vect_1.append(values)

    for line in f2 :
        values = line.split(',')
        vect_2.append(values)

    i = 0
    count = 0

    while i < len(vect_1) : # size of vector
        j = 0
        while j < len(vect_2) :
            if vect_1[i][0] == vect_2[j][0] :

                v1 = vect_1[i][1].split()
                v1 = map(float, v1[0:3])
                #print v1
                dist_v1 = findDist(v1)

                v2 = vect_2[j][1].split()
                v2 = map(float, v2[0:3])
                #print v2
                dist_v2 = findDist(v2)

                result = np.dot(v1,v2)
                #print result,dist_v1,dist_v2

                res = math.acos((result)/(dist_v1*dist_v2))
                deg = res*(float(180)/math.pi)
                #print deg

                if deg >= 90 :
                    count += 1
                
            j += 1
        i += 1

    sum_count.append(count) # add number of event to sum_count list

    #print "Number of Event = " "%s" % count

    numFile += 1 # update numFile (number of file data)

    c.write("Number of Event = " "%s \n" % count)

total = sum(sum_count)
c.write("Total of Event = " "%s \n" % total)

print ("")
print ("! ..... Total of Event = " "%s" " ....." % total)
print ("! Normally Terminated on:"), datetime.datetime.now()
