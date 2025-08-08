# 좌표압축
# 중복을 제외하고 해당 수보다 작은 수의 개수

# 이분탐색으로 해당 수의 인덱스 구함 -> 인덱스= 좌표 압축 
def binary_search(target):
  st,en= 0, len(setDots)
  while(st<=en):
    mid= (st+en)//2
    if(setDots[mid]> target):
      en= mid-1
    elif(setDots[mid]<target):
      st=mid+1
    elif(setDots[mid]==target):
      result.append(mid)
      return
  return

n= int(input())
dots=list(map(int,input().split()))

# 정렬 후 중복제거
sortedDots= sorted(dots)
setDots=[sortedDots[0]]
for i in range(1,n):
  if(sortedDots[i] != setDots[-1]):
    setDots.append(sortedDots[i])

result=[]


for x in dots:
  binary_search(x)
  
print(*result)
# -2 5 -2  -4 3 3 3 
# 1 4 1 0 2 2 2

# -4 -2 -2 3 3 3 5


