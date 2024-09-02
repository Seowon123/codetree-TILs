n = int(input())
arr = list(map(int, input().split()))

arr_even = [i for i in arr if i % 2 == 0]

for elem in arr_even:
    print(elem, end=' ')