'''
그룹 단어 체커
푼 날짜: 25.09.04


aabbbccb


'''

n= int(input())
cnt=0

def check_word(str):
  if(len(str)<=2):
    return 1
  exist=[str[0]]
  for i in range(1,len(str)):
    if(str[i-1]!= str[i]):
      if(str[i] in exist):
        return 0
      exist.append(str[i])
  return 1
  
for _ in range(n):
  word=input().strip()
  if(check_word(word)):
    cnt+=1

print(cnt)


# def is_group_word(word: str) -> bool:
#     seen = set()
#     prev = word[0]
#     seen.add(prev)

#     for ch in word[1:]:
#         if ch != prev:         # 새로운 문자가 등장했을 때
#             if ch in seen:     # 이미 나온 적 있으면 실패
#                 return False
#             seen.add(ch)
#         prev = ch
#     return True


# n = int(input())
# cnt = 0
# for _ in range(n):
#     if is_group_word(input().strip()):
#         cnt += 1

# print(cnt)
