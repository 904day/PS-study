# 백준 2623 음악 프로그램
import sys
from collections import deque
read = sys.stdin.readline

def topology_sort():
    queue = deque()
    result = []

    # 진입 차수가 0인 모든 노드를 큐에 넣음.
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        # 현재 노드와 연결된 모든 노드의 진입차수 -1
        for next in graph[current]:
            indegree[next] -= 1

            if indegree[next] == 0:
                queue.append(next)
                
    return result

# 가수의 수, 보조 PD의 수
N,M = map(int,read().split())
indegree = [0] * (N+1)
graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    broadcast = list(map(int,read().split()))

    for i in range(1, broadcast[0]):
        graph[broadcast[i]].append(broadcast[i+1])
        indegree[broadcast[i+1]] += 1

answer = topology_sort()

if len(answer) == N:
    print(*answer, sep =' ')
else:
    print(0)