# 재귀함수

'''
문제 1. 수열 만들기 (#15649, #15650, #15651, # 15652, # 15654, # 15655, # 15656 )

자연수 N과 M이 주어졌을 때, 길이가 M인 수열을 모두 구하는 프로그램을 작성하세요.

1부터 N까지의 자연수 중에서 M개를 고른 수열
1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
1부터 N까지의 자연수 중에서 중복 없이 오름차순으로 M개를 고른 수열
1부터 N까지의 자연수 중에서 중복 없이 내림차순으로 M개를 고른 수열

4 3

1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
'''
# def recur_1(number,output):
#   if number==M:
#     print(output)
#     return
#   for i in range(1, N+1):
#     recur1(number+1, output+str(i)+" ")
    



def recur(i):
  if i == m:
    print(*arr)
    return
  for j in range(1,n+1):
    if visited[j]:
      continue
    visited[j]=1
    arr.append(j) # 추가하고 
    recur(i+1) # 반복 후
    arr.pop() # 다시 삭제해줘야 함 
    visited[j]=0

arr=[]
n, m = list(map(int, input().split()))
visited= [0 for _ in range(n+1)]

recur(0)