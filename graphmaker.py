# PySide6 importeres til at lave en Qt brugeroverflade
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QCheckBox, QLabel, QHBoxLayout
)
import sys

# MatPlotLib importeres, så vi kan tegne figure i vores vindue
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# networkx håndterer grafer
import networkx as nx



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

        # Input fields, button and checkbox
        self.tb_nodeInput = QLineEdit(self)
        self.tb_nodeInput.setPlaceholderText("Enter nodes (e.g., A,B,C)")
        self.tb_edgeInput = QLineEdit(self)
        self.tb_edgeInput.setPlaceholderText("Enter edges (e.g., A-B,B-C)")
        self.btn_draw = QPushButton("Draw Graph", self)
        self.btn_draw.clicked.connect(self.draw_graph)
        self.cb_directedGraph = QCheckBox("Directed graph")

        # Add inputs to layout
        self.input_layout.addWidget(QLabel("Nodes:"))
        self.input_layout.addWidget(self.tb_nodeInput)
        self.input_layout.addWidget(QLabel("Edges:"))
        self.input_layout.addWidget(self.tb_edgeInput)
        self.input_layout.addWidget(self.btn_draw)
        self.input_layout.addWidget(self.cb_directedGraph)

        # Graph canvas
        self.canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

    def draw_graph(self):
        # Clear the plot
        self.ax.clear()

        # Read user input
        nodes = self.tb_nodeInput.text().split(",")
        edges = [tuple(edge.split("-")) for edge in self.tb_edgeInput.text().split(",") if "-" in edge]

        print(edges)

        # Create graph
        if self.cb_directedGraph.isChecked():
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        # Use a circular layout for better visualization of small graphs
        pos = nx.spring_layout(G, seed=1)
        if 'a' in pos.keys() and 'b' in pos.keys() and 'c' in pos.keys():
            print(pos['a'])
            print(pos['b'])
            print(pos['c'])

        # Draw the graph
        nx.draw_networkx(
            G, pos, ax=self.ax, 
            node_size=300, node_color='lightblue', 
            with_labels=True, width=2)
        if self.cb_directedGraph.isChecked():
            nx.draw_networkx_edges(G, pos, ax=self.ax, arrows=True, arrowsize=25, arrowstyle="-|>")

        # Add title and update canvas
        self.ax.set_title("Graph Visualization", fontsize=14)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphApp()
    window.show()
    sys.exit(app.exec())


    #A1-A2,A2-A3,B1-B2,B2-B3,C1-C2,C2-C3,A1-B1,B1-C1,A2-B2,B2-C2,A3-B3,B3-C3
    #A1,A2,A3,B1,B2,B3,C1,C2,C3
