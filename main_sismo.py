
import streamlit as st
from PIL import Image
from pydantic import BaseModel
import joblib
import numpy as np


#https://sismo-henry.streamlit.app/

def clasificar_sismo(Magnitud: float, Intensidad: float ):
    # Carga del modelo entrenado
    model = joblib.load("kmeans_model.pkl")
    

    # Realizar la clasificación utilizando el modelo entrenado
    clasificacion = model.predict([[Magnitud, Intensidad]])

    # Convertir el resultado en un tipo de datos nativo de Python
    clasificacion = clasificacion.item()

    # Asignar texto de acuerdo a la clasificación
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

    return { "texto": texto}






def main():
    st.image("imagen.png", use_column_width=True)

    st.title("Clasificación Sismo")

    Magnitud = st.number_input("Ingrese la magnitud:", value=0.0)
    Intensidad = st.number_input("Ingrese la intensidad:", value=0.0)

    if st.button("Clasificar"):
        resultado = clasificar_sismo(Magnitud, Intensidad)
        st.success(resultado["texto"])

    # Agregar los textos debajo del formulario
    st.write("""
Magnitud:

Menos de 2.0: Generalmente no se percibe, excepto en condiciones muy favorables.
2.0 a 3.9: A menudo se percibe, pero rara vez causa daños.
4.0 a 4.9: Se siente como un temblor de vibración menor, similar a la de un camión que pasa. Raramente causa daños.
5.0 a 5.9: Puede causar daños significativos en edificios y estructuras mal construidas en áreas pobladas.
6.0 a 6.9: Puede causar una gran cantidad de daños en áreas habitadas en un rango de hasta unos 160 kilómetros alrededor del epicentro.
7.0 a 7.9: Puede causar daños graves en áreas más grandes.
8.0 o superior: Un terremoto de esta magnitud puede causar daños devastadores en áreas extensas.
""")
    st.write("")
    st.write("---------------------------------------------------------------------")
    st.write("""
Intensidad:

I. No se siente.
II. Se siente solo por unas pocas personas en reposo y en posición tranquila.
III. Se siente dentro de los edificios, especialmente en los pisos superiores.
IV. Se siente como un camión pesado que pasa cerca o como una vibración similar al paso de un tren.
V. Se siente ampliamente en el área afectada. Los objetos colgantes pueden oscilar y se pueden escuchar ruidos.
VI. Se siente por todas las personas. Los objetos frágiles se rompen y se pueden producir grietas en las paredes.
VII. Daños menores en las estructuras, como grietas en los muros y caída de revestimientos.
VIII. Daños importantes en las estructuras, como colapso parcial de edificios y chimeneas.
IX. Daños severos en las estructuras, con colapso parcial generalizado.
X. Daños extensos en las estructuras, con colapso de muchos edificios.
XI. Daños de gran alcance, con colapso de la mayoría de los edificios.
XII. Daño total. Las estructuras se desploman y el terreno puede agrietarse y deformarse.
""")
    st.write("")
    st.write("---------------------------------------------------------------------")
    st.write("""
GAP:

GAP < 30: Excelente<br>
30 ≤ GAP < 60: Buena<br>
60 ≤ GAP < 90: Razonable<br>
90 ≤ GAP < 120: Pobre<br>
GAP ≥ 120: Muy pobre<br>


* Excelente: Cobertura angular óptima, alta precisión en la ubicación y estimación de la magnitud del terremoto.
* Buena: Cobertura angular adecuada, buena precisión en la ubicación y estimación de la magnitud del terremoto.
* Razonable: Cobertura angular aceptable, precisión razonable en la ubicación y estimación de la magnitud del terremoto.
* Pobre: Cobertura angular deficiente, precisión reducida en la ubicación y estimación de la magnitud del terremoto.
* Muy pobre: Cobertura angular muy deficiente, baja precisión en la ubicación y estimación de la magnitud del terremoto.
""")

if __name__ == '__main__':
    main()