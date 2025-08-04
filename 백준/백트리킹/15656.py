# N과 M(7)

# 같은 수를 여러번 골라도 된다.
# 수열은 사전 순 증가 , 
n,m = map(int, input().split())
arr= list(map(int,input().split()))


# 배열 정렬 하기
# 중복 포함 개수만큼 픽하기 (모든 경우의 수 )

arr.sort()

count=m
tmp=[]
def dfs(start):
  if len(tmp)==m:
    print(*tmp)
    return
  for i in range(start, len(arr)):
    tmp.append(arr[i])  # 요소 별로 하나씩 들어가겠지, 
    dfs(0) # 다음 요소도 처음부터 다 봐야함. 
    tmp.pop() # 포문 돌 때 두개 들어가면 안되니까..

dfs(0)