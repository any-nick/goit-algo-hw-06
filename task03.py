import networkx as nx

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

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0  

    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_node = min(unvisited, key=lambda node: distances[node])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_node] == float('infinity'):
            break

        # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_node)

    return distances
# Виклик алгоритм Дейкстри для вершини Lviv
shortest_paths = dijkstra(G, 'Lviv')
for city, distance in shortest_paths.items():
    print(f"Відстань від Lviv до {city}: {distance} км")
