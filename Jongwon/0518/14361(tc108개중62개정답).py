# 14361. 숫자가 같은 배수

# testcase 108 중 62개만 정답


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    n = str(N)
    nums = []
    for i in n:
        nums.append(i)
    k = 1
    res = "impossible"
    while True:
        k += 1
        N *= k
        a = str(N)
        arr = []
        for num in a:
            arr.append(num)
        
        if len(n) < len(a):
            break 

        for b in nums:
            if b in arr:
                arr.remove(b)
        
        if len(arr) == 0:
            res = "possible"
            break
        
        arr.clear()
    
    print("#{} {}".format(test_case, res))

# 로직 : input 수로 이루어진 리스트와 k배한 숫자 리스트를 대조하여 앞의 리스트 안에 있는 숫자를 k배한 숫자 리스트에서 제거하고
# 반복문 종료후 리스트안에 아무것도 없으면 재배열로 배수를 만들수 있으므로 possible, 아니라면 impossible 반환

