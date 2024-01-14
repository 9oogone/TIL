
#%%
T = int(input()) # testcase의 개수
for test_case in range(1, T + 1): # test_case 1부터 T+1까지(T개), range(start, stop-1)
    t = list(map(int, input().split())) # T+1개 입력받은 case를 띄어쓰기에 따라 하나하나의 정수로 구분
    t.sort(reverse=True) # t의 list를 내림차순으로 정렬
    print('#{} {}'.format(test_case, t[0])) # t의 list에서 0번째 순서에 오는 값 출력