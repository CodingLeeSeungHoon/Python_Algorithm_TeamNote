# coding=utf-8
"""
백준 1287번 : 할 수 있다
"""

S = input()
try:
    eval(S.replace("+", "&").replace("-", "&").replace("/", "&").replace("*", "&"))
    print(int(eval(S.replace("/", "//"))))

except:
    print("ROCK")