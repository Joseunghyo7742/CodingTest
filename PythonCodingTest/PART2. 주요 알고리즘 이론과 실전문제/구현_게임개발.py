n,m = map(int,input().split()) #맵의 크기
x,y, direction= map(int, input().split()) #캐릭터의 좌표 (a,b), 바라보는 방향 d

#nxm맵 생성 입력받기
d= [[0]* m for _ in range(n)]
d[x][y]=1 #현재 좌표 방문처리

# 맵 전체 정보 받기
array=[]
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#왼쪽으로 회전
def turn_left():
  global direction
  direction-=1
  if direction==-1:
    direction=3

#시뮬레이션 시작
count=1 #현재 좌표를 방문한 곳으로 체크
# 방문한 곳인지 확인하기

turn_time=0
while True: 
  turn_left()
  new_x= x+ dx[direction]
  new_y= y+ dy[direction]
  #바라보는 칸이 가보지 않았고 육지인 경우
  if(d[new_x][new_y]==0 and array[new_x][new_y]==0):
    x=new_x
    y= new_y
    count+=1
    d[x][y]=1
    turn_time=0
    continue
  else:
    turn_time+=1
  #네 방향 모두 갈 수 없는 경우
  if turn_time==4:
    new_x= x-dx[direction]
    new_y= y-dy[direction]
    #뒤로 갈 수 있다면 이동
    if (array[new_x][new_y]==0):
      x= new_x
      y= new_y
    else: #바다가 뒤에 있는 경우
      break
    turn_time=0
print(count)
      

    