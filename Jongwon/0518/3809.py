# 3809. 화섭이의 정수 나열 

T = int(input())
 
for test_case in range(1, T + 1):
    n = int(input())
    nums = ''
    while True:
        nums += ''.join(map(str, input().split()))
        if len(nums) == n:
            break
    ans = 0
    while str(ans) in nums:
        ans += 1
    print("#{} {}".format(test_case, ans))

# 로직 : ans를 0부터 증가시켜 입력값으로 받는 num까지 반복해 없으면 그 수를 반환한다.