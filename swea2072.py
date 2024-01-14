T = int(input())  # 테스트케이스의 개수 입력
for test_case in range(1, T + 1):  # 각 테스트케이스에 대한 반복
    t = list(map(int, input().split()))  # 각 테스트케이스의 정수들을 리스트로 입력받음
    total_sum = 0  # 홀수의 합계를 저장할 변수 초기화
    for i in t:  # 각 정수에 대해 반복
        if i % 2 == 1:  # 정수가 홀수일 경우
            total_sum += i  # 홀수를 합계에 더함
    print('#{} {}'.format(test_case, total_sum))  # 현재 테스트케이스의 결과 출력
