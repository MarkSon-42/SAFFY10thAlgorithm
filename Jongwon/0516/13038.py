T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    days = list(map(int, input().split()))
    
    # 최소 일수를 저장할 변수
    min_days = float('inf')
    
    # 수업이 열리는 첫 번째 요일부터 시작하여 7일 주기로 확인
    for start_day in range(7):
        count = 0  # 수업 일수를 세는 변수
        current_day = start_day  # 현재 요일을 저장할 변수
        
        # n일 동안 수업 확인
        for _ in range(n):
            # 현재 요일에 수업이 열리는 경우 count를 증가
            if days[current_day] == 1:
                count += 1
            current_day = (current_day + 1) % 7  # 다음 요일로 이동
            
        # 현재 시작 요일에서의 수업 일수가 최소값인지 확인
        min_days = min(min_days, count)
    
    print("#{} {}".format(test_case, min_days))