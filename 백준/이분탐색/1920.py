
# 수찾기 내 방식
# st,en은 값이 있을 법한 범위
def two_point(st,en,t):
  # en<st이면 0출력, finish 조건
  if(en<st):
    print(0)
    return
  mid= (st+en)//2
  # mid보다 찾으려는 값이 작으면, en= mid-1, 
  if(t<arr[mid]):
    en= mid-1
  # mid보다 찾으려는 값이 크면, st= mid+1 , 
  if(t>arr[mid]):
    st= mid+1
    
  # mid와 값이 같다면 1출력 , finish 조건
  if(t==arr[mid]):
    print(1)
    return
  two_point(st,en,t)
  

n= int(input())
arr= list(map(int,input().split()))

m= int(input())
mrr= list(map(int,input().split()))

arr.sort()


for i in mrr:
  two_point(0,n-1,i)