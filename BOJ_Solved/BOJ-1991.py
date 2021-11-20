"""
백준 1991번 : 트리순회
"""

n = int(input( ))
tree = {}


def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])


def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])


def pastorder(node):
    if node == '.':
        return
    pastorder(tree[node][0])
    pastorder(tree[node][1])
    print(node, end='')


for _ in range(n):
    node, left, right = input( ).split( )
    tree[node] = (left, right)

preorder('A')
print( )
inorder('A')
print( )
pastorder('A')