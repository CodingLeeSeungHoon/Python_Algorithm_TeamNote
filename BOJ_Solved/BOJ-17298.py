"""
백준 17298번 : 오큰수
"""
n = int(input())
array = list(map(int, input().split()))
answer = [-1] * n

# 스택에 인덱스 넣기
stack = [0]

for i in range(1, n):
    while stack and array[stack[-1]] < array[i]:
        # 스택의 오른쪽부터 빠져나감
        answer[stack.pop()] = array[i]
    stack.append(i)

print(*answer)