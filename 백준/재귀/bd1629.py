a, b, c = list(map(int, input().split()))

#모듈러 분배법칙 사용
def mul(a,b,c):
  if b==1:
    return a%c
  
  temp = solution(a,b//2,c)
  
  if b%2 ==1:
    return ((temp*temp)%c) * a%c
  else:
    return(temp* temp) %c 
  
  