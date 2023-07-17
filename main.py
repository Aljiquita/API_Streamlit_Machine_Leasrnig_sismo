from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


Magnitud: float
Intensidad: float

# Carga del modelo entrenado
model = joblib.load("kmeans_model.pkl")

# Creación de la aplicación FastAPI
app = FastAPI()


    
# Realizar la clasificación utilizando el modelo entrenado
clasificacion = model.predict([[Magnitud, Intensidad]])

# Convertir el resultado en un tipo de datos nativo de Python
clasificacion = np.asscalar(clasificacion)

if clasificacion == 0:
    texto = f""" La clasificación es {clasificacion}, 
    Los sismos en este rango tienen una intensidad perceptible 
    que va desde niveles bajos hasta niveles ampliamente perceptibles en el área afectada. 
    Pueden provocar daños menores en estructuras, 
    como grietas en los muros y caída de revestimientos, 
    y ser percibidos por un número variable de personas, 
    desde unas pocas en reposo y en posición tranquila 
    hasta todas las personas en el área afectada.
    """
elif clasificacion == 1:
    texto = f""" La clasificación es {clasificacion}, 
    Los sismos en este rango tienen una intensidad que generalmente no se percibe, 
    excepto en condiciones muy favorables, 
    hasta niveles que a menudo se perciben, 
    pero rara vez causan daños. 
    En términos de magnitud, 
    van desde temblores que se sienten como vibraciones menores 
    hasta sismos que pueden causar daños menores en estructuras.
    """
elif clasificacion == 2:
    texto = f""" La clasificación es {clasificacion}, 
    los sismos en este rango tienen una intensidad que generalmente no se percibe, 
    pero que en condiciones favorables puede ser percibida por unas pocas personas en reposo 
    y en posición tranquila. 
    Además, la magnitud de estos sismos va desde temblores de vibración menor 
    hasta la capacidad de causar una gran cantidad de daños en áreas habitadas.
    """
elif clasificacion == 3:
    texto = f""" La clasificación es {clasificacion}, 
    los sismos en este rango tienen una intensidad que a menudo se percibe 
    y puede causar una gran cantidad de daños en áreas habitadas, 
    junto con una magnitud que va desde temblores menores 
    hasta la capacidad de causar daños significativos en estructuras.
    """
elif clasificacion == 4:
    texto = f""" La clasificación es {clasificacion}, 
    los sismos en este rango tienen una intensidad 
    que puede causar daños significativos en áreas más grandes 
    y una magnitud que va desde la capacidad de causar daños significativos
    en estructuras hasta la posibilidad de ocasionar daños extensos 
    e incluso colapso total de edificios.
    """
else:
    texto = f"{clasificacion}"

    