# 12004. 구구단 1

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ans = "No"
    for i in range(1, 10):
        if N % i == 0 and 1<= N / i <=9: # 딱 나누어 떨어지는 수이고 몫이 1~9 범위 내라면 yes, 아니라면 no 반환
            
            ans = "Yes"
    
    print("#{} {}".format(test_case, ans))