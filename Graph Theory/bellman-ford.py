
INF = int(1e9)

# 벨만 포드 알고리즘
def bf(start, n, edges):
    dis = [INF] * (n+1)  # 최단거리 초기화
    dis[start]=0
    # 메인 로직
    # 음의 사이클 판별을 위해 n-1번이 아닌 n번 반복
    for i in range(n):
        # 반복마다 모든 간선 확인
        for edge in edges:
            cur = edge[0] # 출발
            next_node = edge[1] # 도착
            cost = edge[2] # 비용

            # 현재 노드에 도달이 가능하면서
            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[cur] != INF and dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                # i==n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True

    return False