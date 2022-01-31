"""
백준 1038번 : 감소하는 수
"""
import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()               # 모든 감소하는 수
for i in range(1, 11):      #  1~10개의 조합 만들기 (0~9이니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순
try:
    print(nums[n])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)