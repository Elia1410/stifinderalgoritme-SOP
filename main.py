'''
Programbeskrivelse:
    Visualiserer Dijkstra's og A* algoritme i at bestemme 
    den korteste vej i en graf.

Lavet af: Elias Schack
Projekt: SOP
Periode: 28-11-2024 til 19-12-2024
Fag: Programmering B og Matematik A

'''

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QLabel, QHBoxLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import sys


class GraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Drawer")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.layout = QVBoxLayout(self.central_widget)
        self.input_layout = QHBoxLayout()
        self.layout.addLayout(self.input_layout)

        # Input fields and button
        self.node_input = QLineEdit(self)
        self.node_input.setPlaceholderText("Enter nodes (e.g., A,B,C)")
        self.edge_input = QLineEdit(self)
        self.edge_input.setPlaceholderText("Enter edges (e.g., A-B,B-C)")
        self.draw_button = QPushButton("Draw Graph", self)
        self.draw_button.clicked.connect(self.draw_graph)

        # Add inputs to layout
        self.input_layout.addWidget(QLabel("Nodes:"))
        self.input_layout.addWidget(self.node_input)
        self.input_layout.addWidget(QLabel("Edges:"))
        self.input_layout.addWidget(self.edge_input)
        self.input_layout.addWidget(self.draw_button)

        # Graph canvas
        self.canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

    def draw_graph(self):
        # Clear the plot
        self.ax.clear()

        # Read user input
        nodes = self.node_input.text().split(",")
        edges = [tuple(edge.split("-")) for edge in self.edge_input.text().split(",") if "-" in edge]

        # Create graph
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        # Use a circular layout for better visualization of small graphs
        pos = nx.circular_layout(G)

        # Draw the graph
        nx.draw(G, pos, ax=self.ax, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)

        # Add title and update canvas
        self.ax.set_title("Graph Visualization", fontsize=14)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphApp()
    window.show()
    sys.exit(app.exec())
