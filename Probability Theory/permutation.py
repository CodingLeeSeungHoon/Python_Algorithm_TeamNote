from itertools import permutations

array = [1, 2, 3, 4, 5]

# permutations(list, 개수)의 형태로 실행, return된 객체는 permutations 객체이기 때문에 일반적으로
# list로 형변환을 한다.
print(list(permutations(array, 2)))


# 출력 : [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1),
# (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

