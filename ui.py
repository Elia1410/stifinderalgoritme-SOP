# PySide6 importeres til at lave en Qt brugeroverflade
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, 
    QCheckBox, QLabel, QHBoxLayout, QComboBox
)

# MatPlotLib importeres, så vi kan tegne figure i vores vindue
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_Form(object):
    def setupUi(self, Form):
        # centralt widget med vertical layout sættes op til at indeholde gui elementer og graph canvas'et
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)

        # GUI ELEMENTER:
        self.guiLayout = QHBoxLayout()
        self.central_layout.addLayout(self.guiLayout)

        # input til kanter og knuder
        self.inputLayout = QVBoxLayout()
        self.guiLayout.addLayout(self.inputLayout)

        self.tbNodesInput = QLineEdit(self)
        self.tbNodesInput.setPlaceholderText("E.g. a, b, c, ...")
        self.lblNodesInput = QLabel(self, text="Nodes: ")
        self.nodesInputLayout = QHBoxLayout()
        self.nodesInputLayout.addWidget(self.lblNodesInput)
        self.nodesInputLayout.addWidget(self.tbNodesInput)

        self.tbEdgesInput = QLineEdit(self)
        self.tbEdgesInput.setPlaceholderText("E.g. a-b, b-c, c-a, ...")
        self.lblEdgesInput = QLabel(self, text="Edges: ")
        self.edgesInputLayout = QHBoxLayout()
        self.edgesInputLayout.addWidget(self.lblEdgesInput)
        self.edgesInputLayout.addWidget(self.tbEdgesInput)

        self.inputLayout.addLayout(self.nodesInputLayout)
        self.inputLayout.addLayout(self.edgesInputLayout)

        # input af start og slutknude til stifinderalgoritme
        self.tbStartNode = QLineEdit(self)
        self.tbStartNode.setPlaceholderText("Start node")
        self.tbStartNode.setFixedWidth(60)
        self.tbEndNode = QLineEdit(self)
        self.tbEndNode.setPlaceholderText("End node")
        self.tbEndNode.setFixedWidth(60)

        self.startEndLayout = QVBoxLayout()
        self.guiLayout.addLayout(self.startEndLayout)
        self.startEndLayout.addWidget(self.tbStartNode)
        self.startEndLayout.addWidget(self.tbEndNode)


        # 'directed' checkbox og 'draw weights' checkbox
        self.cbDirected = QCheckBox(self, text="Directed")
        self.startEndLayout.addWidget(self.cbDirected)
        self.cbDrawEdgeLabels = QCheckBox(self, text="Draw weights")
        self.startEndLayout.addWidget(self.cbDrawEdgeLabels)

        # 'generate graph' knap og tekstbox
        self.btnGenerateGraph = QPushButton(text="Generate graph")
        self.btnGenerateGraph.setFixedWidth(90)
        self.tbGraphSize = QLineEdit()
        self.tbGraphSize.setPlaceholderText("n nodes")
        self.tbGraphSize.setFixedWidth(90)
        self.inputLayout.addWidget(self.btnGenerateGraph)
        self.inputLayout.addWidget(self.tbGraphSize)



        # dropdown menu til at vælge algoritme, tegn-knap og start-knap
        self.ddSelectAlgorithm = QComboBox()
        self.ddSelectAlgorithm.addItems(['Dijkstra', 'A*', 'Dijkstra (pQ)', 'A* (pQ)'])
        self.btnStart = QPushButton(text="Find shortest path")
        self.btnDraw = QPushButton(text="Draw graph")
        
        self.graphFunctionLayout = QVBoxLayout()
        self.graphFunctionLayout.addWidget(self.btnStart)
        self.graphFunctionLayout.addWidget(self.btnDraw)
        self.graphFunctionLayout.addWidget(self.ddSelectAlgorithm)
        self.guiLayout.addLayout(self.graphFunctionLayout)


        # matpotlib canvas
        self.canvas = FigureCanvas(Figure(figsize=(5, 5)))
        self.central_layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

        # stifinder output
        self.lblPathDisplay = QLabel(text="")
        self.central_layout.addWidget(self.lblPathDisplay)