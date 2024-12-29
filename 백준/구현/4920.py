

#다양한 모양들을 넣어봐야 하는데
#가장 큰 값 



# 13가지 모양 테트리스
t1=[[0,1],[0,2],[0,3]]
t2=[[1,0],[2,0],[3,0]]

t3=[[0,1],[1,1],[1,2]]
t4=[[1,0],[1,-1],[2,-1]]

t5=[[0,1],[0,2],[1,2]] #ㄱ
t6=[[1,0],[2,0],[2,-1]]
t7=[[0,-1],[0,-2],[-1,-2]] #ㄴ
t8=[[-1,0],[-2,0],[-2,1]]

#ㅗ
t9=[[0,1],[1,1],[0,2]]
t10=[[1,0],[1,1],[2,0]]
t11=[[0,-1],[-1,-1],[0,-2]]
t12=[[-1,0],[-1,-1],[-2,0]]

t13=[[0,1],[1,0],[1,1]]

tet_set=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13]

def getMax(r,c,value,N):
  max_val=-1000000
  for i in tet_set:
    temp=value
    isOutbound=False
    for j in range(3):
      nr= r+ i[j][0]
      nc= c+ i[j][1]
      if(nr<0 or nr>=N or nc<0 or nc>=N):
        isOutbound=True
        break
      temp+=field[nr][nc]
    if(isOutbound):
      continue
    max_val=max(max_val,temp)
  return max_val
    
count=0
while(True):
  N= int(input())
  count+=1
  if(N==0):break
  field=[]
  for _ in range(N):
    field.append(list(map(int,input().split())))
  result=-1000000
  
  for i in range(N):
    for j in range(N):
      value=getMax(i,j,field[i][j],N)
      result= max(result,value)
  
  print('{}. {}'.format(count,result))