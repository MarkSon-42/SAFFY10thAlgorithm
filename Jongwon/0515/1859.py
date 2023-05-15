# 1859 백만 장자 프로젝트


T = int(input())

for test_case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_now = 0 # 최댓값
    answer = 0 # 최대 이익

    for now in nums[::-1]: # 배열 뒤에서 부터 최댓값을 갱신을 하여 배열의 값보다 최댓값이 작으면 최댓값과 배열의 차 만큼 최대 이익에 더해서 갱신
        if now >= max_now: # 팔 값 >= 최댓값
            max_now = now
        else:
            answer += (max_now - now)
    
    print("#{} {}".format(test_case + 1, answer))