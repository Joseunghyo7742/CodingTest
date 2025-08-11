'''
균형잡힌 세상
푼날짜 8/9
'''


import sys
input= sys.stdin.readline


while(True):
  line= input()
  stack=[]
  ok=False
  if(line=="."):
    break
  for c in line:
    if(c =="(" or c== "["):
      stack.append(c)
    elif(c==")"):
      if not stack or stack[-1]!="(":
        ok=False
        break
      stack.pop()
  if(len(stack)):
    print("no")
  else:
    print("yes")

