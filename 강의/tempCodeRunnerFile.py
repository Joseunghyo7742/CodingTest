# 19942
#요구사항: 식재료 n개 선택했을 때 탄단지비가 일정 이상이어야함
# 최소영양분은 만족하면서 비용은 최소화하는 재료로 짜기

# 입력: 식재료 수/ 단백질, 지방, 탄수화물, 비타민 순으로 최소 영양성분 기준/ n 줄 동안 식재료
# 출력: 첫째줄 최소비용, 최소 비용 식재료의 번호  // 없다면 -1


#예외처리: 최소비용은 같은데 더이상 재료가 필요없는 경우
# 최소영양분 기준을 통과하면 비용 검사를 해본다.
# 몇번째 재료인지 저장필요



def getCombi(k):
  getCost()
  
  for i in range(k,n):
    if i  not in combi:
      combi.append(i) #재료를 넣은 경우
      getCombi(i+1)
      combi.pop() #재료를 안넣은 경우

def getCost():
  global min_cost, min_combi
  p,f,c,v,cost=0,0,0,0,0
  
  for i in combi:
    p+=nutrients[i][0]
    f+=nutrients[i][1]
    c+=nutrients[i][2]
    v+=nutrients[i][3]
    cost+=nutrients[i][4]
    
  if(p>=mp and f>=mf and c>=mc and v>=mv and cost<min_cost):
    min_cost=cost
    min_combi= [a+1 for a in combi]

n= int(input())
mp, mf, mc, mv= map(int,input().split()) # 최소 영양기준
nutrients= [list(map(int,input().split())) for _  in range(n)] #식재료

combi=[] #재료 조합
min_cost= 1_000_000_000
min_combi= []

getCombi(0)

if min_cost == 1_000_000_000:
  print(-1)
else:
  print(min_cost)
  print(*min_combi)