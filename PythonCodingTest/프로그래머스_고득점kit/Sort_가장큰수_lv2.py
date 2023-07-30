def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers.sort(reverse=True)
    for i in numbers:
        answer+=i
    return answer
#실패 이유: [3,30,34,5,9] 의 경우 30보다 3이 더 높은 순위로 나와서.
#해결방법: 1000이하 . 3-> x*3을 해서 비교한다. 자릿수를 채워줌 

def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers.sort(reverse=True, key=lambda x: x*3)
'''return str(int(''.join(numbers))) 한줄로 처리가능 ''' 
    for i in numbers:
        answer+=i 
    if answer[0]=='0': #반드시 예외 부분을 생각해줘야 한다.
        return '0' #놓친부분.. '0000'= '0'이다. 
    return answer