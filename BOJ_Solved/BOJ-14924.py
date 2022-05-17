"""
백준 14924번 : 폰 노이만과 파리
"""
S, T, D = map(int, input().split())
time = D/(S*2)
print(int(T*time))