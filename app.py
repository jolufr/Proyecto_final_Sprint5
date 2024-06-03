import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('E:/JLFR/DataScientist/Sprint5/ProyectoFinal/Proyecto_final_Sprint5/vehicles_us.csv') # leer los datos

st.header('PROYECTO FINAL SPRINT 5')

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
            
disp_button = st.button('Grafico de dispersion') # crear un botón

if disp_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # muestra grafico de dispersion
            fig.show
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)