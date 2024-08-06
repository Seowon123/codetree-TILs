N = int(input())
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(N):
    drt, drtc = input().split()
    drtcnt = int(drtc)
    while (drtcnt > 0):
        if drt == 'N':
            x, y = x + dx[0], y + dy[0]
        elif drt == 'E':
            x, y = x + dx[1], y + dy[1]
        elif drt == 'S':
            x, y = x + dx[2], y + dy[2]
        else :
            x, y = x + dx[3], y + dy[3]
        drtcnt-=1

print(x, y)