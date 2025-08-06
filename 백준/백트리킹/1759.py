# 암호만들기
# L개의 알파벳 문자 (최소 한 개의 모음, 최소 두 개의 자음), 오름차순 암호
# C- 암호화에사용할 문자 종류
# 가능성있는 모든 암호 

def inspect(st):
  vowel=0
  consonant=0
  for i in st:
    if i in ['a','e','i','o','u']:
      vowel+=1
    else:
      consonant+=1
  
  if(vowel>=1 and consonant>=2):
    return True
  return False
  

combi=[]
def makeCombi(start):
  if(len(combi)==l):
    isPrintable= inspect(combi)
    if(isPrintable): print(''.join(combi))
    return
  else:
    for i in range(start, len(alp)):
      combi.append(alp[i])
      makeCombi(i+1)
      combi.pop()
  
  

l,c= map(int,input().split()) # l 암호자리수, c는 들어올 문자입력수 
alp= list(input().split())

alp.sort()

makeCombi(0)
# a c i s t w
