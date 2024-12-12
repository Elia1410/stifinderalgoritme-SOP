'''
Programbeskrivelse:
    Visualiserer Dijkstra's og A* algoritme i at bestemme 
    den korteste vej i en graf.

Lavet af: Elias Schack
Projekt: SOP - Stifinderalgoritmer
Periode: 28-11-2024 til 19-12-2024
Fag: Programmering B og Matematik A

'''

# PySide6 til Qt vindue med gui
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

# gui importeres fra ui.py
from ui import Ui_Form

from graph import Graph


# tager et string input som brugeren skriver ind i nodes-textbox'en
# og konverterer det til en liste af knuder
def nodeTextBoxToList(nodesString: str):
    nodesStringNoSpaces = nodesString.replace(" ", "")
    return nodesStringNoSpaces.split(",")

# tager et string input som brugeren skriver ind i edges-textbox'en
# og konverterer det til en liste af kanter
# brugeren kan enten input en kant som: a-b  eller med kantvægt som: a-b-5
def edgeTextBoxToList(edgesString: str):
    edgesStringNoSpaces = edgesString.replace(" ", "")
    edgesList = []
    for edge in edgesStringNoSpaces.split(","):
        edgeSplit = edge.split("-")
        if len(edgeSplit) == 3:
            edgesList.append([edgeSplit[0], edgeSplit[1], float(edgeSplit[2])])
        else:
            edgesList.append([edgeSplit[0], edgeSplit[1]])
    return edgesList


# klasse der indeholder programvinduet
class GraphApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.G = None

        self.btnDraw.clicked.connect(self.drawGraph)
        self.btnStart.clicked.connect(self.findPath)

    def findPath(self):
        if self.ddSelectAlgorithm.currentText() == "Dijkstra":
            start = self.tbStartNode.text()
            end = self.tbEndNode.text()
            pathNodes = self.G.dijkstra(start, end)
            print("pathNodes: " + str(pathNodes))
        self.G.highlightPath(self.ax, pathNodes, self.canvas)

    def drawGraph(self):
        nodes = nodeTextBoxToList(self.tbNodesInput.text())
        edges = edgeTextBoxToList(self.tbEdgesInput.text())
        self.G = Graph(nodes, edges, self.cbDirected.isChecked())
        self.G.draw(self.ax, self.canvas)
        


app = QApplication(sys.argv)
window = GraphApp()
window.show()
sys.exit(app.exec())


'''
5x5 grid:
Nodes: v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25 
Edges: v1-v2, v1-v3, v4-v2, v4-v3, v5-v3, v6-v5, v6-v4, v9-v1, v8-v3, v7-v5, v7-v8, v8-v9, v12-v7, v12-v11, v11-v10, v11-v8, v10-v9, v16-v10, v16-v15, v15-v14, v13-v14, v13-v2, v14-v1, v15-v9, v20-v6, v19-v5, v18-v7, v17-v12, v17-v18, v18-v19, v19-v20, v25-v24, v23-v24, v22-v23, v21-v22, v21-v17, v22-v12, v23-v11, v24-v10, v25-v16

a,b,c,d,e
a-b-4, b-c-3, c-a-2, b-d-5, c-d-1, c-e-3, d-e-1


'''