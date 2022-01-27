"""
백준 9996번 : 한국이 그리울 땐 서버에 접속하지
"""
import re, sys
input = sys.stdin.readline
n = int(input())
s,e = input().rstrip().split("*")
pt = re.compile(s+".*"+e+"+")

for i in range(n):
    string = input().rstrip()
    a = pt.search(string)
    if a and a.group() == string:
        print("DA")
    else:
        print("NE")