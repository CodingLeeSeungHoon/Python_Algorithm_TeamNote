"""
백준 17009번 : Winning Score
"""
apple, banana = [], []
for _ in range(3):
    apple.append(int(input()))
for _ in range(3):
    banana.append(int(input()))

ascore = apple[0] * 3 + apple[1] * 2 + apple[2]
bscore = banana[0] * 3 + banana[1] * 2 + banana[2]

if ascore > bscore:
    print('A')
elif ascore == bscore:
    print('T')
else:
    print('B')