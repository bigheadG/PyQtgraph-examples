from PyQt5 import QtGui, QtWidgets, QtCore
import pyqtgraph as pg
#from pyqtgraph.Qt import QtGui
import numpy as np

# Create a new PyQtGraph application
#app = QtGui.QApplication([])
app = QtWidgets.QApplication([])
# Create a plot widget
pw = pg.PlotWidget()
pw.setWindowTitle('Polar Plot Example')
pw.show()

# Generate some sample data
theta = np.linspace(0, 2 * np.pi, 100)
r = np.sin(2 * theta)

# Convert polar coordinates to cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create a scatter plot item to represent the data
data = pg.ScatterPlotItem(x=x, y=y, pen='b')

# Add the data to the plot widget
pw.addItem(data)

# Customize the appearance of the plot
pw.getPlotItem().hideAxis('left')
pw.getPlotItem().hideAxis('bottom')
pw.getPlotItem().showGrid(True, True)
pw.getPlotItem().setAspectLocked(True)
pw.getPlotItem().setRange(xRange=[-1, 1], yRange=[-1, 1])

# Start the PyQtGraph event loop to display the plot
app.exec_()

