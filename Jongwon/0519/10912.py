T = int(input())

for test_case in range(1, T+1):
    string = list(input())
    string.sort() 
    stack = []
    for i in range(len(string)): 
        if len(stack) == 0: # 스택에 아무것도 없으면 문자열의 원소 하나를 넣고
            stack.append(string[i])
        elif stack[-1] == string[i]: # 스택에 원소가 있으면 스택의 마지막 원소와 해당하는 위치의 문자열의 원소가 같으면 스택에서 pop(짝이 맞춰지면 pop)
            stack.pop()
        else:
            stack.append(string[i]) # 둘 다 아니라면 문자열의 해당하는 위치의 문자를 스택에 추가
    if len(stack) == 0: # 스택에 아무것도 없다면 good 반환, 있으면 남은 원소 join해서 문자열 반환
        ans = "Good"
    else:
        ans = ''.join(map(str, stack))
    
    print("#{} {}".format(test_case, ans))