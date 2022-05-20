"""
백준 18330번 : Petrol
"""

n = int(input())
k = int(input()) + 60

discount = n if k > n else k
more = n-k if n > k else 0
print(discount*1500 + more*3000)
