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

from timeit import default_timer as timer


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


class GraphApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.G = None

        self.btnDraw.clicked.connect(self.drawGraph)
        self.btnStart.clicked.connect(self.findPath)

    def findPath(self):
        start = self.tbStartNode.text()
        end = self.tbEndNode.text()

        time_start = timer()

        if self.ddSelectAlgorithm.currentText() == "Dijkstra":
            pathNodes = self.G.dijkstraPQueue(start, end)
        else:
            pathNodes = self.G.aStar(start, end)

        time_end = timer()

        self.G.highlightPath(self.ax, pathNodes, self.canvas, self.cbDrawEdgeLabels.isChecked())
        self.lblPathDisplay.setText(f"Path: {pathNodes}   Time: {(time_end-time_start)}s")

    def drawGraph(self):
        nodes = nodeTextBoxToList(self.tbNodesInput.text())
        edges = edgeTextBoxToList(self.tbEdgesInput.text())
        self.G = Graph(nodes, edges, self.cbDirected.isChecked())
        self.G.draw(self.ax, self.canvas, self.cbDrawEdgeLabels.isChecked())
        

app = QApplication(sys.argv)
window = GraphApp()
window.show()
sys.exit(app.exec())
