def flattern_boxes(test_cases):
    output = []

    for i, (dump_count, heights) in enumerate(test_cases, 1):
        # 상자들 높이 정렬하기
        sorted_heights = sorted(heights)

        # 반복문을 통해 주어진 덤프 숫자 만큼 평탄화 하기
        for _ in range(dump_count):
            # 최고 높이 박스를 최소 높이 박스로 덤핑
            sorted_heights[0] += 1
            sorted_heights[-1] -= 1

            # 다음 반복문 되풀이를 위해 다시 정렬 ( 갱신 )
            sorted_heights.sort()

            # 높이 차이 계산
            diff = sorted_heights[-1] - sorted_heights[0]

            # 높이차가 1 혹은 그 아래면 더 평탄화 할 필요 없으니 break
            if diff <= 1:
                break
        output.append((i, diff))

    return output



def main(): # 프로그램의 주요 논리를 포함하는 메인 함수가 이곳에 정의.
    # input.txt file 읽기
    with open('input.txt', 'r') as file:
        # with문은 읽기 모드에서 txt파일을 열고, 블록이 종료되면 자동을 파일을 닫는 데 사용. 그리고 열린 파일은 file 변수에 할당된다.
        lines = file.readlines()
        #file.reaselines()는 파일의 모든 줄을 읽고 변수 line에 리스트로 저장한다.
        test_case_count = int(lines[0].strip())
        # 파일의 첫번째 줄은 테스트 케이스의 수를 나타낸다. 여기서는 덤핑 횟수를 나타냄.
        # strip() 함수는 선행 및 후행 공백을 제거해준다.
        test_cases = []
        # 파싱된 값들을 저장하기 위해 빈 리스트를 초기화해준다.
        for i in range(0, len(lines), 2):
            dump_count = int(lines[i].strip())
            heights = list(map(int, lines[i + 1].strip().split()))
            test_cases.append((dump_count, heights))






if __name__ == '__main__':
    main()