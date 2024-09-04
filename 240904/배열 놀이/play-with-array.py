#n은 두번째 줄에 입력되는 숫자 수
#p는 세번째부터 입력되는 줄 수
n, p = map(int, input().split())
arr = list(map(int, input().split()))
que = []
#반복문으로 p번 입력받기
for i in range(p):
    que.append(list(map(int, input().split())))
#arr = [1, 8, 5]
#que = [[1, 1], [2, 5], [3, 1, 2]]

#반복분 p번 실행
for i in range(p):
    #1일때 - a번째 원소 출력
    if que[i][0] == 1:
        #인데스는 0부터 시작하므로 -1
        m = que[i][1] - 1
        print(arr[m])
    #2일때 - b의 위치 찾기
    elif que[i][0] == 2:
        #b의 위치 저장 인덱스 cnt
        cnt = 0
        j = 1
        for elem in arr:
            if elem == que[i][1]:
                cnt = j
                break
            j += 1
        print(cnt)
    #3일때 s부터 e까지 원소 차례대로 출력
    else:
        a, b = que[i][1] - 1, que[i][2]
        for elem in range(a, b):
            print(arr[elem], end=' ')
        print('')