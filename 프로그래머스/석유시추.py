# bfs로 석유 넓이를 파악
# 열이 얼마나 퍼져있는지가 중요함. -> bfs조사를 하면서 열 시작점과 끝점을 갱신하기
# oil[i] i는 열 -> 열 시작점부터 끝점까지 해당 넓이를 더해주기 
# 방문한 곳은 0으로 변경하기
    
from collections import deque
def solution(land):
    
    
    n= len(land)  #행길이
    m= len(land[0]) #열길이
    
    direct=[(0,1),(1,0),(-1,0),(0,-1)]
    oil=[0]*m # i 열에서 시추할 수 있는 오일량
    
    def bfs(r,c):
        q= deque()
        q.append([r,c])
        land[r][c]=0 # 방문처리
        
        min_c= c
        max_c= c
        width=1 
        while(q):
            r,c= q.popleft()
            for a,b in direct:
                n_r, n_c= r+a, c+b
                if(n_r<0 or n_r>=n or n_c<0 or n_c>=m):
                    continue
                if(land[n_r][n_c]==1):
                    min_c= min(min_c,n_c)
                    max_c= max(max_c,n_c)
                    land[n_r][n_c]=0  # 방문처리
                    width+=1 
                    q.append([n_r,n_c])
        
        for i in range(min_c, max_c+1):
            oil[i]+=width
        

    
    for i in range(n):
        for j in range(m):
            if(land[i][j]==1):
                bfs(i,j)
    print(oil)
    return max(oil)