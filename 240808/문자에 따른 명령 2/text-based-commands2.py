x, y =0, 0
go = input()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direct = 3
for i in go:
    if i == 'L':
        direct = (direct + 3) % 4
    elif i == 'R':
        direct = (direct + 1) % 4
    else:
        x, y = x + dx[direct], y + dy[direct]

print(x, y)