import sys
input=sys.stdin.readline

n= int(input())
arr=[]

for i in range(n):
  arr.append(int(input()))
  
# 합병 정렬 이용하기
def merge_sort(st,en):
  #temp 배열 내에 정렬된 배열
  temp=[]
  mid= (st+en)//2
  li,ri= st,mid
  
  while(li<mid or ri<en):
    if(li==mid):
      temp.append(arr[ri])
      ri+=1
    elif(ri==en):
      temp.append(arr[li])
      li+=1
    elif(arr[li]> arr[ri]):
      temp.append(arr[ri])
      ri+=1
    elif(arr[li]<=arr[ri]):
      temp.append(arr[li])
      li+=1

  arr[st:en]= temp
  #기존 배열에 정렬된 temp 덮어쓰기
  

# st부터 en-1까지 두 배열로 나눔, 그리고 합쳐나가기
def merge(st, en):
  # 배열 길이가 1이면 그만
  if(st==en-1):
    return
  # 중앙 인덱스 필요
  mid= (st+en)//2
  # 왼쪽
  merge(st,mid)
  # 오른쪽
  merge(mid,en)
  # 합치기
  merge_sort(st,en)

merge(0,n)
for i in arr:
  print(i)