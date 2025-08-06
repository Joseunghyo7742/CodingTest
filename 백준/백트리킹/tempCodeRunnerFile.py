# N과 M (8)
# 중복 ok
# 오름차순

n,m= map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
comb=[]
# start부터 만들 수 있는 조합을 만들어서 프린트
def combi(start):
  if(len(comb)==m):
    print(*comb)
    return
  else:
    for i in range(start, len(arr)):
      comb.append(arr[i])
      combi(i)
      combi.pop()

combi(0)
