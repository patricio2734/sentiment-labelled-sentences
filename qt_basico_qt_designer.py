import sys
import pickle
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

def Funcmetricas(metrica, curva):
    todas = []
    for i in range(5):
        una = []
        for ytrue, ypred, yl in curva[i]:
            if metrica == 'accuracy':   
                valor = accuracy_score(ytrue, ypred)
            elif metrica == 'f1':
                valor = f1_score(ytrue, ypred, average = 'weighted')
            elif metrica == 'pr':
                valor = precision_score(ytrue, ypred, average = 'weighted')
            elif metrica == 'rec':
                valor = recall_score(ytrue, ypred, average = 'weighted')
            una.append(valor) 
        todas.append(una)
    todas = np.mean(todas, axis = 0)
    return todas

Historial = {'64': 0, '128': 1, '192': 2,
            '256': 3, '320': 4, '384': 5,
            '448': 6, '512': 7, '576': 8,
            '640': 9, '704': 10, '768': 11,
            '800': 12}


def Counter_Func(Y, clas, num):
    A = "porcentaje"+str(clas)+": "+'\n'
    historial = {'64': 0, '128': 1, '192': 2,
                '256': 3, '320': 4, '384': 5,
                '448': 6, '512': 7, '576': 8,
                '640': 9, '704': 10, '768': 11,
                '800': 12}
    x,y = Y[clas][:,:,2].shape
    dist = np.empty((x,y), dtype=object)
    for i in range(x):
        for j in range(y):
            dist[i,j] = Counter(Y[clas][:,:,2][i,j])
    dist = dist.sum(axis=0)[historial[str(num)]]
    for k in dist:
        dist[k] = dist[k]/(num*5)
        A += "Clase "+str(k)+": "+str(dist[k]*100)+'%'+'\n'
    return A #str(dist[0]*100)+'%'+'\n'+str(dist[1]*100)+'%'
    #return dist.sum(axis=0)[0][1]

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('interfaz.ui')
        self.ui.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        self.ui.show()
        
        self.widget_plot = self.ui.graphicsView.addPlot()
        self.widget_plot.showGrid(x = True, y = True, alpha = 0.6)
        #self.widget_plot.setXrange(1,5)
        #self.widget_plot.setYrange()
        self.widget_plot.setLabel(axis='bottom', text='Cantidad de datos de entrenamiento')
        self.widget_plot.setLabel(axis='left', text='Metrica')
        self.widget_plot.addLegend()
        
        #self.curve1 = self.widget_plot.plot([], pen=[255,0,0], name = 'MNB')
        pen = pg.mkPen(color=(255, 0, 0), width=1, style=QtCore.Qt.DashLine)
        self.curve1 = self.widget_plot.plot([], pen=pen, name = 'Activo')
        self.curve2 = self.widget_plot.plot([], pen=[0,255,0], name = 'Aleatorio') 
        
        
        #eventos
        self.ui.btn_plot.clicked.connect(self.btn_plot)
        self.ui.btn_clear.clicked.connect(self.btn_clear)
        self.ui.btn_history.setEnabled(False)
        self.ui.btn_history.clicked.connect(self.btn_history)
        self.ui.spinBox.valueChanged.connect(self.spinBox)
        self.value = 64
        
        self.ui.abrir.triggered.connect(self.abrir)
        self.ui.cerrar.triggered.connect(self.cerrar)
        
        self.ui.clasificadores.currentIndexChanged.connect(self.clasificadores)
        self.ui.metricas.currentIndexChanged.connect(self.metricas)

        self.x = []
        self.y1 = []
        self.y2 = []
        self.y3 = []
        
        #variables descripcion
        self.amazon = 0
        self.clasificador_info = 0
        #self.clasificador = 0
        #self.metrica = 0
        
        
    #slots
    @pyqtSlot()
    def btn_plot(self):  
        self.curve1.setData(self.x['Axis_X'], Funcmetricas(self.metrica, self.y1[self.clasificador]))
        self.curve2.setData(self.x['Axis_X'], Funcmetricas(self.metrica, self.y1[self.clasificador +'_PL']))
        self.widget_plot.setLabel(axis='left', text=self.metrica)
        
    @pyqtSlot()
    def btn_clear(self):
        self.curve1.setData([], [])
        self.curve2.setData([], [])
    
    @pyqtSlot()
    def spinBox(self):
        if self.ui.spinBox.value() == 736:
            self.value = 768
            self.ui.spinBox.setValue(self.value)   
            
        self.value = self.ui.spinBox.value()
        self.clasificadores()
        #print(self.x['MNB'])
    
    @pyqtSlot()
    def btn_history(self):
        fig = plt.figure()
        plt.subplot(1,2,1)
        plt.plot(self.x['RED_History'][Historial[str(self.value)]][0], 'orange', label = 'Validation Loss')
        plt.plot(self.x['RED_History'][Historial[str(self.value)]][1], 'blue', label = 'Train Loss')
        plt.xlabel('epochs')
        plt.ylabel('error')
        plt.title('Active Learning')
        plt.legend()
        #plt.show()
        
        #fig2 = plt.figure()
        plt.subplot(1,2,2)
        plt.plot(self.x['RED_PL_History'][Historial[str(self.value)]][0], 'orange', label = 'Validation Loss')
        plt.plot(self.x['RED_PL_History'][Historial[str(self.value)]][1], 'blue', label = 'Train Loss')
        plt.xlabel('epochs')
        plt.ylabel('error')
        plt.title('Passive Learning')
        plt.legend()
        plt.show()
        
    @pyqtSlot()
    def cerrar(self):
        self.ui.close()
        
    @pyqtSlot()
    def clasificadores(self):
        self.clasificador = self.ui.clasificadores.currentText()
        if self.clasificador == 'MNB':    
            self.ui.info_clasificador.setText("Hiperparametros: "+'\n'+"Valor Alfa: "+str(self.clasificador_info['MNB']['alpha'])+'\n'+'\n'+str(Counter_Func(self.x, self.clasificador, self.ui.spinBox.value()))+'\n'+str(Counter_Func(self.x, self.clasificador+'_PL', self.ui.spinBox.value())))
            self.ui.btn_history.setEnabled(False)
        elif self.clasificador == 'SVM':
            self.ui.info_clasificador.setText("Hiperparametros: "+'\n'+"Kernel: "+self.clasificador_info['SVM']['kernel']+'\n'+"Valor de C: "+str(self.clasificador_info['SVM']['C'])+'\n'+'\n'+str(Counter_Func(self.x, self.clasificador, self.ui.spinBox.value()))+'\n'+str(Counter_Func(self.x, self.clasificador+'_PL', self.ui.spinBox.value())))
            self.ui.btn_history.setEnabled(False)
        elif self.clasificador == 'RED':
            self.ui.btn_history.setEnabled(True)
            self.ui.info_clasificador.setText("Hiperparametros: "+'\n'+"Capas ocultas: "+str(self.clasificador_info['RED']['capas_ocultas'])+'\n'+"epocas: "+str(self.clasificador_info['RED']['epocas'])+'\n'+"Batch: "+str(self.clasificador_info['RED']['batch'])+'\n'+"Funciones de activacion: "+str(self.clasificador_info['RED']['funciones_acti'])+'\n'+"optimizador: "+str(self.clasificador_info['RED']['optimizador'])+'\n'+'\n'+str(Counter_Func(self.x, self.clasificador, self.ui.spinBox.value()))+'\n'+str(Counter_Func(self.x, self.clasificador+'_PL', self.ui.spinBox.value())))
        #    self.ui.info_clasificador.setText("c")
        #self.ui.info_clasificador.setText(self.clasificador)
    
    @pyqtSlot()
    def metricas(self):
        self.metrica = self.ui.metricas.currentText()

    @pyqtSlot()
    def abrir(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        with open(path, 'rb') as a:
            datos = pickle.load(a)
        
        self.amazon = datos['descripcion'][list(datos['descripcion'])[0]]
        self.clasificador_info = datos['hiperparametros']
        self.ui.info_dataset.setText("Nombre: "+self.amazon['nombre']+'\n'+"Numero de clases: "+str(self.amazon['nclases'])+'\n'+"Fuente: "+self.amazon['fuente']+'\n'+"Numero de ejemplos: "+str(self.amazon['n_ejemplos']))
        self.x = datos['resultados']
        self.y1 = datos['resultados']
        self.y2 = datos['resultados']
        
app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())
