# 쉬운 계단수
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개
# 인접한 모든 자리의 차이가 1



n= int(input())

calcs=[
  [1,2,3,4,5,6,7,8,9],
  [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
]

# idx자릿수의 다음 자리 계단수 구하기
def getStairNum(idx):
  digit= 10**idx # 10
  n_stairs=[]
  
  for num in calcs[idx]:
    units= num%digit # num의 일의자리 저장.
    
    new_num= digit*10 # num에 10을 곱해 자리수 높여주기
    
    # num에 +1 , -1한 것 calcs에 추가. 이때 일의자리가 0이면 +1한 것만 넣고, 9라면 -1한것만 넣기 
    if(units==9):
      n_stairs.append(new_num+units-1)
    elif(units==0):
      n_stairs.append(new_num+units+1)
    else:
      n_stairs.append(new_num+units-1)
      n_stairs.append(new_num+units+1)
      
  calcs.append(n_stairs)
  return

# n이 2이하이면 calcs에 개수 꺼내서 출력
if(n<=2):
  print(len(calcs[n-1]))
# n이 2 초과면 calcs 구하기 
else:
  for i in range(1,n):
    getStairNum(i)
  print(len(calcs[n-1]))