"""
python default sort
: stable sort
"""
point = [[1, 2], [2, 3], [3, 1], [3, 5]]

""" key = lambda x : (우선순위 더 높은 키 값, 다음 우선순위 키 값) 으로 정렬 """
point.sort(key=lambda x: (x[1], x[0]))
for p in point:
    print("{} {}".format(p[0], p[1]))
