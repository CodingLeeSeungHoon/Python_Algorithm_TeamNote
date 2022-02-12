"""
백준 1339번 : 단어 수학
"""
from collections import Counter

N = int(input())
nums = []
alpha = set()

for _ in range(N):
    num = input()
    for n in num:
        alpha.add(n)
    nums.append(num)

nums.sort(key=lambda x: -len(x))

max_len = len(nums[0])
for n in range(len(nums)):
    nums[n] = "0" * (max_len - len(nums[n])) + nums[n]

dicts = {a: 0 for a in alpha}

for i in range(max_len):
    array = []
    for num in nums:
        if num[i] != '0':
            array.append(num[i])
    counts = Counter(array)
    for c in counts:
        dicts[c] += counts[c] * (10 ** (max_len - i))

sorted_dict = sorted(dicts.items(), key=lambda item: item[1], reverse=True)
temp = 9

for s in sorted_dict:
    for n in range(len(nums)):
        nums[n] = nums[n].replace(s[0], str(temp))
    temp -= 1

ans = 0
for n in nums:
    ans += int(n)
print(ans)