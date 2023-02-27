#입력 받기
n,m,k= map(int,input().split())
data=list(map(int,input().split()))

data.sort() #입력 받은 수 정렬
first= data[n-1]
second= data[n-2]


#first_sum= (m//k)*first*k - 문제.. 마지막 묶음이 홀수로 끝났을 때 
#second_sum= (m%k)*second
#K+1로 묶어 나눠야 했다. 
#반복되는 수열의 길이 슬라이싱을 신중하게 해주자.
first_sum= (m//(k+1))*(k*first+second)
second_sum=(m%(k+1))*first

result=first_sum+second_sum
print(result)