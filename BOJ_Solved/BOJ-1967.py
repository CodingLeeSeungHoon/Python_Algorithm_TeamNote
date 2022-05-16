"""
백준 1967번 : 트리의 지름
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs로 한 점 기준으로 거리를 잴 수 있다.
def dfs(start, weight):
    for i in tree[start]:
        node, w = i
        if dist[node] == -1:
            dist[node] = weight + w
            dfs(node, weight + w)


node = int(input())
tree = {x: [] for x in range(node+1)}

for _ in range(node-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

# 한 점 기준으로 가장 먼 곳 찾기 -> n1
dist = [-1] * (node + 1)
dist[1] = 0
dfs(1, 0)

# n1 노드 찾고, n1 기준으로 가장 먼 곳 찾기 -> n2
start = dist.index(max(dist))
dist = [-1] * (node + 1)
dist[start] = 0
dfs(start, 0)

# n1 -> n2가 트리의 지름이 됨.
print(max(dist))