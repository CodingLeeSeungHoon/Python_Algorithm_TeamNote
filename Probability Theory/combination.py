from itertools import combinations

array = [1, 2, 3, 4, 5]

# combination(list, 개수)의 형태로 실행, return된 객체는 combinations 객체이기 때문에 일반적으로
# list로 형변환을 한다.
print(list(combinations(array, 2)))


# 출력 : [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
