
#N과 M(6)
#중복없이 / 사전 순 / M개의 수를 가진 모든 경우의 수
n,m = map(int,(input().split()))
arr=list(map(int,input().split()))

arr.sort()

co=[]
def curr(start): 
  if(len(co)==m):
    print(*co)
    return
  else:
    for k in range(start, len(arr)):
      co.append(arr[k])
      curr(k+1)
      co.pop()

curr(0) # 인덱스의 값이 포함된 모든 조합  
