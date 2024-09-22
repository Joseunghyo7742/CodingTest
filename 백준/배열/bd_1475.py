import math
n= input()

n_set= [0]*10
for i in n:
  i=int(i)
  if(i==6 or i==9):
    n_set[9]+=1
  else: n_set[i]+=1
  
max_value= max(n_set)
max_idx=n_set.index(max_value)

if(max_idx)==9:
  max_value= math.ceil(max_value/2)

print(max_value)
