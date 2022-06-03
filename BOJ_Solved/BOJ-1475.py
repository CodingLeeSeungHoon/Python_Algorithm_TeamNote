"""
백준 1475번 : 방 번호
"""
import math
N = input()
nums = [0 for _ in range(9)]
for n in N:
    if n != '6' and n != '9':
        nums[int(n)] += 1
    else:
        nums[6] += 1
nums[6] = math.ceil(nums[6] / 2)
print(max(nums))
