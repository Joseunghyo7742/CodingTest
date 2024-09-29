from collections import deque


q= deque()

l= [1,2,3,4,5,6,7,7,8,9,7,10]
q.extend(l)
q.remove(7)
print(q)

q.rotate(3)
print(q)