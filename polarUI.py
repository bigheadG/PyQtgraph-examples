from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QScatterSeries, QPolarChart, QChart, QChartView, QValueAxis
import random

class MyPolarWindow(QWidget):
    def __init__(self, parent=None):
        super(MyPolarWindow, self).__init__(parent)

        # 创建图表
        self.polarChart = QPolarChart()
        self.chartView = QChartView()

        # 创建Series
        self.scatterSeries = QScatterSeries()

        # 添加数据
        for value in range(1, 50):
            self.scatterSeries.append(value, random.random()*10)
            #scatterSeries.append(QPointF(value, random.random()*10))
        
        self.scatterSeries.setMarkerSize(10)
        self.scatterSeries.setColor(Qt.red)
        self.scatterSeries.setBorderColor(Qt.yellow)
        self.scatterSeries.setMarkerShape(QScatterSeries.MarkerShapeCircle)  # 圆形标记
        # scatterSeries.setMarkerShape(QScatterSeries.MarkerShapeRectangle) # 方形标记        
        self.scatterSeries.setName("星位图")

        self.polarChart.addSeries(self.scatterSeries)
        self.polarChart.setContentsMargins(0, 0, 0, 0)
        self.polarChart.setTheme(QChart.ChartThemeBlueCerulean)
        # polarChart.createDefaultAxes()


        # 设置 角向轴
        self.angularAxis = QValueAxis()
        self.angularAxis.setTickCount(9)
        self.angularAxis.setLabelFormat("%.2f")
        self.angularAxis.setShadesVisible(True)
        self.angularAxis.setShadesBrush(QBrush(QColor(230, 230, 255)))
        self.polarChart.addAxis(self.angularAxis, QPolarChart.PolarOrientationAngular)
        self.angularAxis.setRange(0, 20) # 必须设置范围，否则图表无法显示

        # 设置 径向轴
        self.radialAxis = QValueAxis()
        self.radialAxis.setTickCount(5)
        self.radialAxis.setLabelFormat("%d")
        self.polarChart.addAxis(self.radialAxis, QPolarChart.PolarOrientationRadial)
        self.radialAxis.setRange(0, 10)
        
        self.chartView.setChart(self.polarChart)
        self.chartView.setFocusPolicy(Qt.NoFocus)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.chartView)
        self.setLayout(self.vbox)

        self.polarChart.zoomOut()
        self.polarChart.zoomIn()
        # polarChart.scroll(-1.0, 0)
        # polarChart.scroll(1.0, 0)
        # polarChart.scroll(0, 1.0)
        # polarChart.scroll(0, -1.0)
