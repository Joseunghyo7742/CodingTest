'''
프린터 큐
푼 날짜: 25.09.08

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
그렇지 않다면 바로 인쇄를 한다

문서가 몇 번째로 인쇄되었는지
4 2 
1 2 3 4

a,b,c,d 

6 0
1 1 9 1 1 1
a b c d e f

c d e f a b


'''
from collections import deque

t = int(input())

for _ in range(t):
    q = deque()
    cnt = 0  # 몇 번째로 인쇄되었는지 카운트
    n, m = map(int, input().split())  # 문서 개수, 타깃 문서 인덱스
    value = list(map(int, input().split()))
    q = deque((i, p) for i, p in enumerate(value))  # (원래 인덱스, 중요도)

    while True:
        # 현재 큐에서 가장 큰 중요도
        # (변수 추가 없이 매번 계산: n<=100이라 성능 충분)
        max_pri = max(p for _, p in q)

        # 맨 앞 문서가 최대 중요도면 인쇄
        if q[0][1] == max_pri:
            idx, _ = q.popleft()
            cnt += 1
            if idx == m:        # 타깃 문서면 종료
                print(cnt)
                break
        else:
            # 더 큰 중요도가 뒤에 있으므로 한 칸 회전
            q.rotate(-1)
