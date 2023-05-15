T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    for i in range(len(price)):
        max_benefit_list = []
        max_benefit = 0
        for j in range(1, len(price)):
            if price[j] - price[i] > max_benefit:
                max_benefit = price[j] - price[i]
        max_benefit_list.append(max_benefit)

    print(f"#{T} {sum(max_benefit_list)}")





