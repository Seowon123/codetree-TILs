#입력
arr = []
for _ in range(3):
    arr.append(input().split())

clinic = [0, 0, 0, 0]
for i in range(3):
    #i가 홀수 일 때 == 숫자가 아닐때
    if arr[i][0] == 'Y' and int(arr[i][1]) >= 37:
        clinic[0] += 1
    elif arr[i][0] == 'N' and int(arr[i][1]) >= 37:
        clinic[1] += 1
    elif arr[i][0] == 'Y' and int(arr[i][1]) < 37:
        clinic[2] += 1
    else:
        clinic[3] += 1

for elem in clinic:
    print(elem, end=' ')
if clinic[0] >= 2:
    print('E')