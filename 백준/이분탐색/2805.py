'''
나무자르기
푼 날짜: 25.09.16

적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
'''
n,m = map(int,input().split()) # 나무의 수 n, m미터
trees=list(map(int,input().split()))

trees.sort()

# 트리 내에 최소값과 최댓값 사이에서 나무를 베어보며 높이와 비교하기
max_h=0
s,e= 0, trees[-1]
while(True):
  tmp_sum=0
  if(s>e):
    break
  h= (s+e)//2
  for k in trees:
    if(k>h):
      tmp_sum+=k-h
  
  # 나무베기 만족
  if(tmp_sum>=m):
    max_h= max(h,max_h)
    s=h+1
  else:
    e=h-1

print(max_h)
