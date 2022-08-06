"""
선택 정렬 (Selection sort)
처음 자리에 들어갈 애들 모든 배열 중 판단, 한 루프 돌면 앞에서 부터 자리가 완성됨.
"""

array = [3, 4, 5, 2, 1, 6, 7]

for i in range(len(array)):
    tmp = array[i]
    idx = -1
    for j in range(i, len(array)):
        if tmp > array[j]:
            tmp = array[j]
            idx = j

    if idx != -1:
        array[i], array[idx] = array[idx], array[i]

print(array)