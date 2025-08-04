# 로또
# 입력: k, k개 수는 집합 S에 포함, S의 원소 오름차순
# 출력: 테케마다 수를 고르는 모든 방법 출력, 사전순/ 테케 사이에는 빈 줄을 하나 출력한다

# 6개 수열 경우의 수 
import sys
input= sys.stdin.readline




tmp=[]
def makeCombi(start):
  if(len(tmp)==6):
    print(*tmp)
    return
  else:
    for i in range(start, len(arr)):
      tmp.append(arr[i])
      makeCombi(i+1)
      tmp.pop()
  

while(1):
  line= list(map(int,input().split()))
  k= line[0]
  if(not k): break # k가 0이면 종료
  arr=line[1:]
  arr.sort()
  
  makeCombi(0)
  tmp=[]

  print('')


