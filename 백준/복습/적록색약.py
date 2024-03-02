import sys
sys.setrecursionlimit(10**6) #재귀호출 제한을 늘림
input= sys.stdin.readline

n= int(input())
palette=[]
for _ in range(n):
  palette.append(list(input().strip()))


check=[[0]*n for _ in range(n)]
d= [(0,-1),(0,1),(1,0),(-1,0)]

#dfs 제사용을 위해 방문 여부를 visited로 체크한다.
visited= 1 

def dfs(c,r,color):
  global check
  if check[c][r] == visited: #방문여부 확인 
    return
  check[c][r]=visited #방문 체크
  for dc, dr in d: #4방향 dfs탐색 
    new_c = c+ dc
    new_r= r+dr
    if(new_c<0 or new_c>=n or new_r<0 or new_r>=n):#범위가 같지않다면 스킵
      continue
    if(palette[new_c][new_r] not in color): #색상이 같지않다면 스킵
      continue
    dfs(new_c,new_r,color) 
  


result1=0 #적록색약 아닌 경우
result2=0 #적록색약인 경우

#적록색약 아닌 경우
for i in range(n):
  for j in range(n):
    if(check[i][j]!=visited):
      dfs(i,j,palette[i][j])
      result1+=1

#적록색약인 경우, 방문한 곳을 0으로 본다.
visited=0 
#적록색약인 경우 
for i in range(n):
  for j in range(n):
    if(check[i][j]!=visited):
      if palette[i][j]=="R" or palette[i][j]=="G":
        dfs(i,j,"RG")
      else:
        dfs(i,j,"B")
      result2+=1
print(result1, result2)

