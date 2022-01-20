# 부분 배열 추출하기

paper = [[i*j for i in range(1, 6)] for j in range(1, 6)]
print(paper)

sub_array = [row[2:4] for row in paper[2:4]]  # 2x2
print(sub_array)
