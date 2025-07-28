
# arr[st:mid] 와 arr[mid:en]은 정렬 상태인데 이때 둘을 합친다.
# st부터 en-1까지 합치기
def merge(st, en):
  mid= (st+en)//2
  temp=[]
  # arr1 인덱스 초기값은 st
  # arr2 인덱스 초기값은 mid
  
  lidx, ridx= st,mid
  #lidx를 기준으로, lidx값이 ridx값보다 작으면 tmp에 계속 넣는다.
  #ridx값이 더 작으면 ridx를+1한다
  while(lidx<mid or ridx<en):
    if(lidx==mid):
      temp.append(arr[ridx])
      ridx+=1
    elif(ridx==en):
      temp.append(arr[lidx])
      lidx+=1
    elif(arr[lidx]> arr[ridx]):
      temp.append(arr[ridx])
      ridx+=1
    elif(arr[lidx]<= arr[ridx]):
      temp.append(arr[lidx])
      lidx+=1
  
  # arr에 정렬된 temp를 덮어쓴다
  arr[st:en]= temp

# arr[st:en] 정렬
def merge_sort(st,en):
  if(st==en-1): return
  mid=(st+en)//2
  
  merge_sort(st,mid)
  merge_sort(mid,en)
  merge(st,en)

n= int(input())
arr= list(map(int,input().split()))
merge_sort(0,n)
print(arr)

