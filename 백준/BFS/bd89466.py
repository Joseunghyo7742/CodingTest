#플젝 팀원 수 제한 x. 끝과 마지막이 꼬리를 물 때 한 팀 가능
# 어느 플젝 팀에도 속하지 않는 학생 수


# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8

# 3
# 0
t= int(input())
#학생 수 n
for _ in range(t):
  n= int(input())
  arr= list(map(int,input().split())) #선택된 학생 수 
  