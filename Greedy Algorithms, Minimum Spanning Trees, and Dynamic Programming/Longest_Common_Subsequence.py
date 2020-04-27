#!/usr/bin/env python
# coding: utf-8

# In[90]:


def lcs(A,B):
    m,n=len(A),len(B)
    opt=np.zeros((m+1,n+1))
    pi =np.zeros((m+1,n+1))
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1]==B[j-1]:
                opt[i,j]=opt[i-1,j-1]+1
                pi[i,j]=1
            else:
                if opt[i-1,j]>opt[i,j-1]:
                    opt[i,j]=opt[i-1,j]
                    pi[i,j]=2
                else:
                    opt[i,j]=opt[i,j-1]
                    pi[i,j]=3

    # recovering the sequence
    len_common_sequence=int(opt[m,n])
    common_sequence=''
    r,c=m,n
    while r!=0 and c!=0:
        if pi[r,c]==1:
            common_sequence=B[c-1]+common_sequence
            r-=1
            c-=1
        elif pi[r,c]==2:
            r-=1
        elif pi[r,c]==3:
            c-=1
    return(len_common_sequence,common_sequence)
        
    


# In[99]:


import numpy as np 
A=input()
B=input()
l,s=lcs(A,B)
print(l)
print(s)


# In[ ]:





# In[ ]:




