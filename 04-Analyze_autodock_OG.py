# Last edited by BZ 17:24 BST 07/03/20

import glob
import pandas as pd
import os

inp = pd.read_csv('accessible.csv')
inp['ADV'] = ''
for jobdir in glob.glob('results/*/'):
   for logfile in glob.glob(f'{jobdir}*.txt'):
      if os.stat(logfile).st_size != 0:
          lignameext = os.path.basename(logfile)
          ligname = os.path.splitext(lignameext)[0]
          if ligname.split('_')[-1] != 'out':
              with open(logfile) as out:
                 content = [line.rstrip() for line in out]
                 emin = float(content[25].split()[1])
              inp.loc[inp['#LigandName'] == ligname,'ADV'] = emin
inp.to_csv('accessible_emin.csv')