import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readline

n= int(input())
palette=[]
for _ in range(n):
  palette.append(list(input().strip()))


check=[[0]*n for _ in range(n)]
d= [(0,-1),(0,1),(1,0),(-1,0)]
switch= 1 

def dfs(c,r,color):
  global check
  if check[c][r] == switch:
    return
  check[c][r]=switch
  for dc, dr in d:
    new_c = c+ dc
    new_r= r+dr
    if(new_c<0 or new_c>=n or new_r<0 or new_r>=n):
      continue
    if(palette[new_c][new_r] not in color):
      continue
    dfs(new_c,new_r,color)
  


result1=0
result2=0
#적록색약 x의 경우
for i in range(n):
  for j in range(n):
    if(check[i][j]!=switch):
      dfs(i,j,palette[i][j])
      result1+=1


switch=0
#적록색약인 경우 
for i in range(n):
  for j in range(n):
    if(check[i][j]!=switch):
      if palette[i][j]=="R" or palette[i][j]=="G":
        dfs(i,j,"RG")
      else:
        dfs(i,j,"B")
      result2+=1
print(result1, result2)

