from collections import deque

dc = [(-1,0),(0,1),(1,0),(0,-1)]

# 입력받기
n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]  # ★ range(n)

# 1년 후 빙산 상태
def getNewBerg():
    new_ice = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                tmp = iceberg[i][j]
                # 바다 접면 수만큼 감소 (경계 체크 필수)
                for dr, dc_ in dc:
                    nr, nc = i + dr, j + dc_
                    if 0 <= nr < n and 0 <= nc < m and iceberg[nr][nc] == 0:
                        tmp -= 1
                new_ice[i][j] = max(0, tmp)
    return new_ice

# 덩어리 하나를 0으로 지우는 BFS (board는 복사본)
def countBerg(board, r, c):
    q = deque()
    q.append((r, c))
    board[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc_ in dc:
            nr, nc = r + dr, c + dc_
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 0:
                board[nr][nc] = 0
                q.append((nr, nc))

result = 0  # 걸린 시간(년)
while True:
    # 1년 경과 후 상태
    new_iceberg = getNewBerg()
    result += 1

    # 분리 개수는 복사본으로 계산 (원본 훼손 금지)
    tmp = [row[:] for row in new_iceberg]
    ice_cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] != 0:
                ice_cnt += 1
                countBerg(tmp, i, j)

    if ice_cnt >= 2:          # 두 덩어리 이상으로 분리됨
        break
    if ice_cnt == 0:          # 모두 녹아버림
        result = 0
        break

    iceberg = new_iceberg     # ★ 다음 해로 상태 갱신 (여기서 해야 함)

print(result)
