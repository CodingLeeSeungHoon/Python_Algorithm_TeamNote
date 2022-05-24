"""
백준 9466번 : 텀 프로젝트
"""
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(start):
    global group
    visited[start] = True
    cycle.append(start)
    num = students[start]

    if visited[num]:
        if num in cycle:
            group += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


t = int(input())
for _ in range(t):
    num_student = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [False for _ in range(num_student+1)]
    group = []

    for i in range(1, num_student+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(num_student - len(group))
