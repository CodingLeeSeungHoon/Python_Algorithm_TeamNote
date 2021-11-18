"""
백준 3052번 : 나머지
"""

rest = []
for _ in range(10):
    num = int(input()) % 42
    rest.append(num)

print(len(set(rest)))