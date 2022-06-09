"""
백준 10867번 : 중복 빼고 정렬하기
"""
_ = input()
print(*sorted(set(map(int, input().split()))))