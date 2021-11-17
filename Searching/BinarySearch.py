nums = [i for i in range(10)]

# 내가 리스트 안에 넣고 싶은 값
n = 5
start = 0
end = len(nums) -1

while start <= end:
    mid = (start + end) // 2
    if nums[mid] >= n:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)