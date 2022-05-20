"""
백준 21612번 : Boiling Water
"""

B = int(input())
print(5*B-400)
print(1 if 100 > B else 0 if 100 == B else -1)