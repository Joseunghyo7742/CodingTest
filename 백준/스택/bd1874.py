import sys

n= int(sys.stdin.readline())

#1~n수를 스택에 넣었다 뺴면서 하나의 수열을 만드다.
# push순서는 반드시 오름차순 . 어떤 순서로 push pop? 
#4 3 6 8 7 5 2 1
#1 2 3 4 5 6 7 8
#push는 오름차순만 가능 

result=[]
stack=[]
count=1
for i in range(n):
  num= int(input())
  while count <=num:
    stack.append(count)
    result.append('+')
    count+=1
  if(stack[-1]== num):
    stack.pop()
    result.append('-')
  else:
    print("NO")
    exit()

for i in result:
  print(i)
  
