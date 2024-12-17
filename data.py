from graph import Graph
from graphmaker import makeGraph
from timeit import default_timer as timer
import pandas as pd
import gc
from random import choice

algo = Graph.dijkstraPQueue
rep = 25

graphSizes = [15, 30, 45, 60, 85, 100, 125, 150, 175, 200, 250, 300, 350, 400, 450]

DATA = {}

G = None
nodes = None
edges = None

for i in graphSizes:
    del G
    del nodes
    del edges
    gc.collect
    nodes, edges = makeGraph(i)
    total_time = 0

    print(f"{i}: ", end="")

    for j in range(rep):
        print("*", end="")

        node1 = choice(nodes)
        node2 = choice(nodes)
        G = Graph(nodes, edges, False)
        timeStart = timer()
        algo(G, node1, node2)
        timeEnd = timer()
        total_time += timeEnd - timeStart
    
    print()
    
    DATA[i] = total_time/rep
    
for item in DATA:
    print(f"{item}: {DATA[item]}")

df = pd.DataFrame(DATA.items(), columns=['knuder', 'tid'])
df.to_csv("dijkstraPQueue.csv")