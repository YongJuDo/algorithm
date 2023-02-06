n = int(input()) # 정점 개수 (컴퓨터)
m = int(input()) # 간선 개수 (네트워크)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)
print(sum(visited) - 1)