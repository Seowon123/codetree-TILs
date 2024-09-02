n = int(input())
arr = list(map(int, input().split()))
cnt = [0]*9
for i in arr:
    cnt[i-1] += 1

for j in cnt:
    print(j)