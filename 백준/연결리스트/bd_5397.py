#키로거
n= int(input())

for _ in range(n):
  line= input()
  left=[]
  right=[]
  for i in line:
    if i=="<":
      if left:
        right.append(left.pop())
        print(left, right)
    elif i==">": 
      if right:
        left.append(right.pop())
        print(left, right)
    elif i=="-": 
      if left:
        left.pop()
        print(left, right)
    else:
      left.append(i)
      print(left, right)
  
  
  left.extend(reversed(right))
  print(''.join(left))

  
#   2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t

# BAPC
# ThIsIsS3Cr3t

