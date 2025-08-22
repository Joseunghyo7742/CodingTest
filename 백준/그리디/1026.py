'''
보물
푼 날짜: 25.08.22

a 배열의 수만 재배열 가능 
s의 값을 최솟값으로 만들기 
'''

n= int(input()) #배열의 길이
a=list(map(int,input().split()))
b= list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

result= 0
for i in range(n):
  result+= a[i]*b[i]
  
print(result)