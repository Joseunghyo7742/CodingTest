def search(array, target, start, end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    else:
        return search(array, target, mid + 1, end)

n = int(input())
product = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))
product.sort()


for i in range(m):
    print(search(product,request[i],0,n-1),end=' ')
