'''
경로찾기
푼 날짜: 25.08.12
복습필요
'''

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(u: int):
    # u에서 도달 가능한 정점들을 visited에 표시
    for v in range(n): # u에 연결된 정점 중 방문하지 않은 곳을 방문해보기 
        if graph[u][v] == 1 and not visited[v]: 
            visited[v] = 1        # 방문 표시를 1로
            dfs(v) # 그 정점에서 또 갈 수 있는 곳까지 닿아보기.

for s in range(n):
    visited = [0] * n             # 시작점마다 초기화
    dfs(s)          # s에서 갈 수 있는 모든 정점 탐색
    print(*visited)  