from random import random, choice, shuffle, randint
def makeGraph(size):
    nodes = ["v" + str(i) for i in range(size)]
    shuffle(nodes)
    edges = []
    for i in range(len(nodes)-1):
        edges.append([nodes[i], nodes[i+1]])
        for i in range(randint(1, 3)):
            other = choice(nodes)
            while other == nodes[i]:
                other = choice(nodes)
            edges.append([nodes[i], other])
    return (nodes, edges)