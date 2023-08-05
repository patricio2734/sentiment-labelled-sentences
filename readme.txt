# Diseño e implementacion de una herramienta de visualizacion para explorar el proceso de aprendizaje activo en algoritmos de clasificacion
==============================================================================================================================
## Descripcion del proyecto
===============================================================================================================================
Este documento sirve como guia para poder instalar y ocupar la herramienta de visualizacion.
La herramienta de visualizacion es un software que le permite al usuario ver las curvas de aprendizaje, 
distribucion de clases, errores de validacion y entrenamiento. Es importante señalar que el software debe 
cargar un archivo pkl con una estructura especifica que se va a detallar a continuacion. Se guiara al usuario 
para poder entrenar un set de datos con el mismo algoritmo para entrenar los modelos, para luego exportar los 
resultados y cargarlos en la herramienta de visualizacion.
===============================================================================================================================
## Instalacion
===============================================================================================================================
Para un correcto funcionamiento del software es necesario tener las librerias instaladas con las versiones correspondientes, 
dado que no se puede asegura que con nuevas versiones de estas librerias el software funcione correctamente. 
Se dividen las librerias utilizadas en dos; las utilizadas en el notebook de jupyter y las utilizadas en Spyder IDLE. 
La más importante son las de Spyder IDLE, dado que posibiltan al IDLE Spyder que al ejecutar el archivo Main.py se inicie el software.

===============================================================================================================================
### librerias utilizadas y versiones
===============================================================================================================================
#### Jupyter notebook
re: 2.2.1
numpy: 1.22.3
random
os
tensorflow: 2.9.1
WordCloud, STOPWORDS
matplotlib.pyplot: 3.5.2
pandas: 1.4.4
loadtxt
Sequential: 2.9.0
Dense, Dropout, Input: 2.9.0
GlorotUniform: 2.9.0
to_categorical: 2.9.0
Model: 2.9.0
StandardScaler: 1.1.2
TfidfTransformer: 1.1.2
TfidfVectorizer: 1.1.2
CountVectorizer: 1.1.2
KFold: 1.1.2
Pipeline: 1.1.2
shuffle: 1.1.2
MultinomialNB: 1.1.2
SVC: 1.1.2
make_pipeline: 1.1.2
StandardScaler: 1.1.2
accuracy_score: 1.1.2
f1_score: 1.1.2
pylab: 1.22.3
entropy: 1.7.3
Counter
pickle
===============================================================================================================================
#### Spyder
sys: 3.9.12
pickle
pyqtgraph: 0.13.1
QtCore
QtGui, QtWidgets, uic
pyqtSlot
accuracy_score, f1_score, precision_score, recall_score
Counter
matplotlib.pyplot
numpy: 1.22.3
===============================================================================================================================
### Como ejecutar el algoritmo de jupyter notebook

Antes de poder usar la herramienta de visualizacion, es necesario generar el archivo pickle el cual tendra los 
resultados del entrenamiento y prediccion de los modelos entrenados en el jupyter notebook. En el archivo de las 
bases de datos utilizadas, tenemos los set de datos binarios y multiclase, dependiendo del set de datos que se 
quiera entrenar, se utiliza el jupyter notebook **Entrenamiento Binario** o el **Entrenamiento Multiclase**.

Primero se carga el file al jupyter notebook, para luego ejecutar el kernel, se puede ir variando los parametros 
como las epocas, eso si considerando que puede tardar en ejecutar el algoritmo si se dan valores altos. Si se ejecutaron 
las celdas sin error, revise en donde se guardo el archivo pickle, dado que es necesario para cargarlo en la herramienta de visualizacion.

**Nota**: El algoritmo para entrenar los modelos se ejecutara 6 veces, 3 veces por los clasificadores SVM, ANN y NB 
y otras 3 veces con los mismos clasificadores, pero con el enfoque de aprendizaje activo, todo esto el algoritmo lo 
hace automaticamente.
===============================================================================================================================
### Como ejecutar el Main.py
Si se han instalado las librerias con las versiones respectivas del IDLE Spyder, debiera ser posible ejecutar la 
herramienta de visualizacion desde el IDLE Spyder o el archivo Main.py desde la terminal de **Anaconda Powershell Prompt**, 
accediendo a donde se encuentra el Main.py y a continuacion solo es necesario escribir **python Main.py**
===============================================================================================================================
### Como cargar los datos en la herramienta
Si ya logro ejecutar la herramienta, solo falta cargar los datos desde el software, para esto debe hacer click en la 
pestaña **Archivo**, se desplegara dos opciones, haga click en la que diga **Abrir** y luego debe buscar en donde tiene 
guardado el archivo pickle y darle a la opcion Abrir y listo, ya ha cargado los datos, solo queda explorar la herramienta 
de visualizacion cambiando metricas de prediccion y clasificadores.
===============================================================================================================================
## Estructura del directorio

| - README
| - Presentacion_trabajo_titulo.pptx
| - Informe_Trabajo_de_Titulo.pdf
| - Presentacion_trabajo_titulo.pdf
| - Informe_Trabajo_de_Titulo.docx
| - Video_muestra_version_anterior.mp4
| - Video_muestra_version_final.mp4
| - Codigo
|	| -- uoh.jpg
|	| -- interfaz.ui.bak
|	| -- interfaz.ui
|	| -- Main.py
|	| -- Entrenamiento_Binario_final.ipynb
|	| -- Entrenamiento_Multiclase_final.ipynb
|	| -- Base de datos utilizadas
|	|	| -- datos binarios
|	|	|	| --- readme.txt
|	|	|	| --- imdb_labelled.txt
|	|	|	| --- yelp_labelled.txt
|	|	|	| --- amazon_cells_labelled.txt
|	|	| -- datos multiclase
|	|	|	| --- archive.zip
