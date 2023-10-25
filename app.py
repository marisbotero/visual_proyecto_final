import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('datos (1).csv')  # Utilizamos el delimitador de tabulación ya que tus datos parecen estar en formato TSV

# Título
st.title('Dashboard de Análisis Descriptivo PREDICCIÓN DE COBRO ')



# Mostrar datos brutos
st.subheader('Datos brutos')
st.write(df)



# Estadísticas descriptivas
st.subheader('Estadísticas Descriptivas')
st.write(df.describe())

# Gráfico de ImporteTotal por Fecha_Emision
st.subheader('Importe Total por Fecha de Emisión')
fig1 = px.bar(df, x='Fecha_Emision', y='ImporteTotal', title='Importe Total por Fecha de Emisión')
st.plotly_chart(fig1)

# Mostrar distribución de Demora
st.subheader('Distribución de Demora')
fig2 = px.histogram(df, x='Demora', title='Distribución de Demora')
st.plotly_chart(fig2)

# Gráfico de línea del ImporteNet por Fecha_Emision
st.subheader('Importe Neto por Fecha de Emisión')
fig3 = px.line(df, x='Fecha_Emision', y='ImporteNet', title='Importe Neto por Fecha de Emisión')
st.plotly_chart(fig3)

# Gráfico de barras de Pagado por Fecha_Emision
st.subheader('Total Pagado por Fecha de Emisión')
fig4 = px.bar(df, x='Fecha_Emision', y='Pagado', title='Total Pagado por Fecha de Emisión')
st.plotly_chart(fig4)

# Gráfico de pie sobre la condición de pago
st.subheader('Distribución de Condiciones de Pago')
fig5 = px.pie(df, names='Desc_CondicionPago', title='Distribución de Condiciones de Pago')
st.plotly_chart(fig5)

# Gráfico de barras de Demora por Fecha_Emision
st.subheader('Demora por Fecha de Emisión')
fig6 = px.bar(df, x='Fecha_Emision', y='Demora', title='Demora por Fecha de Emisión')
st.plotly_chart(fig6)


# Gráfico de Importe Pendiente de Pago por Fecha_Emision
st.subheader('Importe Pendiente de Pago por Fecha de Emisión')
fig2 = px.bar(df, x='Fecha_Emision', y='FaltaPagar', title='Importe Pendiente de Pago por Fecha de Emisión')
st.plotly_chart(fig2)


# Gráfico de dispersión de Importe Total vs. Importe Neto
st.subheader('Gráfico de dispersión: Importe Total vs. Importe Neto')
fig1 = px.scatter(df, x='ImporteTotal', y='ImporteNet', title='Importe Total vs. Importe Neto')
st.plotly_chart(fig1)

# Histograma de Demora de pagos
st.subheader('Histograma de Demora de Pagos')
fig2 = px.histogram(df, x='Demora', title='Distribución de Días de Demora en Pagos')
st.plotly_chart(fig2)

# Gráfico de barras de Importe Total por tipo de documento (DescTipo)
st.subheader('Importe Total por Tipo de Documento')
fig3 = px.bar(df, x='DescTipo', y='ImporteTotal', title='Importe Total por Tipo de Documento', color='DescTipo')
st.plotly_chart(fig3)

