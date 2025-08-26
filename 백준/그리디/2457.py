import sys
input = sys.stdin.readline

n = int(input())  # 꽃의 총 개수
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    s = sm * 100 + sd              # 시작 mmdd
    e = em * 100 + ed              # 끝   mmdd 
    flowers.append((s, e))

S, E = 301, 1130                   # 3/01 ~ 11/30을 mmdd로

# 1) 의미 없는 꽃 제거
#    - 끝이 S(3/1)보다 작거나 같으면 시작 전에 끝남 → 제외 (e > S 필요)
#    - 시작이 E(11/30)보다 늦으면 커버 범위 밖 → 제외 (s <= E 필요)
filtered = [(s, e) for (s, e) in flowers if e > S and s <= E]

# 2) 정렬: 시작 오름차순, 시작 같으면 끝 내림차순
#    같은 날 피기 시작하는 꽃 중 "가장 멀리 가는" 게 먼저 오게 함
filtered.sort(key=lambda x: (x[0], -x[1]))

cur = S            # 현재까지 연속으로 덮은 마지막 날짜 (초기: 3/01)
idx = 0            # 스캔 인덱스
cnt = 0            # 선택한 꽃 수
n2 = len(filtered) # ← 필터와 정렬 이후에 길이 계산

# 3) 그리디:
#    'cur' 이하에서 시작하는 모든 후보 중 끝이 가장 먼 것을 선택하여 cur을 전진
while cur <= E:
    furthest = cur

    # 현재 cur 이하에서 시작하는 모든 꽃을 보며 가장 멀리 가는 끝을 갱신
    while idx < n2 and filtered[idx][0] <= cur:
        furthest = max(furthest, filtered[idx][1])
        idx += 1

    # 한 칸도 못 전진하면, 중간에 구멍이 생긴 것 → 불가능
    if furthest == cur:
        print(0)
        break

    # 하나 선택 (가장 멀리 가는 꽃)
    cnt += 1
    cur = furthest

    # 목표 종료일을 넘겼으면 성공적으로 덮은 것
    if cur > E:
        print(cnt)
        break
