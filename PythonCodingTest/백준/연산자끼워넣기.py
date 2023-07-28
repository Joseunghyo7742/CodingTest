n= int(input()) #수의 개수
numbers= list(map(int,input().split())) #수열
operators=list(map(int,input().split())) #연산자 + - x %

result=[]

def dfs(i, sum):
  if(i==n): 
    result.append(sum)
    return
  if(operators[0]>0):
    operators[0]-=1
    dfs(i+1,sum+numbers[i])
    operators[0]+=1
    
  if(operators[1]>0):
    operators[1]-=1
    dfs(i+1,sum-numbers[i])
    operators[1]+=1
    
  if(operators[2]>0):
    operators[2]-=1
    dfs(i+1, sum*numbers[i])
    operators[2]+=1
    
  if(operators[3]>0):
    operators[3]-=1
    dfs(i+1, int(sum/numbers[i]))
    operators[3]+=1
    
    
  
dfs(1,numbers[0])
print(max(result))
print(min(result))