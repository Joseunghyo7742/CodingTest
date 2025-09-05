from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# s[i][j] + s[j][i] 미리 합치기
pair = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        pair[i][j] = pair[j][i] = s[i][j] + s[j][i]

people = list(range(n))

def team_score(team):
    # team 내부의 모든 (i<j) 쌍 합
    total = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            total += pair[team[i]][team[j]]
    return total

'''
전체 인원: [0,1,2,3,4,5]

한 팀 크기: n//2 = 3

range(1,6) = [1,2,3,4,5]

여기서 2명(n//2 - 1 = 2) 뽑음

결과: (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)

여기에 (0,)을 붙여서 스타트팀 완성:
{0,1,2}, {0,1,3}, {0,1,4}, ... {0,4,5}
'''
# 대칭 제거: 0번을 반드시 포함하는 조합만 생성
answer = float('inf')
for comb in combinations(range(1, n), n//2 - 1):
    a = (0, ) + comb
    a_set = set(a)  # 여기서만 한 번 사용
    b = [x for x in people if x not in a_set]

    diff = abs(team_score(a) - team_score(b))
    if diff < answer:
        answer = diff

print(answer)
