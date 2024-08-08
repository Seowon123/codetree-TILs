#입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#초기설정
x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0
total_cnt = 0
#범위확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

#칸 한칸씩 이동
#1의 개수 확인 반복
while True:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    if cnt >= 3:
        total_cnt += 1
    cnt = 0
    y += 1
    if y > n:
        x += 1
        y = 0
    if x > n:
        break

print(total_cnt)