# Last edited by BZ 16:20 BST 15 July 2020

# This script analyses OpenGrowth results in the form of Ligandsummary.txt, 
# tests the synthetic accessibility of the ligands, 
# converts and sends those that are <4.0 to ADV, and records the score.

import pandas as pd
import os
#from shutil import copyfile
import glob
from rdkit import Chem
from rdkit.Chem import RDConfig
import sys
sys.path.append(os.path.join(RDConfig.RDContribDir, 'SA_Score'))
import sascorer

roundname = 'r1'
bigfile = pd.DataFrame()

for pocketname in glob.glob('*/'):
    counter = 0
    pocket = pocketname.split('\\')[0]
    for i in range(1000):
        filename=f"{pocketname}Ligand_Summary_{i}.txt"
        if os.path.isfile(filename)==False:
            continue
        elif os.stat(filename).st_size==0:
            continue
        else:
            inp = pd.read_csv(filename,sep='\s+',usecols=[0,1,5,7])
            # ^ 0=name, 1=score, 5=3mer 7=smiles
            for lineno in range(len(inp.index)):
                inp.iloc[lineno,0] = f'{roundname}_{pocket}_{counter}'
                counter = counter + 1
            bigfile = pd.concat([bigfile,inp])

### Synthetic accessibility score
sa = []
for lig in range(len(bigfile.index)):
    ligtodraw = Chem.MolFromSmiles(bigfile.iloc[lig,3])
    try:
        sascore = round(sascorer.calculateScore(ligtodraw),1)
    except:
        sascore = 'N/A'
    sa.append(sascore)
bigfile['SA'] = sa
#bigfile.sort_values(by=['SA'],inplace=True,ascending=False)
bigfile.to_csv('Summary.csv',index=False)