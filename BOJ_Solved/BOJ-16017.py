"""
백준 16017번 : Telemarketer or not?
"""

phone = [int(input()) for _ in range(4)]
if (phone[0] == 8 or phone[0] == 9) and (phone[3] == 8 or phone[3] == 9) and phone[1] == phone[2]:
    print('ignore')
else:
    print('answer')