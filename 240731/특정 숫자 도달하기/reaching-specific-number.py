arr = list(map(int, input().split()))
a_sum = 0
cnt = 0
a_avg = 0

for i in arr:
    if i>=250:
        break
    a_sum += i
    cnt += 1

a_avg = a_sum/cnt

print(f"{a_sum} {a_avg:.1f}")