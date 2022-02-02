"""
백준 1016번 : 제곱 ㄴㄴ 수
에라토스테네스의 체 심화 응용
"""

min, max = map(int, input().split())

seive = [1 for _ in range(max-min+1)]

i = 2

while i**2 <= max:
    mul = min // (i**2)
    while mul * (i**2) <= max:
        if 0 <= mul * (i**2) - min <= max-min:
            seive[mul * (i**2) - min] = 0
        mul += 1
    i += 1

print(sum(seive))