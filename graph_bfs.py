
from collections import deque

def bfs(start, graph):
    q = deque([start])
    visited = set([start])

    while q:
        node = q.popleft()
        print(node, end=' ')
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

graph = {
    1:[2,3],
    2:[4],
    3:[4],
    4:[]
}

bfs(1, graph)
