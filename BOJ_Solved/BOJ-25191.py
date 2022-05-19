"""
백준 25191번 : 치킨댄스를 추는 곰곰이를 본 임스
"""

chicken = int(input())
coke, beer = map(int, input().split())
print(min(coke//2 + beer, chicken))