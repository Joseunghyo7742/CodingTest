'''
퇴사 2 문제 

입력: n / ti,pi n일까지 순서대로
출력: 퇴사일 까지 상담으로 벌어들일 수 있는 최대이익


7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''


n= int(input())
iv= [list(map(int,input().split())) for _ in range(n)]

dp= [0] *(n+1)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값 유지

    ti, pi = iv[i - 1]  # i번째 상담의 소요 기간, 수익
    nd = i + ti - 1  # 상담이 끝나는 날

    if nd <= n:
        dp[nd] = max(dp[nd], dp[i - 1] + pi)  # 상담을 선택하는 경우