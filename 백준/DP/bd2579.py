# 계단오르기
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 6
# 10
# 20
# 15
# 25
# 10
# 20

#75

#d[i][j] 현재 i까지 j개연속해 밟음 
n= int(input())
stairs=[]


for i in range(n):
  num= int(input())
  stairs.append(num)

d=[[stairs[0],0]]

for i in range(1,len(stairs)):
  
  #d[k][1]= d[k-1][1] or d[k-1][2] + 현재
  #d[k][2]= d[k-1][1] + 현재
  
  first=stairs[i]
  if(i>=2):
    max_value= max(d[i-2][0], d[i-2][1])+ stairs[i]
    first= max_value
  second= d[i-1][0]+ stairs[i]
  d.append([first,second])

print(max(d[-1][0],d[-1][1]))

  
  

  