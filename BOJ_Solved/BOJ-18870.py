# coding=utf-8
"""
백준 18870번 : 좌표 압축
"""
import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
sort_array = sorted(list(set(array)))

dic = {sort_array[i]: i for i in range(len(sort_array))}

for a in array:
    print(dic[a], end=' ')

