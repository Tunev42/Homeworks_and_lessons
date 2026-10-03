# Граффы - вершины объедённые рёбрами,
# но есть исключения в виде "изолированных вершин".
# Они не соедены с другими вершинами рёбрами

# social_network = {
#     "user_1": ["user_2", "user_3"],
#     "user_2": ["user_1", "user_4"],
#     "user_3": ["user_1"],
#     "user_4": ["user_2"]
# }
#
# print(f"Connections of user_1 - {social_network['user_1']}")



# обход в ширину
# from collections import deque
#
# def bfs(graph, start, target):
#     queue = deque([[start]])
#     visited = set()
#
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#
#         if node == target:
#             return path
#
#         if node not in visited:
#             visited.add(node)
#
#             for neighbor in graph.get(node, []):
#                 new_path = list(path)
#                 new_path.append(neighbor)
#                 queue.append(new_path)
#
#     return None
#
# social_network = {
#     "user_1": ["user_2", "user_3"],
#     "user_2": ["user_1", "user_4"],
#     "user_3": ["user_1"],
#     "user_4": ["user_2"]
# }
#
# print("Max short from user_1 to user_2", bfs(social_network, 'user_4', 'user_3')) Вывод: ['user_4', 'user_2', 'user_1', 'user_3']

import heapq

def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pred_distance = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                pred_distance[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = pred_distance[current]

    return path, distances[target]

road_map = {
    'home': {'shop': 5, 'intersection': 2},
    'shop': {'home': 5, 'unicum': 6},
    'intersection': {'home': 2, 'shop': 1, 'unicum': 7},
    'unicum': {'shop': 6, 'intersection': 7}
}

path, time = dijkstra(road_map, "home", "unicum")

print(f"Most short way to: {path}, will take {time} minute")
