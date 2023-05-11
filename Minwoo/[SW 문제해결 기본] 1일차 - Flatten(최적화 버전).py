t = int(input())

for test_case in range(1, t + 1):
    dmp_cnt = int(input())
    boxes = list(map(int, input().split()))

    while dmp_cnt > 0:
        max_box = max(boxes)
        min_box = min(boxes)
        if max_box - min_box <= 1:
            break

        max_index = boxes.index(max_box)
        min_index = boxes.index(min_box)

        boxes[max_index] -= 1
        boxes[min_index] += 1

        dmp_cnt -= 1

    result = max(boxes) - min(boxes)
    print(f"#{test_case} {result}")
