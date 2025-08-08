# 숫자카드2, 카운트 정렬로 푼 경우 
n= int(input()) #상근이가 가지고 있는 숫자카드 개수 1<= n <=500_000
cards= list(map(int,input().split())) #숫자 카드에 쓰인 수 -10_000_000 ~ 10_000_000
m= int(input())
cnt= list(map(int, input().split())) # 이 숫자들을 상근이가 몇개 가지고 있는지 

arr=[0]*20_000_001 # 인덱스는 카드 숫자, 값은 카드 장수


# 카드 카운트, 카드 수의 인덱스에 카운트하기
for x in cards:
    arr[x+10_000_000]+=1

result=[]
for y in cnt:
  result.append(arr[y+10_000_000])

print(*result)
