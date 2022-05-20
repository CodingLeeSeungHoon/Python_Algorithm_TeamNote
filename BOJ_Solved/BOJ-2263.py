"""
백준 2263번 : 트리의 순회
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = [0] + list(map(int, input().split()))
postorder = [0] + list(map(int, input().split()))

index = [-1 for _ in range(100001)]

for i in range(1, n+1):
    index[inorder[i]] = i

def preorder(instart, inend, poststart, postend):
    if instart > inend or poststart > postend:
        return

    rootidx = index[postorder[postend]]
    leftsize = rootidx - instart
    print(inorder[rootidx], end=' ')

    preorder(instart, rootidx-1, poststart, poststart + leftsize - 1)
    preorder(rootidx+1, inend, poststart + leftsize, postend - 1)


preorder(1, n, 1, n)