h, w = map(int, input().split())

b = 10000*w/(h**2)

print(f"{b*10//10:.0f}")
if b>=25:
    print('Obesity')