import os
import networkx as nx

def create_mock_graphs():
    nodes_data = [
        ('ZL8cgMY7b8POMaxKgd6u3g', 'Evan', 'user'),
        ('62edU1CH_ki2L0FodOzavA', 'Jane', 'user'),
        ('hKBQ-PFlcB-t5FK3HUxoyQ', 'Wanda', 'user'),
        ('9SQPIP8ASyy6J7Ujjzi3Ag', 'Jennifer', 'user'),
        ('xdQzGzNu3nIUEvOGPW1tYw', 'Aspin', 'user'),
        ('dQg16IsfcluBTkuUDQuGDQ', 'Zoe', 'user'),
        ('YqximOhYJza5Bp4hhnSgUQ', 'Otts Tavern & Millstadt Fish Stand', 'business'),
        ('jopXZhgCjhfx5KjFJKD-vw', 'Happy Days', 'business'),
        ('CSkIucODjUoGRxiIONcSgg', "Farmer's Inn Restaurant & Bar", 'business'),
        ('4hhC-WUKaI-g4QoZEK7yig', "Reinhardt's Restaurant", 'business'),
        ('ttKlWxEaX4trG30xkCDYkA', 'Dollar General', 'business'),
        ('fypGyTRBy5b60RRPG_NQ5g', 'Farmers Inn', 'business'),
        ('tTyFGm2z4zqMXEN_ZWLVfQ', 'China King', 'business'),
        ('0bzkJPZaxJI0aWh20ayBJQ', 'Subway', 'business'),
        ('K0xjMTLYdicHvwLKNFlUZw', "Smokin K's BBQ & More", 'business'),
        ('Vr5bxmQ2C0XMXmT1WyamUQ', "Mariachi's", 'business'),
        ('tzT32YLUpNy-Z2FN77aZrQ', "Eckert's Millstadt Fun Farm", 'business'),
        ('mx1_2BxcIbZ1RKsGG_UPHg', 'Good Times Saloon', 'business'),
        ('TsohTE3w1br2m0Nb-tDRDA', 'Dairyland', 'business'),
        ('NdgNF6Bpk1nLAcKg_j_r9w', 'Triple Lakes Tavern', 'business')
    ]

    edges_data = [
        ('ZL8cgMY7b8POMaxKgd6u3g', 'YqximOhYJza5Bp4hhnSgUQ'), ('ZL8cgMY7b8POMaxKgd6u3g', 'jopXZhgCjhfx5KjFJKD-vw'),
        ('ZL8cgMY7b8POMaxKgd6u3g', 'CSkIucODjUoGRxiIONcSgg'), ('ZL8cgMY7b8POMaxKgd6u3g', 'ttKlWxEaX4trG30xkCDYkA'),
        ('ZL8cgMY7b8POMaxKgd6u3g', 'tTyFGm2z4zqMXEN_ZWLVfQ'), ('ZL8cgMY7b8POMaxKgd6u3g', '0bzkJPZaxJI0aWh20ayBJQ'),
        ('ZL8cgMY7b8POMaxKgd6u3g', 'K0xjMTLYdicHvwLKNFlUZw'), ('ZL8cgMY7b8POMaxKgd6u3g', 'tzT32YLUpNy-Z2FN77aZrQ'),
        ('ZL8cgMY7b8POMaxKgd6u3g', 'TsohTE3w1br2m0Nb-tDRDA'), ('62edU1CH_ki2L0FodOzavA', 'YqximOhYJza5Bp4hhnSgUQ'),
        ('62edU1CH_ki2L0FodOzavA', 'Vr5bxmQ2C0XMXmT1WyamUQ'), ('62edU1CH_ki2L0FodOzavA', 'NdgNF6Bpk1nLAcKg_j_r9w'),
        ('hKBQ-PFlcB-t5FK3HUxoyQ', 'K0xjMTLYdicHvwLKNFlUZw'), ('hKBQ-PFlcB-t5FK3HUxoyQ', 'NdgNF6Bpk1nLAcKg_j_r9w'),
        ('9SQPIP8ASyy6J7Ujjzi3Ag', 'YqximOhYJza5Bp4hhnSgUQ'), ('9SQPIP8ASyy6J7Ujjzi3Ag', 'CSkIucODjUoGRxiIONcSgg'),
        ('9SQPIP8ASyy6J7Ujjzi3Ag', 'mx1_2BxcIbZ1RKsGG_UPHg'), ('xdQzGzNu3nIUEvOGPW1tYw', 'fypGyTRBy5b60RRPG_NQ5g'),
        ('xdQzGzNu3nIUEvOGPW1tYw', 'NdgNF6Bpk1nLAcKg_j_r9w'), ('dQg16IsfcluBTkuUDQuGDQ', '4hhC-WUKaI-g4QoZEK7yig'),
        ('dQg16IsfcluBTkuUDQuGDQ', 'NdgNF6Bpk1nLAcKg_j_r9w')
    ]

    os.makedirs("graphs/IL", exist_ok=True)

    G = nx.Graph()
    for nid, label, ntype in nodes_data:
        G.add_node(nid, label=label, type=ntype)
    G.add_edges_from(edges_data)

    path1 = "graphs/IL/state_IL_city_Dupo.graphml"
    path2 = "graphs/IL/state_IL_city_Millstadt.graphml"
    
    nx.write_graphml(G, path1)
    nx.write_graphml(G, path2)
    
    print(f"Files generated successfully:\n- {path1}\n- {path2}")

if __name__ == "__main__":
    create_mock_graphs()