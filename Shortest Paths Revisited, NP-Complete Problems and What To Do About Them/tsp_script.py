import numpy as np
from itertools import combinations 
import copy
import pprint as pp
def dist(d1,d2):
  return ((d1[0]-d2[0])**2 + (d1[1]-d2[1]) **2)**0.5

filename ='tsp.txt'
header=False
v=0
coords={}
for f in open(filename):
  if not header:
    n=int(f)
    header=True
  else:
    f=f.replace('\n','').split(" ")
    coords[v]=[float(f[0]),float(f[1])]
    v=v+1

dist_matrix=np.zeros([v,v])
for i in coords.keys():
  for j in coords.keys():
    dist_matrix[i,j]=dist(coords[i],coords[j])
coords=dist_matrix



  # coords=[[0,1,15,6],[2,0,7,3],[9,6,0,12],[10,4,8,0]]
coords=np.array(coords)
s=0
n=len(coords[0])
A=np.zeros([n,n]).tolist()
for i in range(n):
  for j in range(n):
    A[i][j]={}
for i in range(n):
  if i==s:
    A[s][s]['_']=0
  else: 
    A[i][0]['_']=coords[s][i]
for i in range(1,n-1):
  file1 = open("tsp_out.txt","w") 
  L=[str(i)+' nodes processed']
  file1.writelines(L)
  file1.close()
  # print(i,"length route complete")
  nodes=list(range(n))
  nodes.remove(s)
  combs=combinations(nodes,i)
  combs=[list(i) for i in combs]
  for comb in combs:
    for j in nodes:
      if j not in comb:
        if len(comb)<2:
          A[j][i]['_'+str(comb[0])+'_']=float(A[comb[0]][i-1]['_']+coords[comb[0],j])
        else:
          val=np.inf
          for x in range(len(comb)):
            residual=copy.deepcopy(comb)
            y=residual.pop(x)
            key='_'
            keys=[]
            for k in residual:
              key=key+str(k)+'_'
              keys=keys+[k]
            if val>float(A[y][i-1][key]+coords[y,j]):
              val=float(A[y][i-1][key]+coords[y,j])
              key_final=key
              keys_final=keys
              y_final=y
          key=keys_final+[y_final]
          key.sort()
          # print(key)
          emp='_'
          for k in key:
            emp=emp+str(k)+'_'
          # A[j][i]['_'+str(y_final)+key_final]=val
          A[j][i][emp]=val

# for i in range(len(A)):
#   print(A[i])


dist=np.inf
for i in range(n):
  if A[i][n-2]!={} and i!=s:
    for j in A[i][n-2].keys():
      if dist>(A[i][n-2][j])+coords[i][s]:
        dist=(A[i][n-2][j])+coords[i][s]



print("The shortest path is:",dist)

file1 = open("tsp_out.txt","w") 
L=["The length of the TSP tour:",str(dist)]
file1.writelines(L)
file1.close()