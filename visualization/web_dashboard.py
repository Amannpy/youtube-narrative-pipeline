import streamlit as st
import networkx as nx

def load_network():
    return nx.read_gexf("data/outputs/network.gexf")

def main():
    st.title("YouTube Narrative Network")
    G = load_network()
    st.write(f"Nodes: {len(G.nodes)}, Edges: {len(G.edges)}")
    sentiment_counts = {}
    for n, d in G.nodes(data=True):
        label = d.get('sentiment', 'unknown')
        sentiment_counts[label] = sentiment_counts.get(label, 0) + 1
    st.bar_chart(sentiment_counts)
    st.write("Download the GEXF file for advanced visualization in Cosmograph or Gephi.")
    with open("data/outputs/network.gexf", "rb") as f:
        st.download_button("Download Network File", f, file_name="network.gexf")

if __name__ == "__main__":
    main()
