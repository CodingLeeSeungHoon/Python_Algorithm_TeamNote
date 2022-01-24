# coding=utf-8
"""
백준 11403번 : 경로 찾기
플로이드-워셜 쉬운 버젼
"""
import sys

input = sys.stdin.readline

N = int(input())
graph = []

for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(N):
    print(*graph[i])