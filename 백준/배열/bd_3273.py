#투포인터 연산
n= int(input())
arr= list(map(int,input().split()))
x= int(input())

answer= 0
arr.sort() #오름차순 정렬
left=0
right= n-1

# 1 2 3 5 7 9 11
# 합이크면 left를 오른쪽으로 , 작다면 right를 -1하기 

while left< right:
  sum = arr[left]+ arr[right]
  if sum ==x:
    answer+=1
    left+=1
    right-=1
  elif sum>x:
    right-=1
  elif sum<x:
    left+=1

print(answer)