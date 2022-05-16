"""
백준 1167번 : 트리의 지름
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start, weight):
    for i in tree[start]:
        node, w = i
        if dist[node] == -1:
            dist[node] = weight + w
            dfs(node, weight + w)


V = int(input())
tree = {x: [] for x in range(V+1)}

for _ in range(V):
    connection = list(map(int, input().split()))
    connection.pop()
    node = connection.pop(0)
    while connection:
        tree[node].append([connection.pop(0), connection.pop(0)])


dist = [-1] * (V+1)
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1] * (V+1)
dist[start] = 0
dfs(start, 0)

print(max(dist))