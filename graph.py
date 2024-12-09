
'''
'Graph' klassen indeholder attributter og metoder til at
repræsentere en grafstruktur og udføre stifindealgoritmer på den.

Grafens knuder kaldes 'nodes', og dens kanter kaldes 'edges'.

Grafen initialiseres med to lister: nodes og edges
    nodes er blot en liste af strings der repræsenterer knude i grafen (f.eks. ['a', 'b', 'c'])
    edges er en liste af tuples der indeholder strengen for 2 knuder, (f.eks. [('a', 'b'), ('b', 'c'), ('c', 'a')])

Derudover initialiseres grafen også med sandhedsværdien 'directed' 
 som bestemmer om grafen er en orienteret graf

For at udføre stifinderalgoritmer med Dijkstra og A* algoritmerne, udregnes en kantvægt også for hver kant
 ud fra koordinaterne genereret af networkx modulet

'''
# networkx håndterer grafer som kan tegnes med matplotlib
import networkx as nx

from math import sqrt, inf

class Graph:
    def __init__(self, 
                 nodes: list[str], 
                 edges: list[tuple[str, str]], 
                 directed: bool
                 ):
        
        self.nodes = nodes
        self.edges = edges
        self.directed = directed
        
        # hvis directed værdien er sand laves grafen til en DiGraph, 
        # som i networkx sørger for at grafen er orienteret
        if self.directed:
            self.nxGraph = nx.DiGraph()
        else:
            self.nxGraph = nx.Graph()

        # knuder og kanter tilføjes til nx grafen
        self.nxGraph.add_nodes_from(self.nodes)
        self.nxGraph.add_edges_from(self.edges)

        # grafpositionering oprettes. dette tildeler grafens knuder nogen koordinater,
        # som matplotlib kan arbejde med når grafen tegnes
        self.graphPos = nx.spring_layout(self.nxGraph, seed=1)

        # kantvægte beregnes ved afstanden mellem knuderne i kanten for hver kant
        for edge in self.edges:
            firstNodePos = self.graphPos[edge[0]] # giver en tuple (x, y)
            secondNodePos = self.graphPos[edge[1]]
            weight = sqrt((firstNodePos[0] - secondNodePos[0])**2 + (firstNodePos[1] - secondNodePos[1])**2)
            edge.append(weight)
            

        # Der genereres en dictionary indeholdende samtlige knuder i grafen
        # for hver knude laves en subdictionary der indeholder information om knuden:
        #   - knudens naboknuder samt vægten af kanten som leder til en nabo
        #   - dens afstandslabel som bruges i stifinderalgoritmerne
        # 
        # Strukturen ser sådan ud:
        #    graph = {
        #        "V1": {"neighbours": [(node, weight)], "label": float},
        #        "V2": {"neighbours": [(node, weight)], "label": float},
        #        ...
        #        "Vn": {"neighbours": [(node, weight)], "label": float}
        #    }

        # indsæt alle knuder som nøgler i en dict
        # (hver knude gives labelet 'inf' (infinity) da dette bruges i stifinderalgoritmerne)
        self.graph = {node: {"neighbours": [], "label": inf} for node in self.nodes}

        # kør igennem listen af kanter, og definer de enkelte knuders naboknuder 
        # og kantvægten der fører hen til naboknuderne
        for edge in self.edges:
            self.graph[edge[0]]["neighbours"].append((edge[1], edge[2]))
            if self.directed == False:
                self.graph[edge[1]]["neighbours"].append((edge[0], edge[2]))
        

    def printGraphStructure(self):
        for key in self.graph:
            print(str(key) + ": " + str(self.graph[key]))



# test
if __name__ == "__main__":
    nodes = ["a", "b", "c"]
    edges = [('a', 'b', 4), ('b', 'c', 3), ('c', 'a', 5)]
    G = Graph(nodes, edges, True)
    G.printGraphStructure()