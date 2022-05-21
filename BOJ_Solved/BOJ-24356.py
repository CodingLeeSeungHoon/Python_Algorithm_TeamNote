"""
백준 24356번 : ЧАСОВНИК
"""

t1, m1, t2, m2 = map(int, input().split())
start = t1 * 60 + m1
end = t2 * 60 + m2

if start > end:
    end += 24 * 60

print(end-start, (end-start) // 30)