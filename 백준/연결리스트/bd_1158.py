#요세푸스 문제

# n,m = map(int, input().split())

# arr=[]

# arr = [i for i in range(1,n+1)]
# # for i in range(n):
# #   arr.append(i+1)

# result=[]
# point=0 #제거될 사람 인덱스 번호


# for i in range(n):
#   point+=m-1
#   if(point>= len(arr)):
#       point= point%len(arr)
#   result.append(arr.pop(point))

# print("<",", ".join(map(str,result)),">",sep='')    
  

from collections import deque
n,m = map(int, input().split())
D= deque()
result=[]

for i in range(1,n+1):
  D.append(i)

while len(D)>0:
  for j in range(1,k):
    D.append(D.popleft())
  result.append(str(D.popleft()))

print("<{}>".format(','.join(result)))