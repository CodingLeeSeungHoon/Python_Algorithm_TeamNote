"""
백준 6764번 : Sounds fishy!
"""

nums = [int(input()) for _ in range(4)]
if nums[0] == nums[1] == nums[2] == nums[3]:
    print("Fish At Constant Depth")
elif nums[0] < nums[1] < nums[2] < nums[3]:
    print("Fish Rising")
elif nums[0] > nums[1] > nums[2] > nums[3]:
    print("Fish Diving")
else:
    print('No Fish')