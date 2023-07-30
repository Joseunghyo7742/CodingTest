'''
개체를 차례대로 옮기는 시뮬레이션 유형 문제
'''
n= int(input()) #공간의 크기를 나타내는 n
x,y=1,1
plans=input().split()

#L R U D 움직임
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan== move_types[i]:
      nx= x+dx[i]
      ny= y+dy[i]
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  x,y= nx,ny

print(x,y)

