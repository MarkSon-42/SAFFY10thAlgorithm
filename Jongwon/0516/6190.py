# 6190 단조

T = int(input())
 
for test_case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_result = -1 # 단조 값 곱의 최대값
    for i in range(N - 1): # N개에서 2개 뽑아서 하는 조합 
        for j in range(i + 1, N):
            check = str(nums[i] * nums[j]) # 단조값 곱
            for k in range(len(check) - 1): 
                if check[k] > check[k + 1]: # 단조가 아니면 반복 종료
                    break
            else:
                if max_result < int(check): # 곱의 최댓값을 갱신
                    max_result = int(check)
    print("#{} {}".format(test_case+1, max_result))