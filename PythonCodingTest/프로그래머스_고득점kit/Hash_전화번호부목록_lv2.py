#실패
#접두어!!!
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if (phone_book[i] in phone_book[i+1]) :
                answer=False
                return answer
    return answer
#또실패
#실패이유: 접두어로 존재해야 하기 때문 in을 쓰면 아무위치에나 해도 상관이 없어지까

#답
#실패
#접두어!!!
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if (phone_book[i] in phone_book[i+1]) :
                answer=False
                return answer
    return answer
#또실패
#실패이유: 접두어로 존재해야 하기 때문 in을 쓰면 아무위치에나 해도 상관이 없어지까