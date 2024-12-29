candy=6
answer=0
for A in range (1,candy):
  for B in range(1,candy):
    for C in range(1,candy):
      if(A+B+C==6 and A>=B+2 and C%2==0):
        answer+=1

print(answer)