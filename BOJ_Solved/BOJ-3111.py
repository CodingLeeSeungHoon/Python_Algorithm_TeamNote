"""
백준 3111번 : 검열
"""
import sys

pattern = sys.stdin.readline().rstrip()
text = sys.stdin.readline().rstrip()

pattern = list(pattern)
reverse_pattern = list(reversed(pattern))

len_pattern = len(pattern)

front = []
back = []

frontIdx = 0
backIdx = len(text) - 1

flag = True

while frontIdx <= backIdx:

    if flag:
        front.append(text[frontIdx])
        frontIdx += 1
        if front[-len_pattern:] == pattern :
            front[-len_pattern:] = []
            flag = False

    else:
        back.append(text[backIdx])
        backIdx -= 1

        if back[-len_pattern:] == reverse_pattern:
            back[-len_pattern:] = []
            flag = True

while back:
    front.append(back.pop())

    if front[-len_pattern:] == pattern:
        front[-len_pattern:] = []

answer = "".join(front)
print(answer)
