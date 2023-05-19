def dfs(index, sum_num):
    global case
    if K < sum_num: # 가지치기(k 보다 숫자 합이 더 크면 더이상 진행할 필요없으므로 stop)
        return
    if index == N: # 종료 조건 : 리스트의 인덱스 값이 숫자의 개수(N)와 같아 질때 종료 
        if sum_num == K: # 숫자의 합이 K와 같으면 경우의 수 1 증가
            case += 1
        return
    
    dfs(index+1, sum_num + nums[index]) # 배열의 다음 숫자를 더하는 경우
    dfs(index+1, sum_num) # 배열의 다음 숫자를 안더하는 경우


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    case = 0 # 경우의 수
    dfs(0,0)
    
    print("#{} {}".format(test_case, case))