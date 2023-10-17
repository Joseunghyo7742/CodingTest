import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readline

n= int(input())
palette=[]
for _ in range(n):
  palette.append(list(input()))

print(palette)

check=[[0]*n for _ in range(n)]

d_c=[0,0,-1,1]
d_r=[-1,1,0,0]

count=0
def dfs(c,r,color):
  global count
  check[c][r]=1
  for i in range(4):
    new_c= c+ d_c[i]
    new_r= r+ d_r[i]
    if(new_c<0 or new_c>=n or new_r<0 or new_r>=n):
      continue
    if(color!= palette[new_c][new_r]):
      continue
    dfs(new_c,new_r,color)


for i in range(n):
  for j in range(n):
    if(check[i][j]==0):
      dfs(i,j,palette[i][j])
      count+=1
person=count
count=0

for i in range(n):
  for j in range(n):
    if(check[i][j]==1):
      if(palette[i][j]=="R" or "G"):
        dfs(i,j,"R" or "G")
      else:
        dfs(i,j,"B")
      count+=1
cow= count 

print("person",person)