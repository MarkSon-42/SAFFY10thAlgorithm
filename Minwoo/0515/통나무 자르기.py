#... 통나무를 종이에 그려보면.. 무조건 홀짝 판별로 귀결된다.

TC = int(input())
for i in range(1, TC + 1):
    N = int(input())
    if N % 2 == 0:
        print("#{} Alice".format(i))
    else:
        print("#{} Bob".format(i))

