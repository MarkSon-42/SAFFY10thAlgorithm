# 4466 최대 성적표 만들기

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse = True) # 내림차순 정렬
    arr = []
    for i in range(k): # 내림차순 정렬해서 k개 만큼 큰 순으로 추출해서 총합 반환
        arr.append(nums[i])
    ans = sum(arr)
    
    print("#{} {}".format(test_case, ans))