"""
백준 2644번 : 촌수계산
"""
from collections import deque

def bfs(first, end):
    queue = deque()
    queue.append([first, 0])

    while queue:
        person, chonsu = queue.popleft()
        visited[person] = True
        if person == end:
            return chonsu
        for i in home[person]:
            if visited[i] is False:
                queue.append([i, chonsu+1])

    return -1


n = int(input())
a, b = map(int, input().split())

home = [[] for _ in range(n+1)]
visited = [False] * (n+1)

m = int(input())

for _ in range(m):
    c, d = map(int, input().split())
    home[c].append(d)
    home[d].append(c)

print(bfs(a, b))
