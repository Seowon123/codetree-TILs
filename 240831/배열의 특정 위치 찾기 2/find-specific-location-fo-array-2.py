arr = map(int, input().split())
arr_odd = 0
arr_even = 0
num = 1
for i in arr:
    if num % 2 == 1:
        arr_odd += i
    else:
        arr_even += i
    num += 1

result = arr_odd - arr_even
print(abs(result))