n = int(input())
cnt = 1
o_cnt = 0

while (True) :
    print(n*cnt, end=' ')
    if (n*cnt)%5==0:
        o_cnt += 1
    if o_cnt==2:
        break
    cnt += 1