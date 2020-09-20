from scipy import sparse
from scipy.stats import uniform
import numpy as np
from scipy.sparse import coo_matrix

array1=[[0,0,0,1],
       [3,0,0,0],
       [4,0,0,0],
       [0,0,2,0]
      ]

i=[]
j=[]
k=[]

for q in range(len(array1)):
    for w in range(len(array1[0])):
        if array1[q][w]!=0:
            i.append(q)
            j.append(w)
            k.append(array1[q][w])

row  = np.array(i)
col  = np.array(j)
data = np.array(k)
t=coo_matrix((data, (row, col)))
print (coo_matrix.transpose(t))


output:
D:\python>python hello.py
  (3, 0)        1
  (0, 1)        3
  (0, 2)        4
  (2, 3)        2
