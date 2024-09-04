# 입력 받기
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B가 A의 연속부분수열인지 확인
is_subsequence = False

for i in range(n1 - n2 + 1):
    # A의 부분수열을 확인
    if A[i:i+n2] == B:
        is_subsequence = True
        break

# 결과 출력
if is_subsequence:
    print("Yes")
else:
    print("No")