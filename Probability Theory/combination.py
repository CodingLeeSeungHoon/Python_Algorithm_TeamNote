from itertools import combinations
from itertools import combinations_with_replacement

array = [1, 2, 3, 4, 5]

# combination(list, 개수)의 형태로 실행, return된 객체는 combinations 객체이기 때문에 일반적으로
# list로 형변환을 한다.
print(list(combinations(array, 2)))


# 출력 : [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]


# 자기 자신을 포함한 중복 조합을 사용하는 방법은 combinations_with_replacement를 사용하면 된다.
n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]

for result in combinations_with_replacement(num_list, m):
    print(*result)
