import networkx as nx
from collections import deque

# Створюємо граф доріг між обласними центрами України
G = nx.Graph()

# Додаємо вершини з назвами облісних центрів
cities = [
    "Lviv", "Lutsk", "Rivne", "Ternopil", "Ivano-Frankivsk", 
    "Zhytomyr", "Kyiv", "Khmelnytskyi"
]
G.add_nodes_from(cities)

# Додаємо ребра між вершинами, що означають дороги між обласними центрами та відстанню між ними
roads = [
    ("Lviv", "Lutsk", 152),
    ("Lviv", "Rivne", 212),
    ("Lviv", "Ternopil", 128),
    ("Lviv", "Ivano-Frankivsk", 137),
    ("Lutsk", "Rivne", 74),
    ("Lutsk", "Ternopil", 169),
    ("Rivne", "Zhytomyr", 189),
    ("Rivne", "Khmelnytskyi", 195),
    ("Zhytomyr", "Kyiv", 140),
    ("Ternopil", "Khmelnytskyi", 110),
    ("Ivano-Frankivsk", "Ternopil", 140),
    ("Khmelnytskyi", "Zhytomyr", 170),
    ("Kyiv", "Zhytomyr", 140)
]
G.add_weighted_edges_from(roads)

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Запуск рекурсивного алгоритму DFS
print(f"\nРезультати алгоритму DFS:")
dfs_recursive(G, 'Lviv')


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


# Запуск рекурсивного алгоритму BFS
print(f"\nРезультати алгоритму BFS:")
bfs_recursive(G, deque(["Lviv"]))
