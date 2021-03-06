import ENDF6
import matplotlib.pyplot as plt
import numpy as np
def Read_Two_Column_File(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        start = 0 
        for i,line in enumerate(data):
         if i==0:
          t = line.split()
          start = float(t[0])
         elif i>1:
          p = line.split()
          x.append(float(p[0]))
          y.append(float(p[1]))
    return start,x, y


#f = open('g_4-Be-9_0425.endf')
_, x, y =Read_Two_Column_File('data/output/inel24_50')
#f = open('g_39-Y-89_3925.endf')

fig=plt.figure()
ax = fig.add_subplot(111)
#ax.set_yscale('log')
ax.plot(x, y)
ax.set_xlabel('Photon energy [MeV]')
ax.set_ylabel('Cross-section [barn]')
plt.show()
