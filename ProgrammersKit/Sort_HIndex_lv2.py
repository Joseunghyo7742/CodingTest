def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i #l-i가 h임 즉 h개 이상인지 확인하는 작업.
    return 0