# 숫자카드2, 이진탐색으로 푼 경우

n= int(input()) #상근이가 가지고 있는 숫자카드 개수 1<= n <=500_000
cards= list(map(int,input().split())) #숫자 카드에 쓰인 수 -10_000_000 ~ 10_000_000
m= int(input())
cnt= list(map(int, input().split())) # 이 숫자들을 상근이가 몇개 가지고 있는지 

cards.sort()

def lower_index(target,len):
  st= 0
  en= len
  while(st<en):
    mid=(st+en)//2
    if(cards[mid]>= target):
      en= mid
    elif(cards[mid]<target):
      st= mid+1
  return st 

# target보다 최초로 큰 수가 나온 위치 구하기
def upper_index(target,len):
  st=0
  en= len
  while(st<en):
    mid=(st+en)//2
    if(cards[mid]>target):
      en= mid
    else: st= mid+1
  return st

result=[]
for x in cnt:
  upper= upper_index(x,n)
  lower= lower_index(x,n)
  result.append(upper-lower)

print(*result)