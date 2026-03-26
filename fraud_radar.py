# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:25:31 2026

@author: pablo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

print("🎨 Preparando el lienzo para el Radar de Fraudes...")

# 1. Cargamos los datos originales
df = pd.read_excel("Transacciones_Bancarias.xlsx")

# 2. Corremos el detective rapidísimo de nuevo para tener las etiquetas
modelo = IsolationForest(contamination=0.01, random_state=42)
df['Veredicto_IA'] = modelo.fit_predict(df[['Monto_USD', 'Hora_del_Dia', 'Ubicacion_Frecuente']])

# Convertimos el -1 y 1 en palabras para que la gráfica se lea fácil
df['Tipo_Transaccion'] = df['Veredicto_IA'].map({1: 'Normal (Validada)', -1: '🚨 Anomalía (Fraude)'})

# 3. CONFIGURACIÓN DEL DIBUJO
plt.figure(figsize=(12, 7))
sns.set_style("darkgrid") # Un fondo elegante

# Creamos un gráfico de dispersión (Scatter Plot)
print("🛰️ Dibujando 5,000 puntos de datos en el radar...")
grafico = sns.scatterplot(
    data=df, 
    x='Hora_del_Dia', 
    y='Monto_USD', 
    hue='Tipo_Transaccion', # El color depende de si es fraude o normal
    palette={'Normal (Validada)': '#3498db', '🚨 Anomalía (Fraude)': '#e74c3c'}, # Azul y Rojo
    alpha=0.6, # Hacemos los puntos un poco transparentes
    s=50 # Tamaño de los puntos
)

# 4. TOQUES FINALES DE DISEÑO
plt.title('Radar de Inteligencia Artificial: Detección de Fraudes (Isolation Forest)', fontsize=16, fontweight='bold')
plt.xlabel('Hora del Día (Formato 24h)', fontsize=12)
plt.ylabel('Monto de la Transacción (USD)', fontsize=12)
plt.xticks(range(0, 25, 2)) # Que el eje X muestre de 2 en 2 horas

# Guardamos la gráfica como una imagen de alta calidad
nombre_imagen = "Radar_Anomalias.png"
plt.savefig(nombre_imagen, dpi=300, bbox_inches='tight')

print(f"✅ ¡Gráfica generada con éxito! Se ha guardado como '{nombre_imagen}'.")

# Mostramos la gráfica en pantalla
plt.show()