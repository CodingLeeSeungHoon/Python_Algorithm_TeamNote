"""
삽입 정렬 (Injection_sort)
두 번째 원소부터 앞의 완성된 배열의 자리를 찾아 넣는 알고리즘.
좀 생각이 필요하긴 함.
"""

array = [3, 4, 5, 2, 1, 6, 7]

for i in range(1, len(array)):
    target = array[i]
    idx = i
    for j in range(i-1, -1, -1):
        if array[j] > target:
            array[j], array[idx] = array[idx], array[j]
            idx -= 1

print(array)
