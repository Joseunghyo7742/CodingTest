# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.




while(1):
  line= input()
  st=[]
  isBalanced=True
  if(line=="."): 
    break
  for i in line:
    if(i=="(" or i=="["):
      st.append(i)
    elif(i==")"):
      if(len(st)==0 or st[-1] !="("):
        isBalanced=False
        break
      st.pop()
    elif(i=="]"):
      if(len(st)==0 or st[-1] != "["):
        isBalanced=False
        break
      st.pop()
      
  if(len(st)==0 and isBalanced): #)( 인경우 , (((의 경우.. 
    print("yes")
  else:
    print("no")
