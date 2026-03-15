import os
import osmnx as ox

# city to download
place = "Tokyo, Japan"

# download road network
G = ox.graph_from_place(place, network_type="drive")

os.makedirs("../data", exist_ok=True)

filepath = "../data/tokyo_roads.graphml"
ox.save_graphml(G, filepath)

print("Saved graph to", filepath)
