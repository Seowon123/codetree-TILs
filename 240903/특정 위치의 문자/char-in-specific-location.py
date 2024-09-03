arr = ['L', 'E', 'B', 'R', 'O', 'S']

cha = input()

idx = -1

for i in range(len(arr)):
    if cha == arr[i]:
        idx = i
    
if idx == -1:
    print('none')
else:
    print(idx)