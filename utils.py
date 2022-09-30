
"""OpenFunc 
    Funcion usada para recibir un archivo de tipo txt con oraciones de opinion y 
    valoracion numerica, se retornan dos arreglos, un arreglo con las oraciones y 
    el arreglo con la valoracion numerica.
    
    Parameters
    ----------
    txt : file
        txt contiene el archivo con las oraciones de opinion, en cada linea del 
        archivo debe contener la oracion y al final un numero binario, 0 o 1.
    
    Returns
    -------
    val_1 : array
        Arreglo que guarda las oraciones como tipo de dato 'string'.
    val_2 : array
        Arreglo que guarda la valoracion binaria como tipo de dato 'int'.
    """
      
"""PrepoFunc
    Funcion usada para recibir un arreglo de oraciones y pre procesar las
    oraciones conviertiendolas en minusculas y eliminando espacios mayores 
    a uno, caracteres no relevantes como por ejemplo: puntos, comas, signos
    de exclamacion, etc.
    
    Parameters
    ----------
    text : array
        text contiene el arreglo de las oraciones de tipo string
    
    Returns
    -------
    text : array
        Arreglo que guarda las oraciones pre procesadas.
    """
import re
import numpy as np

def OpenFunc(txt):   
    val_1=[]
    val_2=[]
    with open(txt, 'r') as file_object:
        val_1 = file_object.readlines()
    for i in range (0,len(val_1)):
        val_2.append(int(val_1[i][-2]))
        val_1[i]=val_1[i].replace(val_1[i][-2:-1],' ')#.replace('.',''))
    return np.array(val_1), np.array(val_2)


def PreproFunc(text):    
    for i in range(0,len(text)):
        text[i] = text[i].lower()
        text[i] = re.sub(r'[^a-z]', ' ',text[i])
        text[i] = re.sub(r'\s+', ' ',text[i]).strip()
        #agregar lineas para stopwords
        
    return text