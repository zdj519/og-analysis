#!/bin/bash
# Last edited by BZ 16:25 BST 15 July 2020

IFS=","
while read NAME SCORE SMILES SA
do
   if [[ $SA -lt 4 ]]
   then
      FILENAME="${NAME}.pdbqt"
      obabel -:"${SMILES}" -O ${FILENAME} -p 7.4 --gen3d --partialcharge gasteiger
   fi
done