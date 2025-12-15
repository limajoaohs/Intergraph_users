import networkx as nx

def intergraph_users(g1, g2):
    # Check if input graphs are valid. If either is None or empty, return None.
    if not g1 or not g2:
        return None
    
    # Create a new empty graph to store the result.
    g_final = nx.Graph()

    # Identify common users between g1 and g2.
    common_users = [(n, d) for n, d in g1.nodes(data=True) if d.get('type') == 'user' and n in g2.nodes()]

    # Add the identified common users to the final graph.
    g_final.add_nodes_from(common_users)

    # Iterate over each common user found.
    for u, _ in common_users:
        # For each common user, check their neighbors in both graphs g1 and g2.
        for g in (g1, g2):
            for v in g.neighbors(u):
                node_data = g.nodes[v]
                # If the neighbor is of type 'business', it is relevant for the final graph.
                if node_data.get('type') == 'business':
                    # Add the business node to the final graph if it is not already there.
                    if v not in g_final:
                        g_final.add_node(v, **g.nodes[v])
                    # Add an edge between the user and the business in the final graph.
                    g_final.add_edge(u, v)

    return g_final