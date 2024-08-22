import plotly.graph_objs as go
import networkx as nx

G = nx.random_geometric_graph(200, 0.125)
pos = nx.get_node_attributes(G, 'pos')
edge_trace = go.Scatter(x=[], y=[], line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace['x'] += (x0, x1, None)
    edge_trace['y'] += (y0, y1, None)

node_trace = go.Scatter(x=[], y=[], mode='markers', hoverinfo='text', marker=dict(showscale=True, size=10, color='blue'))

for node in G.nodes():
    x, y = pos[node]
    node_trace['x'] += (x,)
    node_trace['y'] += (y,)

fig = go.Figure(data=[edge_trace, node_trace])
fig.show()
