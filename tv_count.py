## Polymer Structure Analysis Tool
## --> Coding Script for Counting The Number of Topology Violation, version 1.1 (Oct 2016, debugging)
## --> This script is improved interface for general user.
## --> The code is writen by Rangsiman Ketkaew, Computational Chemistry Research Unit, Thammasat U., Thailand
## --> Contact me for what you want to see in next project, rangsiman1993(at)gmail(dot)com

import numpy as np
import math

## You can (must) change N and B to satify your computation (integer number)
## The name of coor file need to be in format of " step*.txt ", where * is start from 0, 1, 2, and so on.
        # The general format of coor file is  contains 5 column # You can see the example coor file in folder /example/
        # 0th column is number of bead/molecule
        # 1st column is the number of polymer chain
        # 2nd column is the coor of particle on X axis
        # 3rd column is the coor of particle on Y axis
        # 4th column is the coor of particle on Z axis
        # 5th column is empty

N = 10 # Number of coor file ## <--- Need to check before submit
B = 2145 # Number of Bead/Molecule ## <--- Need to check before submit

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
        values = map(float,v[2:5])  # the position of X,Y,X coordinate # extract only the coor (xyz) in column 2nd-5th
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

print " ---- Wow, wait a minute ! ---- "

## Second job, dot product of two vectors and finding alpha (in degree unit)

import numpy as np
import math

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

print " Total of Event = " "%s" % total

print " ------ Normal termination ------ "

print " -------- See You Again --------- "

## The computation has done ##
