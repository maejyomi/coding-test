[["ICN", "JFK"], ["HND", "IAD"]]

# path 경로, visit 내가 방문했던 곳

def dfs(graph, path, visit):
    if path:
        to = path[-1]
        if graph[to]: path.append(graph[to].pop(0)) # 갈 수 있으면 추가
        else: visit.append(path.pop()) # 순회에서 갈 수 없다 = 이미 갔다 온 것
        dfs(graph, path, visit)
    return visit[::-1]

def solution(tickets):
    from collections import defaultdict # 키 잡고 값 넣는 걸 자동으로,,
    graph = defaultdict(tickets)
    for a, b in tickets: graph[a].append(b)
    # 딕셔너리 정렬
    for key in graph.keys(): graph[key].sort()