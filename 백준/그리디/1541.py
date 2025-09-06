'''
잃어버린 괄호

푼 날짜: 25.09.05

괄호를 적절히 쳐서 식을 최소로 만들기 


55-50+30-10+20
55-(80)-(10+20)


-를 만나면 그 다음 마이너스가 나올 때까지 더해준다. => 스택에 쌓아준다?

'''

line= input().split(sep="-")

result=0
for i in range(len(line)):
  l= line[i]
  sums=0
  if '+' in l:
    tmp= l.split(sep="+")
    for t in tmp:
      if(t!="+"):
        sums+=int(t)
  else:
    sums=int(l)
  if(i==0):
    result+=sums
  else:
    result-=sums
print(result)
# +나 -가 나올때까지 번호로 인식하여 번호로 바꾸기
# -가 나오면 다음 -가 나올때까지 괄호로 더해주는 것
# 다음 -가 나오면 -로 묶어서 result에 마이너스해주기
#- 안나오면 그냥 더해주면됨





