from PyQt5 import QtGui, QtWidgets, QtCore
import pyqtgraph as pg
import math
import numpy as np
 
    
def roi_moved(roi):
	if roi[0] == 'roi1':
		poly = roi[1].getState()['points']
		poly_ = np.array(poly)
		poly_ = np.round(poly_, 4)
		poly1 = poly_.tolist()
		 
		print(f"roi1: {poly1}")
	if roi[0] == 'roi2':
		poly = roi[1].getState()['points']
		poly_ = np.array(poly)
		poly_ = np.round(poly_, 4)
		poly2 = poly_.tolist()
		 
		print(f"roi2: {poly2}")
	

app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget()
win.show()

view = win.addViewBox()
view.setAspectLocked(True)

close1 = [[0, 0], [0.5, 0],[1,2], [0.5, 0.5], [0, 0.5]]
 
close2 = [[0.2, 0.2], [0.2, 0.8], [0.8, 0.8], [0.8, 0.2]]
 

roi1 = pg.PolyLineROI(close1, closed=True, movable=True) #, pos=[0, 0])
roi2 = pg.PolyLineROI(close2, closed=True, movable=True) #, pos=[0.5, 0.5])

view.addItem(roi1)
view.addItem(roi2)

# Connect the signals
roi1.sigRegionChangeFinished.connect(lambda: roi_moved(["roi1",roi1]))
roi2.sigRegionChangeFinished.connect(lambda: roi_moved(["roi2",roi2]))

# Wait until the ROIs are displayed before trying to move them
app.processEvents()

# Move the ROIs
'''
roi1.setPos([0.1, 0.1])
roi2.setPos([0.6, 0.6])
'''
app.exec_()

 
