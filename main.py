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


# testværdier til tegning af graf
test_nodes = ['a', 'b', 'c', 'd', 'e', 'f']
test_edges = [['a', 'b'], ['b', 'c'], ['c', 'a'], ['a', 'f'], ['a', 'd'], ['d', 'b'], ['b', 'e'], ['e', 'a']]


# klasse der indeholder programvinduet
class GraphApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        G = Graph(test_nodes, test_edges, False)
        G.draw(self.ax)


app = QApplication(sys.argv)
window = GraphApp()
window.show()
sys.exit(app.exec())