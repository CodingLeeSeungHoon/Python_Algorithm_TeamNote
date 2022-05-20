"""
백준 15080번 : Every Second Counts
"""

start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

start = start[0] * 3600 + start[1] * 60 + start[2]
end = end[0] * 3600 + end[1] * 60 + end[2]

if end >= start:
    print(end - start)
else:
    print(end - start + 3600 * 24)