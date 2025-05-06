import os
import yaml
import networkx as nx

def build_network():
    G = nx.Graph()
    for file in os.listdir('data/processed'):
        if file.endswith('_sentiment.yaml'):
            video_id = file.replace('_sentiment.yaml', '')
            with open(f"data/processed/{file}") as f:
                sentiment = yaml.safe_load(f)
            G.add_node(video_id, sentiment=sentiment['label'])
    nx.write_gexf(G, "data/outputs/network.gexf")
    print("Network built and saved.")

if __name__ == "__main__":
    build_network()
