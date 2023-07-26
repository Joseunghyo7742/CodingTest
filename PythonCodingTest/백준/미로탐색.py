from collections import deque

n, m = map(int, input().split())

# 맵 입력받기
grid = []
for i in range(n):
    grid.append(list(map(int, input())))
#일렬로 입력받은 숫자를 list로 하나하나 요소로 넣음
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어났거나 벽인 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m: #범위에 맞는지 확인
                continue
            if grid[nx][ny] == 0: #벽인 경우
                continue
            if grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))
    return grid[n-1][m-1]  # 가장 오른쪽 아래까지의 최단 거리 반환

print(bfs(0, 0))
