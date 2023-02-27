## <파이썬 기본문법>
### [입출력]
  * 입력을 위한 전형적인 소스코드
  ```python
  #데이터의 개수 입력
  n=input(input())
  #각 데이터를 공백으로 구분해 입력
  data= list(map(int, input().split()))
  
  n,m,k= map(int,input().split())
  ```
  -데이터를 입력 받을 때는 input()을 이용한다.
  - input()의 경우 한 줄의 문자열을 입력 받도록 해준다.
  - 입력받은 데이터를 정수형 데이터로 처리하기 위해서는 문자열을 정수로 바꾸는 int() 함수를 사용해야 한다.
  - 여러 개의 데이터를 입력 받을 때는 데이터가 공백으로 구분되는데, 띄어쑤기로 구분해 각각 정수 자료형의 데이터로 저장하는 코드를 자주 사용한다.
  - 이는 ```list(map(int, input().split()))```을 이용하면 된다.
  - input()으로 문자열을 입력받음 -> split()을 이용해 공백으로 나눈 리스트로 바꿈 -> map을 이용해 해당 리스트의 모든 원소에 int()함수 적용 -> list()로 바꿈
  
### [반복문]
  #### 1. while 문
  ```python
  #1~9까지i의 합
  i=1
  while i<=9:
    result+=i
    i+=1
  print(result)
  
  #1~9까지 홀수만 더하고 싶을 때
  i=1
  result=0
  while i<=9:
    if i% 2 ==1: #2로 나눈 나머지가 1이면
      result+=1
    i+=1
  print(result)
  ```
  
  #### 2. for문
  * for 변수 in 리스트: 실행할 소스코드
  * in 뒤에 오는 데이터는 리스트, 튜플, 문자열 등이 사용될 수 있다. 
  * range(시작값, 끝값+1, 증가): 수를 차례대로 나열할 때 사용 
  * range(끝값) : 자동으로 0부터 시작 
  ```python
  #continue 예문 : continue를 만나면 프로그램의 흐름은 반복문 처음으로 간다.
  scores=[90,85,77,65,97]
  black_list={2,4}
  for i in range(5):
    if i+1 in black_list:
      continue
    if scores[i]>=80:
      print(i+1,"번 학생은 합격입니다.")
  ```
 ### [주요 라이브러리의 문법과 유의점]
  * 표준 라이브러리란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리를 의미한다.
  * Built in functions: print(), input()같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리. 
  * itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공
  * heapq: 힙 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용
  * bisect: Binary Search 기능을 제공하는 라이브러리
  * collections: deque, Counter 등의 유용한 자료구조를 포함하고 있는 라이브러리
  * math: 필수적인 수학적 기능을 제공하는 라이브러리. 팩토리얼, 제곱근, 최대공약수(GCD-greatest common divisor), 삼각함수 관련 함수부터 pi와 같은 상수를 포함
  #### 1. Built in functions
  * import 명령어 없이 바로 사용할 수 있는 내장 함수
  * iterable object: any object that can return its elements one at a time. This includes objects like lists, tuples, dictionaries, sets, strings, and generators.
  * ```sum(iterable,/,start=0)```
    - 
  
********************************  

## <그리디>
* 어떤 문제가 있을 때, 탐욕적으로 문제를 푸는 알고리즘이다.
* 현재 상황에서 지금 당장 좋은 것만 고르는 방법
* '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다.
