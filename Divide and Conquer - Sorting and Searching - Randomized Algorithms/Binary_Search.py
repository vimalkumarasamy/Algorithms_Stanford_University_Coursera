# recursion based
import math
A=[1,2,3,4,5,6,7,8,9,10]

def binary_search(A,l,r,n):
  # print(l,r)
  if r-l==1 and A[l]!=n and A[r]!=n:
    return False
  mid=math.ceil((l+r)/2)
  if A[mid]==n:
    return True
  elif A[mid]>n:
    status=binary_search(A,l,mid-1,n)
  else:
    status=binary_search(A,mid,r,n)
  return(status)

n=5.0
present=binary_search(A,0,len(A)-1,n)
print('Is',n,'present in',A,'?\n',present)



# iteration based
A=[1,2,3,4,5,6,7,8,9,10]
l=0
r=len(A)-1
n=11
decided=False

iter=math.ceil(math.log(n,2))
for i in range(iter):
    print(l,r)
    if decided:
        break
    if r-l<2 and A[l]!=n and A[r]!=n:
        decided=True
        found=False
        break
    mid=math.ceil((l+r)/2)
    if A[mid]==n:
        decided=True
        found=True
        break
    elif A[mid]>n:
        r=mid-1
    else:
        l=mid+1
   
print(found)