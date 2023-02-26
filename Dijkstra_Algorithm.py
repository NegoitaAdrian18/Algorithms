import heapq


def dijkstra(graph, start_node):
    nodes_visited = set()
    distances = {start_node: 0}
    priority_queue = [(0, start_node)]

    while priority_queue:
        weight, node = heapq.heappop(priority_queue)
        if node not in nodes_visited:
            nodes_visited.add(node)
            for neighbor, distance in graph[node].items():
                if neighbor not in distances or distances[node] + distance < distances[neighbor]:
                    distances[neighbor] = distances[node] + distance
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    return distances


graph = {
    "A": {
        "B": 4,
        "C": 2
    },
    "B": {
        "D": 2,
        "E": 3,
        "C": 3
    },
    "C": {
        "B": 1,
        "D": 4,
        "E": 5
    },
    "D": {},
    "E": {
        "D": 1
    }
}

print(dijkstra(graph, "A"))
