T = 10
 
for _ in range(T):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    res = 0     ## 가장 긴 회문의 길이
    n = 100     ## 100부터 시작
 
    ## 가로 회문찾기
    for i in range(100):
        for t in range(100, 0, -1):     ## 100부터 회문의 길이 찾아가기
                for j in range(100 - t + 1):
                    if arr[i][j:j + t] == arr[i][j:j + t][::-1]:  ## 회문인 경우
                        res = max(res, len(arr[i][j:j + t]))
 
    ## 세로 회문찾기
    for i in range(100):
        for t in range(100, 0, -1):  ## 100부터 회문의 길이 찾아가기
            for j in range(100 - t + 1):
                ts = ''
                for k in range(j, j + t):
                    ts += arr[k][i]
 
                if ts == ts[::-1]:  ## 회문인 경우
                    res = max(res, len(arr[i][j:j + t]))
 
 
 
    print('#{} {}'.format(tc, res))