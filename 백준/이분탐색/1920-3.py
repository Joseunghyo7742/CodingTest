'''
A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

4 1 5 2 3

1 2 3 4 5
s   m   e

1 3 7 9 5

'''

n= int(input())
arr=list(map(int,input().split()))
m= int(input())
arr2=list(map(int,input().split()))

arr.sort()

def binary_search(t):
  s,e= 0,n-1
  while(s<=e):
    m= (s+e)//2
    if(t>arr[m]):
      s=m+1
    elif(t<arr[m]):
      e=m-1
    else:
      print(1)
      return
  print(0)
  return
      
for i in arr2:
  binary_search(i)