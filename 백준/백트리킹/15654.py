# N과 M(5)
n,m= map(int,input().split())
arr= list(map(int,input().split()))

arr.sort()

# 1 7 8 9 m개 선택한  중복없는 조합
combi=[]
def curr(idx):
  if(len(combi)==m):
    print(*combi)
    return
  else:
    for i in range(idx,len(arr)):
      if(arr[i] not in combi):
        combi.append(arr[i])
        curr(idx)
        combi.pop()

curr(0)