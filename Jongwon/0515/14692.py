# 14692

T = int(input())

for test_case in range(1, T + 1):
    log = int(input())
    if log % 2 == 0: # 짝수여야 반으로 나눴을때 자연수가 나오므로 log가 짝수일때는 Alice를 반환하고, 홀수 일때 Bob을 반환
        ans = "Alice"
    else:
        ans = "Bob"
    
    print("#{} {}".format(test_case, ans))