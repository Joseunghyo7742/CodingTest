n= int(input())
arr_n= list(map(int,input().split()))
m= int(input())
arr_m= list(map(int,input().split()))

arr_n.sort()

def binary_search(t):
    s,e=0,n-1
    while(s<=e):
        mid= (s+e)//2
        if(arr_n[mid]>t):
            e=mid-1
        elif(arr_n[mid]<t):
            s=mid+1
        elif(arr_n[mid]==t):
            print(1)
            return
    print(0)
    return

for i in arr_m:
    binary_search(i)

    
    
        