n, t = map(int, input().split())
rl, cl, d = input().split()
r = int(rl)
c = int(cl)

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]

x, y = r - 1, c - 1
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x + 1, y + 1)