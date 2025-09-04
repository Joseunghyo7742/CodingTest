'''
단어 정렬
푼 날짜: 25.09.03

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.
주어지는 문자열의 길이는 50을 넘지 않는다.
'''

n= int(input())
words=[]
for _ in range(n):
  words.append(input())

set_words= set(words)
words=list(set_words)

words.sort(key=lambda x:(len(x),x))
for k in words:
  print(k)
  
'''
words={input().strip() for _ in range(5)}
for w in sorted(words, key=lambda x: (len(x),x)):
  print(w)
'''