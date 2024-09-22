#알파벳 대문자로된 최대 50자
# "I'm Sorry Hansoo"
# 정답 여러개면 사전순으로 앞서는 걸 출력

name= input()

arr=[0]*26
for i in name:
  arr[ord(i)-65]+=1
  
isOdd=name.length()%2 ==1

#홀수일경우
if(isOdd):
  check=False
  for i in arr:
    if(i%2 ==1 ): check=True
  
  
#짝수일 경우
else: 
  for i in arr:
    if(i%2 ==1):
      print("I'm Sorry Hansoo")
      return
  
  