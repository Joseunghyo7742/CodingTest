from collections import deque
##숨바꼭질3
# 걷기- 1초, X-1 OR -+1
# 순간이동- 0초, 2*X
# 동생을 찾을 가장 빠른 시간
#n,k <= 100,000
n,k= list(map(int, input().split())) 
visited=[0]*k 


def bfs(k,visited):
  q= deque()
  q.append()