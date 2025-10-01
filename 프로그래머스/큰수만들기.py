def solution(number, k):
    '''
    앞자리가 큰 수로 만들기
  
    '''
    arr= list(map(int,number))
    stack=[]
    
    for n in arr:
        while(len(stack) and stack[-1]<n and k>0):
            stack.pop()
            k-=1
        stack.append(n)
        
    while(k>0):
        stack.pop()
        k-=1
        
    
    result=''.join(map(str,stack))
    return result
    
        