#!/bin/bash

for p in c*/; do
   cd ${p}
   for j in */; do
      mkdir -p "../sumtxt/${p}"&&cp ${j}*.txt ../sumtxt/${p}
   done
   cd ..
done