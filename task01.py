import networkx as nx
import matplotlib.pyplot as plt

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

# Візуалізуємо отриманий граф
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title("Road Network Between Ukrainian Oblast Cities")
plt.show()

# Аналізуємо грав
print("Кількість верший (міст):", G.number_of_nodes())
print("Кількість ребер (сполучень доріг):", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))