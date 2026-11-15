'''
AIM=Visualize Network Data

REL. THEORY=
Network visualization represents relationships between different entities using nodes and edges. Nodes represent objects, while edges represent connections between them. Python NetworkX and Matplotlib libraries help create, analyze, and visualize network structures.

CODE=                                                                '''
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

# Add edges
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('C', 'D'),
    ('C', 'E'), ('D', 'F'),
    ('E', 'F')
]

G.add_edges_from(edges)

# Display network information
print("Network Nodes:")
print(G.nodes())

print("\nNetwork Edges:")
print(G.edges())

print("\nNumber of Nodes:", G.number_of_nodes())
print("Number of Edges:", G.number_of_edges())

# Calculate degree of each node
print("\nNode Degrees:")
for node, degree in G.degree():
    print(node, ":", degree)

# Visualize network
plt.figure(figsize=(8, 6))

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(
    G, pos,
    node_color='skyblue',
    node_size=1000,
    edgecolors='black'
)

nx.draw_networkx_edges(
    G, pos,
    width=2,
    edge_color='gray'
)

nx.draw_networkx_labels(
    G, pos,
    font_size=12,
    font_weight='bold'
)

plt.title("Network Data Visualization")
plt.axis('off')
plt.show()


'''
LO=
1.	Learned to create network graphs.
2.	Understood nodes and edges.
3.	Visualized relationships between connected entities.
'''