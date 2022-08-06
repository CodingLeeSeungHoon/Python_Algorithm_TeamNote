"""
버블 소트
양 옆의 것을 계속해서 비교, 한 loop 돌 때마다 제일 마지막의 원소의 위치가 결정됨.
마지막의 원소의 위치가 결정되므로, 다음 loop에서도 처음부터 시작하는 것에 유의하면서 짜면 쉽게 짤 수 있을 것 같음.
"""
array = [3, 4, 5, 2, 1, 6, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j+1]:
            tmp = array[j]
            array[j] = array[j+1]
            array[j+1] = tmp
            """
            array[j], array[j+1] = array[j+1], array[j]
            """

print(array)