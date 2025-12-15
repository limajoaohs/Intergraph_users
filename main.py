import networkx as nx
import matplotlib.pyplot as plt
from intergraph_users import intergraph_users

name1 = "IL/state_IL_city_Dupo.graphml"
name2 = "IL/state_IL_city_Millstadt.graphml"

G1 = nx.read_graphml("graphs/" + name1, force_multigraph=True)
G2 = nx.read_graphml("graphs/" + name2, force_multigraph=True)

c_users = intergraph_users(G1, G2)

print(c_users.nodes)
print([c_users.nodes[u]['label'] for u in c_users.nodes])
print(c_users.edges)
print([(c_users.nodes[u]['label'], c_users.nodes[b]['label']) for b, u in c_users.edges])

user_nodes = [n for n, d in c_users.nodes(data=True) if d.get('type') == 'user']
business_nodes = [n for n, d in c_users.nodes(data=True) if d.get('type') == 'business']

pos = nx.spring_layout(c_users, seed=42)

plt.figure(figsize=(10, 8))

nx.draw_networkx_nodes(c_users, pos, nodelist=user_nodes, node_color='skyblue', node_size=500)
nx.draw_networkx_nodes(c_users, pos, nodelist=business_nodes, node_color='lightgreen', node_size=500)

nx.draw_networkx_edges(c_users, pos, alpha=0.5)
nx.draw_networkx_labels(c_users, pos, labels={n: d['label'] for n, d in c_users.nodes(data=True)}, font_size=8)

plt.axis('off')
plt.show()