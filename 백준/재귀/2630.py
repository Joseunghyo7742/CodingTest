'''
색종이 만들기
푼 날짜: 25.09.01

색상이 같을때까지 4등분 
출력: 잘라진 하얀색 종이와 잘라진 파란색 종이 
'''

n= int(input()) # 4등분 할 수 있게끔 주어짐
papper=[]
for _ in range(n):
  papper.append(list(map(int,input().split())))

blue=0
white=0
# r,c 좌표를 시작으로 length 길이만큼 사각형을 봄. => 같은 색상이 있을 때까지 나눠낸다. 
def recur(r,c,length):
  global blue,white
  # 전부 같은 색상인지 확인하기. r,c 이중 반복문으로 다니면서 +length한 곳까지 검사 
  color=papper[r][c]
  is_same= all( # all은 처음 불일치가 뜨면 즉시 중단함.
    papper[i][j] ==color
    for i in range(r,r+length)
    for j in range(c,c+length)
  )
  
  if(not is_same):
    half= length//2
    #4등분 들어가기
    recur(r,c,half)
    recur(r+half,c,half)
    recur(r,c+half,half)
    recur(r+half, c+half,half)
    return
  if color==1: blue+=1
  else: white+=1
  
recur(0,0,n)
print(white)
print(blue)