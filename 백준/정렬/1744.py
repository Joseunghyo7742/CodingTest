'''
수묶기
푼날짜: 25.09.03

묶으면 곱한 후에 더해야함 
수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램

- 높은 수 끼리 곱한다.
- 음수는 음수와 곱한다.
- 음수가 홀수개면 0이랑 곱해서 없앤다. 
'''

n = int(input())
pos, ones, zeros, neg = [], 0, 0, []

for _ in range(n):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zeros += 1
    else:
        neg.append(x)
        
# 양수(>1): 내림차순 큰 값끼리 곱
pos.sort(reverse=True)
# 음수: 오름차순(가장 작은 음수부터) 짝지어 곱
neg.sort()


result = 0

# 양수 페어 처리
i = 0
while i + 1 < len(pos):
    result += pos[i] * pos[i + 1]
    i += 2
# 남으면 더하기
if i < len(pos):
    result += pos[i]

# 1은 전부 더하기
result += ones

# 음수 페어 처리
j = 0
while j + 1 < len(neg):
    result += neg[j] * neg[j + 1]
    j += 2
# 홀수 개 남은 음수 처리
if j < len(neg):
    # 0이 있으면 상쇄(=아무 것도 더하지 않음)
    if zeros == 0:
        result += neg[j]

print(result)
