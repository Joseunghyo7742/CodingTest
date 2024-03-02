limit= 10000
dNList=[]

def dN (num):
  dn= num
  dn+=sum(map(int,str(num))) #각 자리 수 합
  if(dn in dNList or dn>limit):
    return 0
  else:
    dNList.append(dn)
    dN(dn)

for i in range(1,limit):
  dN(i)

for j in range(1,limit):
  if(j not in dNList):
    print(j)
