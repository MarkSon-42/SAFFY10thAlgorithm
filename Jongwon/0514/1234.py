# 1234 비밀번호


tc = 10

for test_case in range(1, tc + 1):
    n, nums = input().split()
    n = int(n)
    nums = list(nums)
    stack = []
    for i in range(n):        
        #스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(nums[i])
        #제일 뒤에 있는 원소를 비교
        elif stack[-1] == nums[i]:
            stack.pop()
        #삭제 가능한 문자가 없을 때
        else:
            stack.append(nums[i])
        
    ans = ''.join(map(str, stack))
    print("#{} {}".format(test_case, ans))

# 1차시에 정렬을 해서 stack에 넣었다가 테스트 케이스가 1개만 맞아서 정렬을 안해야 비밀번호 그대로 출력