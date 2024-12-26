n,r,c= list(map(int,input().split()))

# 함수는 4분면을 나눈다.
# 좌표가 4분면에서 어디에 위치하는지 구한다.
# 위치한 (분면-1) * 2(n+1) 
# 점점 쪼개서 분면이 각 한칸씩으로 나눌 때까지 쪼갠다. 

result=0
start_y= 0
start_x=0
end_y= 2**n
end_x= 2**n

for i in range(n,0,-1):
  #4분면 나눌 기준점
  offset= 2**(2*i-2)
  y_line=(start_y+end_y)/2
  x_line= (start_x+end_x)/2
  if(r<x_line and c < y_line):
    #1분면
    end_y= y_line
    end_x= x_line
  if(r<x_line and c>=y_line):
    #2분면
    result+=offset
    start_y= y_line
    end_x=x_line
  if(r>=x_line and c<y_line):
    #3분면
    result+= 2*offset
    end_y=y_line
    start_x= x_line
    
  if(r>=x_line and c>=y_line):
    result+= 3*offset
    start_y= y_line
    start_x= x_line
print(result)
