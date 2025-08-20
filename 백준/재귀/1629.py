'''
곱셈
푼 날짜: 25.08.20

a,b,c가 주어지면 a를 b번 곱한 수를 c로 나눈 나머지 구하기
단순히 A^B 를 계산하면 B가 최대 2,147,483,647 까지 가능하기 때문에 시간 초과 + 메모리 초과가 발생

'''

def mul(a,b,c):
  if b==1:
    return a%c 
  # b를 절반으로 줄여 재귀호출
  temp= mul(a,b//2, c)
  
  # b가 홀수인 경우
  if b%2 ==1:
    return ((temp*temp)%c) *a%c # 절반 나눈 것에서 하나를 곱해줘야 함
  else:
    return (temp*temp)%c
  
  