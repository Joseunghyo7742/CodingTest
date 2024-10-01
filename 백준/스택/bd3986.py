n= int(input())

#선끼리 교차하지않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝을 짓는다.
count=0


for i in range(n):
  line= input()
  stack=[]
  for j in line:
    if(len(stack)==0):
      stack.append(j)
    elif(stack[-1]==j):
      stack.pop()
    else:
      stack.append(j)
  if(len(stack)==0): count+=1
  
print(count)
      