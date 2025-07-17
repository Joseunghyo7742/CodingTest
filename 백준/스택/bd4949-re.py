# 균형을 이룬다 = 짝을 이루는 두 괄호 그 사이 문자열이 균형잡힘
# 입력 종료조건은 온점. 각 줄마다 균형잡혔다면 yes 아니라면 no 출력

# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .

# 입력 한줄 씩 받기. yes 또는 no 출력
# 괄호가 들어오면 스택에 넣기, 같은 괄호 닫기일때만  스택에서 pop 
# 온점을 만날때 스택에 쌓여있는게 있다면 no 
# 괄호 하나도 없어도 균현잡힌것

# ((()) 이경우란면? 
stack=[]
while(True):
  isBalanced=True
  line= input()
  if(line[0]=='.'): 
    break
  for s in line:
    if(s=="(" or s=="["):
      stack.append(s)
    elif(s==")"):
      if(len(stack)>0 and stack[-1]=="("):
        stack.pop()
      else:
        isBalanced=False
        break
    elif(s=="]"):
      if(len(stack)>0 and stack[-1]=="["):
        stack.pop()
      else:
        isBalanced=False
        break
  if(len(stack)>0 or not isBalanced):
    print("no")  
    stack=[]
  else:
    print("yes")  
  
  