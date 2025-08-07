# 다른 사람 방식


def binary_search(target, data):
  start=0
  end= len(data)-1
  
  while(start<=end):
    mid= (start+end)//2
    if(data[mid]>target):
      end= mid-1
    elif data[mid] <target:
      start= mid+1
    elif data[mid]==target:
      return 1
  return 0

n= int(input())
arr= list(map(int,input().split()))

m= int(input())
mrr= list(map(int,input().split()))

arr.sort()

for x in mrr:
  if binary_search(x, arr):
    print(1)
  else:
    print(0)