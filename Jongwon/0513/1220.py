# 1220 Magnetic
# 스택 사용

T = 10

for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for j in range(N): # 열로 비교
        stack = []
        for i in range(N):
            if table[i][j] == 1: # 1(N)이면 스택에 1 추가
                stack.append(1)
            if table[i][j] == 2 and stack: # 2(S)이면 스택 비우고 교착상태 1 추가
                stack.clear()
                answer += 1
 
    print("#{} {}".format(test_case, answer)) 

# 1을 넣다가 2가 나오면 교착상태로 판단하여 answer 값 증가시키는 방식