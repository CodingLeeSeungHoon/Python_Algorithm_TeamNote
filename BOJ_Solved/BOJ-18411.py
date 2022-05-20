"""
백준 18411번 : Exam
"""

score = list(map(int, input().split()))
print(sum(score) - min(score))