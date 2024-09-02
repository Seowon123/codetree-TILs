num = int(input())
arr = list(map(int, input().split()))

arr_ = [i**2 for i in arr]

for j in range(num):
    print(arr_[j], end=' ')