# %%
N = int(input()) #입력할 정수의 개수
nums = list(map(int, input().split())) #공백을 기준으로 입력되는 정수들을 list로 저장
nums.sort() #오름차순으로 배열
print(nums[N//2])#[N//2]는 nums라는 리스트에서 N//2에 있는 원소를 가져오라