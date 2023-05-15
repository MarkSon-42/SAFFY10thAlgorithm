# 우선 그림을 보면 인접 중복 요소를 제거하는 형태 -> 스택이 바로 떠오름
# 구현해보고 안되면 다른걸로 시도.

for t in range(10): # 테케가 10개라서 0..9까지 10번 반복.
    s, pw = input().split()
    pw = list(pw)
    stack = []

    while pw:
        stack.append(pw.pop())
        while pw and stack and stack[-1] == pw[-1]: # 비밀번호 연속 같은 두개인지 조건
            stack.pop()
            pw.pop()

    print(f"#{t} {''.join(stack)[::-1]}") # 스택을 그대로 뿌리면 거꾸로기 때문에 역순으로 출력해주기.
