n,m=map(int,input().split())
card=[]
#행렬 입력받기, 내림차순 정렬
for _ in range(n):
  arr= list(map(int,input().split()))
  arr.sort()
  card.append(arr)
#가장 높은 숫자 뽑기
max=0
for i in range(n):
  if(card[i][0]>max):
    max=card[i][0]
print(max)