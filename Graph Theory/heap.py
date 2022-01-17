import heapq

# heapq는 파이썬의 내장 모듈이기 때문에 import 만으로 사용이 가능하다.

"""
heapq 모듈은 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와줍니다. 
자바의 PriorityQueue 클래스처럼 리스트와 별개의 자료구조가 아닌 점에 유의해야 합니다.

그렇게 때문에, 그냥 빈 리스트를 생성해놓은 다음 heapq 모듈의 함수를 호출할 때 마다 이 리스트를 인자로 넘겨야 합니다.
다시말해, 파이썬에서는 heapq 모듈을 통해서 원소를 추가하거나 삭제한 리스트가 그냥 최소 힙입니다.
"""

heap = []  # 일반 리스트

heapq.heappush(heap, 4) # 힙에 삽입하는 과정
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

print(heapq.heappop(heap))  # delete and return element
print(heap)


"""
기존 리스트를 힙으로 변환하는 방법
"""

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

"""
heapq 모듈은 최소 힙(min heap)을 기능만을 동작하기 때문에 최대 힙(max heap)으로 활용하려면 약간의 요령이 필요합니다. 
바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.

따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, 
(우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 됩니다. 
그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됩니다. (우선 순위에는 관심이 없으므로)
"""

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
    print(heapq.heappop(heap)[1])  # 우선순위 말고 값만 꺼내오기