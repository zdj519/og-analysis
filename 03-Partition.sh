#!/bin/bash

# Last edited by BZ 12:34 BST 22 July 2020

i=0
f=0
PNAME="job_${f}"
mkdir ${PNAME}

for LIGNAME in *.pdbqt; do
   if [ ${i} -lt 100 ] 
   then
      mv ${LIGNAME} ${PNAME}/
      i=$(expr ${i} + 1)
   else
      i=0
      f=$(expr ${f} + 1)
      PNAME="job_${f}"
      mkdir ${PNAME}
   fi
done