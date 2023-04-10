import heapq
from collections import deque

def solution(jobs):
    # jobs : [작업이 요청되는 시점, 작업의 소요시간]
    answer = []
    job_queue = deque(sorted(jobs, key=lambda x : x[0]))
    heap = []
    
    time = 0

    while job_queue or heap:
        # 작업 큐에서 실행가능한 힙으로 이동
        while job_queue and job_queue[0][0] <= time:
            start, during = job_queue.popleft()
            # 우선순위, 요청 시점(우선순위가 같으면 요청시간 빠른거부터), 소요 시간
            heapq.heappush(heap, [during, start])
        
        if heap:
            use_time, start = heapq.heappop(heap)
            cost = use_time + time - start
            answer.append(cost)
            time += use_time
        else:
            time += 1
            
    # print(answer)
    return sum(answer) // len(answer)