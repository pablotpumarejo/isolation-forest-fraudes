# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:18:23 2026

@author: pablo
"""

import pandas as pd
from sklearn.ensemble import IsolationForest

print("🔍 Analizando la evidencia (Iniciando el Detective de IA)...")

# ==========================================
# 1. EXTRACCIÓN
# ==========================================
print("📂 Leyendo el estado de cuenta maestro...")
df = pd.read_excel("Transacciones_Bancarias.xlsx")

# ==========================================
# 2. CONFIGURACIÓN DEL DETECTIVE
# ==========================================
# contamination=0.01 le dice a la IA: "Sospechamos que aprox. el 1% de los datos son fraudes"
modelo = IsolationForest(contamination=0.01, random_state=42)

# ==========================================
# 3. EL INTERROGATORIO (Machine Learning)
# ==========================================
print("🧠 Entrenando al algoritmo e identificando patrones anómalos...")

# Le pedimos que mire estas 3 variables para tomar su decisión
columnas_analisis = ['Monto_USD', 'Hora_del_Dia', 'Ubicacion_Frecuente']

# fit_predict hace dos cosas a la vez: estudia los datos y emite un veredicto.
# Devuelve 1 si es normal, y -1 si es una anomalía (fraude)
df['Veredicto_IA'] = modelo.fit_predict(df[columnas_analisis])

# ==========================================
# 4. CAPTURA Y REPORTE
# ==========================================
# Filtramos únicamente a los culpables (los que tienen -1)
fraudes_detectados = df[df['Veredicto_IA'] == -1].copy()
transacciones_normales = df[df['Veredicto_IA'] == 1]

# Le ponemos una etiqueta bonita para el reporte de Excel
fraudes_detectados['Alerta_Seguridad'] = '🔴 BLOQUEO PREVENTIVO'
# Borramos la columna de -1 porque ya no la necesitamos en el reporte final
fraudes_detectados = fraudes_detectados.drop(columns=['Veredicto_IA'])

print("-" * 50)
print(f"✅ Auditoría completada en milisegundos.")
print(f"📊 Transacciones normales validadas: {len(transacciones_normales)}")
print(f"🚨 Anomalías bloqueadas (Fraudes): {len(fraudes_detectados)}")
print("-" * 50)

# Guardamos la evidencia para el equipo de seguridad
archivo_alertas = "Reporte_Fraudes_Detectados.xlsx"
fraudes_detectados.to_excel(archivo_alertas, index=False)

print(f"💾 Reporte ejecutivo guardado en: {archivo_alertas}")
print("\nTop 3 transacciones más críticas detectadas:")
# Ordenamos para mostrar los montos más altos hasta arriba
print(fraudes_detectados.sort_values(by='Monto_USD', ascending=False).head(3))